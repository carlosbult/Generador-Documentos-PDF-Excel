import reflex as rx
from typing import Any
from datetime import datetime
from pathlib import Path
import uuid
import logging
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill


class InvoiceItem(rx.Base):
    id: str
    description: str
    quantity: int
    unit_price: float
    amount: float


class InvoiceState(rx.State):
    """State for the Invoice document."""

    is_loading: bool = False
    from_name: str = "Tu Empresa S.A."
    from_address: str = "Calle Principal 123"
    from_details: str = "Ciudad, País, CP 10001"
    from_email: str = "contacto@tuempresa.com"
    from_phone: str = "+1 234 567 890"
    to_name: str = "Cliente Ejemplo"
    to_company: str = "Empresa Cliente Ltda."
    to_address: str = "Av. Comercial 456"
    to_details: str = "Ciudad Cliente, País"
    invoice_number: str = "INV-2024-001"
    invoice_date: str = ""
    due_date: str = ""
    items: list[InvoiceItem] = [
        InvoiceItem(
            id="1",
            description="Servicios de Consultoría",
            quantity=10,
            unit_price=85.0,
            amount=850.0,
        ),
        InvoiceItem(
            id="2",
            description="Desarrollo Web Frontend",
            quantity=1,
            unit_price=1200.0,
            amount=1200.0,
        ),
    ]
    tax_rate: float = 16.0

    @rx.event
    def on_load(self):
        """Initialize dates on client load to avoid hydration mismatch."""
        if not self.invoice_date:
            today = datetime.now().strftime("%Y-%m-%d")
            self.invoice_date = today
            self.due_date = today

    @rx.var
    def subtotal(self) -> float:
        return sum([item.amount for item in self.items])

    @rx.var
    def tax_amount(self) -> float:
        return self.subtotal * (self.tax_rate / 100)

    @rx.var
    def total(self) -> float:
        return self.subtotal + self.tax_amount

    @rx.event
    def set_field(self, field: str, value: str):
        if hasattr(self, field):
            if field == "tax_rate":
                try:
                    self.tax_rate = float(value)
                except ValueError as e:
                    logging.exception(f"Error converting tax_rate to float: {e}")
                    self.tax_rate = 0.0
            else:
                setattr(self, field, value)

    @rx.event
    def add_item(self):
        self.items.append(
            InvoiceItem(
                id=str(uuid.uuid4()),
                description="Nuevo Item",
                quantity=1,
                unit_price=0.0,
                amount=0.0,
            )
        )

    @rx.event
    def remove_item(self, idx: int):
        if 0 <= idx < len(self.items):
            self.items.pop(idx)

    @rx.event
    def update_item(self, idx: int, field: str, value: Any):
        if 0 <= idx < len(self.items):
            item = self.items[idx]
            if field in ["quantity", "unit_price"]:
                try:
                    val = float(value)
                    if field == "quantity":
                        item.quantity = int(val)
                    else:
                        item.unit_price = val
                    item.amount = item.quantity * item.unit_price
                except ValueError as e:
                    logging.exception(f"Error updating item field {field}: {e}")
            elif field == "description":
                item.description = str(value)
            self.items = self.items

    @rx.event
    async def export_pdf(self):
        self.is_loading = True
        filename = f"Invoice_{self.invoice_number}_{uuid.uuid4().hex[:6]}.pdf"
        upload_dir = Path(".web/public")
        upload_dir.mkdir(parents=True, exist_ok=True)
        file_path = upload_dir / filename
        try:
            doc = SimpleDocTemplate(
                file_path,
                pagesize=letter,
                rightMargin=40,
                leftMargin=40,
                topMargin=40,
                bottomMargin=40,
            )
            elements = []
            styles = getSampleStyleSheet()
            header_data = [
                [
                    Paragraph(
                        f"<b>{self.from_name}</b><br/>{self.from_address}<br/>{self.from_details}<br/>{self.from_email}<br/>{self.from_phone}",
                        styles["Normal"],
                    ),
                    Paragraph(
                        f"<font size=24><b>FACTURA</b></font><br/><br/><b>No:</b> {self.invoice_number}<br/><b>Fecha:</b> {self.invoice_date}<br/><b>Vence:</b> {self.due_date}",
                        styles["Normal"],
                    ),
                ]
            ]
            t_header = Table(header_data, colWidths=[4 * inch, 3 * inch])
            t_header.setStyle(
                TableStyle(
                    [
                        ("VALIGN", (0, 0), (-1, -1), "TOP"),
                        ("ALIGN", (1, 0), (1, 0), "RIGHT"),
                    ]
                )
            )
            elements.append(t_header)
            elements.append(Spacer(1, 40))
            elements.append(Paragraph("<b>FACTURAR A:</b>", styles["Heading4"]))
            elements.append(
                Paragraph(
                    f"{self.to_name}<br/>{self.to_company}<br/>{self.to_address}<br/>{self.to_details}",
                    styles["Normal"],
                )
            )
            elements.append(Spacer(1, 30))
            data = [["DESCRIPCIÓN", "CANT.", "PRECIO", "TOTAL"]]
            for item in self.items:
                data.append(
                    [
                        Paragraph(item.description, styles["Normal"]),
                        str(item.quantity),
                        f"${item.unit_price:,.2f}",
                        f"${item.amount:,.2f}",
                    ]
                )
            t_items = Table(
                data, colWidths=[3.5 * inch, 1 * inch, 1.25 * inch, 1.25 * inch]
            )
            t_items.setStyle(
                TableStyle(
                    [
                        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                        ("FONTSIZE", (0, 0), (-1, 0), 10),
                        ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
                        ("LINEBELOW", (0, 0), (-1, 0), 1, colors.black),
                        ("ALIGN", (1, 0), (-1, -1), "RIGHT"),
                        ("VALIGN", (0, 0), (-1, -1), "TOP"),
                        ("TEXTCOLOR", (0, 0), (-1, 0), colors.gray),
                    ]
                )
            )
            elements.append(t_items)
            elements.append(Spacer(1, 20))
            totals_data = [
                ["Subtotal:", f"${self.subtotal:,.2f}"],
                [f"Impuestos ({self.tax_rate}%):", f"${self.tax_amount:,.2f}"],
                ["Total:", f"${self.total:,.2f}"],
            ]
            t_totals = Table(totals_data, colWidths=[5.75 * inch, 1.25 * inch])
            t_totals.setStyle(
                TableStyle(
                    [
                        ("ALIGN", (0, 0), (-1, -1), "RIGHT"),
                        ("FONTNAME", (0, -1), (-1, -1), "Helvetica-Bold"),
                        ("FONTSIZE", (0, -1), (-1, -1), 12),
                        ("LINEABOVE", (0, -1), (-1, -1), 1, colors.black),
                        ("TOPPADDING", (0, -1), (-1, -1), 10),
                    ]
                )
            )
            elements.append(t_totals)
            doc.build(elements)
            self.is_loading = False
            if not file_path.exists():
                raise FileNotFoundError(f"PDF file was not created: {file_path}")
            return rx.download(url=f"/{filename}", filename=filename)
        except Exception as e:
            self.is_loading = False
            logging.exception(f"PDF Generation Error: {e}")
            return rx.toast.error(f"Error generating PDF: {str(e)}")

    @rx.event
    async def export_excel(self):
        self.is_loading = True
        filename = f"Invoice_{self.invoice_number}_{uuid.uuid4().hex[:6]}.xlsx"
        upload_dir = Path(".web/public")
        upload_dir.mkdir(parents=True, exist_ok=True)
        file_path = upload_dir / filename
        try:
            wb = Workbook()
            ws = wb.active
            ws.title = "Factura"
            title_font = Font(bold=True, size=16)
            header_font = Font(bold=True)
            gray_fill = PatternFill(
                start_color="EEEEEE", end_color="EEEEEE", fill_type="solid"
            )
            ws["A1"] = self.from_name
            ws["A1"].font = title_font
            ws["A2"] = self.from_address
            ws["A3"] = self.from_details
            ws["A4"] = self.from_email
            ws["E1"] = "FACTURA"
            ws["E1"].font = title_font
            ws["E2"] = f"No: {self.invoice_number}"
            ws["E3"] = f"Fecha: {self.invoice_date}"
            ws["A7"] = "FACTURAR A:"
            ws["A7"].font = header_font
            ws["A8"] = self.to_name
            ws["A9"] = self.to_company
            ws["A10"] = self.to_address
            row = 13
            headers = ["Descripción", "Cantidad", "Precio Unitario", "Total"]
            for col, text in enumerate(headers, 1):
                cell = ws.cell(row=row, column=col, value=text)
                cell.font = header_font
                cell.fill = gray_fill
            row += 1
            for item in self.items:
                ws.cell(row=row, column=1, value=item.description)
                ws.cell(row=row, column=2, value=item.quantity)
                ws.cell(row=row, column=3, value=item.unit_price)
                ws.cell(row=row, column=4, value=item.amount)
                row += 1
            row += 2
            ws.cell(row=row, column=3, value="Subtotal:").font = header_font
            ws.cell(row=row, column=4, value=self.subtotal)
            row += 1
            ws.cell(
                row=row, column=3, value=f"Impuestos ({self.tax_rate}%):"
            ).font = header_font
            ws.cell(row=row, column=4, value=self.tax_amount)
            row += 1
            ws.cell(row=row, column=3, value="TOTAL:").font = header_font
            ws.cell(row=row, column=4, value=self.total).font = Font(bold=True)
            ws.column_dimensions["A"].width = 40
            ws.column_dimensions["C"].width = 15
            ws.column_dimensions["D"].width = 15
            wb.save(file_path)
            self.is_loading = False
            return rx.download(url=f"/{filename}", filename=filename)
        except Exception as e:
            self.is_loading = False
            logging.exception(f"Excel Generation Error: {e}")
            return rx.toast.error(f"Error generating Excel: {str(e)}")