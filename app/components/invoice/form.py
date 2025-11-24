import reflex as rx
from app.states.invoice_state import InvoiceState, InvoiceItem


def form_header(title: str, icon: str) -> rx.Component:
    return rx.el.div(
        rx.icon(icon, class_name="w-5 h-5 text-emerald-600"),
        rx.el.h3(title, class_name="text-lg font-semibold text-gray-800"),
        class_name="flex items-center gap-2 mb-4 pb-2 border-b border-gray-100",
    )


def input_group(
    label: str, value: str, field_name: str, type_: str = "text", placeholder: str = ""
) -> rx.Component:
    return rx.el.div(
        rx.el.label(
            label,
            class_name="block text-xs font-medium text-gray-500 mb-1 uppercase tracking-wide",
        ),
        rx.el.input(
            on_change=lambda v: InvoiceState.set_field(field_name, v),
            type=type_,
            class_name="w-full px-3 py-2 bg-gray-50 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-emerald-500/20 focus:border-emerald-500 transition-all text-sm",
            default_value=value,
            placeholder=placeholder,
        ),
    )


def item_row(item: InvoiceItem, index: int) -> rx.Component:
    return rx.el.div(
        rx.el.button(
            rx.icon("trash-2", class_name="w-4 h-4"),
            on_click=InvoiceState.remove_item(index),
            class_name="p-2 mt-6 text-red-400 hover:text-red-600 hover:bg-red-50 rounded-lg transition-colors",
        ),
        rx.el.div(
            rx.el.label(
                "Código", class_name="text-xs font-medium text-gray-500 mb-1"
            ),
            rx.el.input(
                on_change=lambda v: InvoiceState.update_item(index, "code", v),
                class_name="w-full px-3 py-2 bg-gray-50 border border-gray-200 rounded-lg text-sm",
                default_value=item.code,
                placeholder="SKU-001",
            ),
        ),
        rx.el.div(
            rx.el.label(
                "Descripción", class_name="text-xs font-medium text-gray-500 mb-1"
            ),
            rx.el.input(
                on_change=lambda v: InvoiceState.update_item(index, "description", v),
                class_name="w-full px-3 py-2 bg-gray-50 border border-gray-200 rounded-lg text-sm",
                default_value=item.description,
            ),
            class_name="col-span-2 md:col-span-2 lg:col-span-2 xl:col-span-3",
        ),
        rx.el.div(
            rx.el.label("Cant.", class_name="text-xs font-medium text-gray-500 mb-1"),
            rx.el.input(
                type="number",
                on_change=lambda v: InvoiceState.update_item(index, "quantity", v),
                class_name="w-full px-3 py-2 bg-gray-50 border border-gray-200 rounded-lg text-sm",
                default_value=item.quantity.to_string(),
            ),
        ),
        rx.el.div(
            rx.el.label("Precio", class_name="text-xs font-medium text-gray-500 mb-1"),
            rx.el.input(
                type="number",
                on_change=lambda v: InvoiceState.update_item(index, "unit_price", v),
                class_name="w-full px-3 py-2 bg-gray-50 border border-gray-200 rounded-lg text-sm",
                default_value=item.unit_price.to_string(),
            ),
        ),
        rx.el.div(
            rx.el.label("Desc.", class_name="text-xs font-medium text-gray-500 mb-1"),
            rx.el.input(
                type="number",
                on_change=lambda v: InvoiceState.update_item(index, "discount", v),
                class_name="w-full px-3 py-2 bg-gray-50 border border-gray-200 rounded-lg text-sm",
                default_value=item.discount.to_string(),
                step="0.01",
            ),
        ),
        rx.el.div(
            rx.el.label("Total", class_name="text-xs font-medium text-gray-500 mb-1"),
            rx.el.div(
                f"${item.amount:,.2f}",
                class_name="px-3 py-2 bg-gray-100 border border-gray-200 rounded-lg text-sm text-right font-medium text-gray-700",
            ),
        ),
        class_name="grid grid-cols-3 md:grid-cols-4 lg:grid-cols-5 xl:grid-cols-7 gap-3 items-start p-4 bg-white border border-gray-100 rounded-xl shadow-sm hover:shadow-md transition-all",
    )


