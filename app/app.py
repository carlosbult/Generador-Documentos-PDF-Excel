import reflex as rx
from app.pages.dashboard import dashboard
from app.pages.statement import statement_page
from app.pages.invoice import invoice_page
from app.pages.warehouse_receipt import warehouse_receipt_page
from app.pages.quotation import quotation_page

app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(dashboard, route="/")
app.add_page(statement_page, route="/statement")
app.add_page(invoice_page, route="/invoice")
app.add_page(warehouse_receipt_page, route="/warehouse-receipt")
app.add_page(quotation_page, route="/quotation")