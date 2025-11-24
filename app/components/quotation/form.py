"""Quotation form component."""

import reflex as rx
from app.states.quotation_state import QuotationItem, QuotationState


def form_header(title: str, icon: str) -> rx.Component:
    """Create a form section header."""
    return rx.el.div(
        rx.icon(icon, class_name="w-5 h-5 text-purple-600"),
        rx.el.h3(title, class_name="text-lg font-semibold text-gray-800"),
        class_name="flex items-center gap-2 mb-4 pb-2 border-b border-gray-100",
    )


def input_group(
    label: str,
    value: str,
    field_name: str,
    type_: str = "text",
    placeholder: str = "",
    required: bool = False,
) -> rx.Component:
    """Create an input group with label."""
    label_text = f"{label}{'*' if required else ''}"
    return rx.el.div(
        rx.el.label(
            label_text,
            class_name="block text-xs font-medium text-gray-500 mb-1 uppercase tracking-wide",
        ),
        rx.el.input(
            on_change=lambda v: QuotationState.set_field(field_name, v),
            type=type_,
            required=required,
            class_name="w-full px-3 py-2 bg-gray-50 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500/20 focus:border-purple-500 transition-all text-sm",
            default_value=value,
            placeholder=placeholder,
        ),
    )


def item_row(item: QuotationItem, index: int) -> rx.Component:
    """Create a row for a quotation item."""
    return rx.el.div(
        # Delete button
        rx.el.button(
            rx.icon("trash-2", class_name="w-4 h-4"),
            on_click=QuotationState.remove_item(index),
            class_name="p-2 mt-6 text-red-400 hover:text-red-600 hover:bg-red-50 rounded-lg transition-colors",
        ),
        # Description
        rx.el.div(
            rx.el.label(
                "Descripción*",
                class_name="block text-xs font-medium text-gray-500 mb-1",
            ),
            rx.el.input(
                on_change=lambda v: QuotationState.update_item(index, "description", v),
                class_name="w-full px-3 py-2 bg-gray-50 border border-gray-200 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-purple-500/20 focus:border-purple-500",
                default_value=item.description,
                placeholder="Servicio de logística",
            ),
            class_name="col-span-2 md:col-span-2 lg:col-span-2 xl:col-span-3",
        ),
        # Quantity
        rx.el.div(
            rx.el.label(
                "Cantidad",
                class_name="block text-xs font-medium text-gray-500 mb-1",
            ),
            rx.el.input(
                type="number",
                min="1",
                on_change=lambda v: QuotationState.update_item(index, "quantity", v),
                class_name="w-full px-3 py-2 bg-gray-50 border border-gray-200 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-purple-500/20 focus:border-purple-500",
                default_value=item.quantity.to_string(),
            ),
        ),
        # Unit Price
        rx.el.div(
            rx.el.label(
                "Precio Unit.",
                class_name="block text-xs font-medium text-gray-500 mb-1",
            ),
            rx.el.input(
                type="number",
                step="0.01",
                min="0",
                on_change=lambda v: QuotationState.update_item(index, "unit_price", v),
                class_name="w-full px-3 py-2 bg-gray-50 border border-gray-200 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-purple-500/20 focus:border-purple-500",
                default_value=item.unit_price.to_string(),
            ),
        ),
        # Discount
        rx.el.div(
            rx.el.label(
                "Descuento",
                class_name="block text-xs font-medium text-gray-500 mb-1",
            ),
            rx.el.input(
                type="number",
                step="0.01",
                min="0",
                on_change=lambda v: QuotationState.update_item(index, "discount", v),
                class_name="w-full px-3 py-2 bg-gray-50 border border-gray-200 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-purple-500/20 focus:border-purple-500",
                default_value=item.discount.to_string(),
            ),
        ),
        # Total (Read-only)
        rx.el.div(
            rx.el.label(
                "Total", class_name="block text-xs font-medium text-gray-500 mb-1"
            ),
            rx.el.div(
                f"${item.amount:.2f}",
                class_name="px-3 py-2 bg-purple-50 border border-purple-200 rounded-lg text-sm text-right font-bold text-purple-700",
            ),
        ),
        # Notes
        rx.el.div(
            rx.el.label(
                "Notas", class_name="block text-xs font-medium text-gray-500 mb-1"
            ),
            rx.el.input(
                on_change=lambda v: QuotationState.update_item(index, "notes", v),
                class_name="w-full px-3 py-2 bg-gray-50 border border-gray-200 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-purple-500/20 focus:border-purple-500",
                default_value=item.notes,
                placeholder="Nota opcional",
            ),
            class_name="col-span-2 md:col-span-2 lg:col-span-3 xl:col-span-4",
        ),
        class_name="grid grid-cols-3 md:grid-cols-4 lg:grid-cols-5 xl:grid-cols-8 gap-3 items-start p-4 bg-white border border-gray-100 rounded-xl shadow-sm hover:shadow-md transition-all",
    )