def invoice_form() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            form_header("Datos del Emisor", "building-2"),
            rx.el.div(
                input_group("Nombre / Empresa", InvoiceState.from_name, "from_name"),
                input_group("Dirección", InvoiceState.from_address, "from_address"),
                input_group(
                    "Ciudad / Detalles", InvoiceState.from_details, "from_details"
                ),
                rx.el.div(
                    input_group(
                        "Email", InvoiceState.from_email, "from_email", "email"
                    ),
                    input_group(
                        "Teléfono", InvoiceState.from_phone, "from_phone", "tel"
                    ),
                    input_group(
                        "RIF/Cédula", InvoiceState.from_tax_id, "from_tax_id"
                    ),
                    input_group(
                        "Logo URL", InvoiceState.logo_url, "logo_url"
                    ),
                    class_name="grid grid-cols-2 gap-4",
                ),
                class_name="grid grid-cols-1 gap-4",
            ),
            class_name="bg-white p-6 rounded-2xl shadow-sm border border-gray-200",
        ),
        rx.el.div(
            form_header("Datos del Cliente", "user"),
            rx.el.div(
                input_group("Nombre Contacto", InvoiceState.to_name, "to_name", placeholder="Cliente Ejemplo"),
                input_group("Empresa", InvoiceState.to_company, "to_company", placeholder="Empresa Cliente Ltda."),
                input_group("Dirección", InvoiceState.to_address, "to_address", placeholder="Av. Comercial 456"),
                input_group(
                    "Detalles Ubicación", InvoiceState.to_details, "to_details", placeholder="Caracas, Venezuela"
                ),
                input_group(
                    "RIF/Cédula", InvoiceState.to_tax_id, "to_tax_id", placeholder="V-987654321"
                ),
                class_name="grid grid-cols-1 md:grid-cols-2 gap-4",
            ),
            class_name="bg-white p-6 rounded-2xl shadow-sm border border-gray-200",
        ),
        rx.el.div(
            form_header("Detalles de Nota de entrega", "file-text"),
            rx.el.div(
                input_group(
                    "Número Nota de entrega", InvoiceState.invoice_number, "invoice_number", placeholder="INV-NOS-2024-001"
                ),
                input_group(
                    "Impuesto %",
                    InvoiceState.tax_rate.to_string(),
                    "tax_rate",
                    "number",
                    placeholder="16.0",
                ),
                input_group(
                    "Fecha Emisión", InvoiceState.invoice_date, "invoice_date", "date"
                ),
                input_group(
                    "Fecha Vencimiento", InvoiceState.due_date, "due_date", "date"
                ),
                class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4",
            ),
            class_name="bg-white p-6 rounded-2xl shadow-sm border border-gray-200",
        ),
        rx.el.div(
            form_header("Información de Pago", "credit-card"),
            rx.el.div(
                input_group(
                    "Método de Pago", InvoiceState.payment_method, "payment_method", placeholder="Transferencia Bancaria"
                ),
                input_group(
                    "Nombre del Banco", InvoiceState.bank_name, "bank_name", placeholder="Banco Provincial"
                ),
                input_group(
                    "Cuenta Bancaria", InvoiceState.bank_account, "bank_account", placeholder="0102-0000-0000-0000-1234"
                ),
                class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4",
            ),
            class_name="bg-white p-6 rounded-2xl shadow-sm border border-gray-200",
        ),
        rx.el.div(
            form_header("Términos y Condiciones", "file-text"),
            rx.el.div(
                rx.el.label(
                    "Términos y Condiciones",
                    class_name="block text-xs font-medium text-gray-500 mb-1 uppercase tracking-wide",
                ),
                rx.el.textarea(
                    on_change=lambda v: InvoiceState.set_field("terms_conditions", v),
                    class_name="w-full px-3 py-2 bg-gray-50 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-emerald-500/20 focus:border-emerald-500 transition-all text-sm h-24 resize-none",
                    default_value=InvoiceState.terms_conditions,
                    placeholder="Pago contra entrega. Validez 30 días. Los precios están expresados en bolívares.",
                ),
                class_name="mb-4",
            ),
            rx.el.div(
                rx.el.label(
                    "Notas Adicionales",
                    class_name="block text-xs font-medium text-gray-500 mb-1 uppercase tracking-wide",
                ),
                rx.el.textarea(
                    on_change=lambda v: InvoiceState.set_field("notes", v),
                    class_name="w-full px-3 py-2 bg-gray-50 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-emerald-500/20 focus:border-emerald-500 transition-all text-sm h-20 resize-none",
                    default_value=InvoiceState.notes,
                    placeholder="Notas adicionales...",
                ),
                class_name="mb-4",
            ),
            input_group(
                "Autorizado por", InvoiceState.authorized_by, "authorized_by", placeholder="Juan Pérez - Gerente"
            ),
            class_name="space-y-4",
        ),
        rx.el.div(
            rx.el.div(
                form_header("Items de Nota de entrega", "shopping-cart"),
                rx.el.button(
                    rx.icon("plus", class_name="w-4 h-4"),
                    rx.el.span("Agregar Item"),
                    on_click=InvoiceState.add_item,
                    class_name="flex items-center gap-2 px-3 py-1.5 bg-emerald-50 text-emerald-600 rounded-lg text-sm font-medium hover:bg-emerald-100 transition-colors",
                ),
                class_name="flex justify-between items-center mb-4",
            ),
            rx.el.div(
                rx.foreach(
                    InvoiceState.items,
                    lambda item, idx: rx.box(
                        item_row(item, idx),
                        key=item.id,
                    ),
                ),
                class_name="space-y-3",
            ),
            class_name="bg-white p-6 rounded-2xl shadow-sm border border-gray-200",
        ),
        class_name="space-y-6",
    )