def quotation_form() -> rx.Component:
    """Create the main quotation form."""
    return rx.el.div(
        # Quotation Info Section
        rx.el.div(
            form_header("Información de Cotización", "file-text"),
            rx.el.div(
                input_group(
                    "Número de Cotización",
                    QuotationState.quote_number,
                    "quote_number",
                    placeholder="COT-2024-001",
                    required=True,
                ),
                input_group(
                    "Fecha",
                    QuotationState.quote_date,
                    "quote_date",
                    "date",
                    required=True,
                ),
                input_group(
                    "Válida Hasta",
                    QuotationState.valid_until,
                    "valid_until",
                    "date",
                    required=True,
                ),
                class_name="grid grid-cols-3 gap-4 mb-6",
            ),
            class_name="bg-white p-6 rounded-2xl border border-gray-200 shadow-sm mb-6",
        ),
        # Client Info Section
        rx.el.div(
            form_header("Información del Cliente", "user"),
            rx.el.div(
                input_group(
                    "Nombre del Cliente",
                    QuotationState.client_name,
                    "client_name",
                    placeholder="Juan Pérez",
                    required=True,
                ),
                input_group(
                    "Empresa",
                    QuotationState.client_company,
                    "client_company",
                    placeholder="Empresa XYZ C.A.",
                ),
                input_group(
                    "Dirección",
                    QuotationState.client_address,
                    "client_address",
                    placeholder="Av. Principal, Caracas",
                ),
                class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 mb-4",
            ),
            rx.el.div(
                input_group(
                    "Email",
                    QuotationState.client_email,
                    "client_email",
                    "email",
                    placeholder="cliente@ejemplo.com",
                ),
                input_group(
                    "Teléfono",
                    QuotationState.client_phone,
                    "client_phone",
                    "tel",
                    placeholder="+58 424-4966616",
                ),
                class_name="grid grid-cols-2 gap-4 mb-6",
            ),
            class_name="bg-white p-6 rounded-2xl border border-gray-200 shadow-sm mb-6",
        ),
        # Line Items Section
        rx.el.div(
            form_header("Servicios / Productos", "package"),
            rx.el.div(
                rx.foreach(
                    QuotationState.items,
                    lambda item, idx: rx.box(
                        item_row(item, idx),
                        key=item.id,
                    ),
                ),
                class_name="space-y-3 mb-4",
            ),
            rx.el.button(
                rx.icon("plus", class_name="w-4 h-4"),
                "Agregar Item",
                on_click=QuotationState.add_item,
                class_name="flex items-center gap-2 px-4 py-2 bg-purple-600 text-white rounded-lg hover:bg-purple-700 transition-colors text-sm font-medium shadow-sm",
            ),
            class_name="bg-white p-6 rounded-2xl border border-gray-200 shadow-sm mb-6",
        ),
        # Financial Section
        rx.el.div(
            form_header("Ajustes Financieros", "calculator"),
            rx.el.div(
                input_group(
                    "Descuento Global ($)",
                    QuotationState.discount_global.to_string(),
                    "discount_global",
                    "number",
                ),
                input_group(
                    "Impuestos (%)",
                    QuotationState.tax_rate.to_string(),
                    "tax_rate",
                    "number",
                    placeholder="16",
                ),
                input_group(
                    "Costo de Envío ($)",
                    QuotationState.shipping_cost.to_string(),
                    "shipping_cost",
                    "number",
                ),
                class_name="grid grid-cols-3 gap-4 mb-6",
            ),
            class_name="bg-white p-6 rounded-2xl border border-gray-200 shadow-sm mb-6",
        ),
        # Additional Info Section
        rx.el.div(
            form_header("Información Adicional", "info"),
            rx.el.div(
                rx.el.label(
                    "Notas",
                    class_name="block text-xs font-medium text-gray-500 mb-1",
                ),
                rx.el.textarea(
                    on_change=lambda v: QuotationState.set_field("notes", v),
                    class_name="w-full px-3 py-2 bg-gray-50 border border-gray-200 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-purple-500/20 focus:border-purple-500",
                    default_value=QuotationState.notes,
                    placeholder="Notas adicionales para el cliente...",
                    rows=3,
                ),
                class_name="mb-4",
            ),
            rx.el.div(
                rx.el.label(
                    "Términos de Pago",
                    class_name="block text-xs font-medium text-gray-500 mb-1",
                ),
                rx.el.textarea(
                    on_change=lambda v: QuotationState.set_field("payment_terms", v),
                    class_name="w-full px-3 py-2 bg-gray-50 border border-gray-200 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-purple-500/20 focus:border-purple-500",
                    default_value=QuotationState.payment_terms,
                    placeholder="50% adelantado, 50% contra entrega...",
                    rows=2,
                ),
                class_name="mb-4",
            ),
            rx.el.div(
                rx.el.label(
                    "Términos y Condiciones",
                    class_name="block text-xs font-medium text-gray-500 mb-1",
                ),
                rx.el.textarea(
                    on_change=lambda v: QuotationState.set_field(
                        "terms_conditions", v
                    ),
                    class_name="w-full px-3 py-2 bg-gray-50 border border-gray-200 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-purple-500/20 focus:border-purple-500",
                    default_value=QuotationState.terms_conditions,
                    placeholder="Términos y condiciones generales...",
                    rows=2,
                ),
            ),
            class_name="bg-white p-6 rounded-2xl border border-gray-200 shadow-sm mb-6",
        ),
        class_name="space-y-6",
    )
