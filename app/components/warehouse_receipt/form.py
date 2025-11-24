import reflex as rx
from app.states.warehouse_receipt_state import WarehouseReceiptState, PackageDimension


def form_header(title: str, icon: str) -> rx.Component:
    return rx.el.div(
        rx.icon(icon, class_name="w-5 h-5 text-orange-600"),
        rx.el.h3(title, class_name="text-lg font-semibold text-gray-800"),
        class_name="flex items-center gap-2 mb-4 pb-2 border-b border-gray-100",
    )


def input_group(
    label: str, value: str, field_name: str, type_: str = "text", placeholder: str = ""
) -> rx.Component:
    return rx.el.div(
        rx.el.label(
            label,
            class_name="block text-xs font-medium text-gray-600 mb-1.5 uppercase tracking-wide font-semibold",
        ),
        rx.el.input(
            on_change=lambda v: WarehouseReceiptState.set_field(field_name, v),
            type=type_,
            class_name="w-full px-4 py-3 bg-white border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-orange-500 focus:border-orange-500 transition-all duration-200 text-sm placeholder-gray-400 shadow-sm hover:shadow-md hover:border-gray-400",
            default_value=value,
            placeholder=placeholder,
        ),
    )


def dimension_row(dimension: PackageDimension, index: int) -> rx.Component:
    return rx.el.div(
        rx.el.button(
            rx.icon("trash-2", class_name="w-4 h-4"),
            on_click=WarehouseReceiptState.remove_dimension(index),
            class_name="p-2 mt-6 text-red-400 hover:text-red-600 hover:bg-red-50 rounded-lg transition-colors",
        ),
        rx.el.div(
            rx.el.label(
                "Bultos", class_name="text-xs font-medium text-gray-600 mb-1.5 font-semibold"
            ),
            rx.el.input(
                type="number",
                on_change=lambda v: WarehouseReceiptState.update_dimension(
                    index, "bultos", v
                ),
                class_name="w-full px-3 py-2.5 bg-white border border-gray-300 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-orange-500 focus:border-orange-500 transition-all shadow-sm hover:shadow-md",
                default_value=dimension.bultos.to_string(),
            ),
        ),
        rx.el.div(
            rx.el.label("Largo", class_name="text-xs font-medium text-gray-600 mb-1.5 font-semibold"),
            rx.el.input(
                type="number",
                step="0.1",
                on_change=lambda v: WarehouseReceiptState.update_dimension(
                    index, "largo", v
                ),
                class_name="w-full px-3 py-2.5 bg-white border border-gray-300 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-orange-500 focus:border-orange-500 transition-all shadow-sm hover:shadow-md",
                default_value=dimension.largo.to_string(),
            ),
        ),
        rx.el.div(
            rx.el.label("Ancho", class_name="text-xs font-medium text-gray-600 mb-1.5 font-semibold"),
            rx.el.input(
                type="number",
                step="0.1",
                on_change=lambda v: WarehouseReceiptState.update_dimension(
                    index, "ancho", v
                ),
                class_name="w-full px-3 py-2.5 bg-white border border-gray-300 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-orange-500 focus:border-orange-500 transition-all shadow-sm hover:shadow-md",
                default_value=dimension.ancho.to_string(),
            ),
        ),
        rx.el.div(
            rx.el.label("Alto", class_name="text-xs font-medium text-gray-600 mb-1.5 font-semibold"),
            rx.el.input(
                type="number",
                step="0.1",
                on_change=lambda v: WarehouseReceiptState.update_dimension(
                    index, "alto", v
                ),
                class_name="w-full px-3 py-2.5 bg-white border border-gray-300 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-orange-500 focus:border-orange-500 transition-all shadow-sm hover:shadow-md",
                default_value=dimension.alto.to_string(),
            ),
        ),
        rx.el.div(
            rx.el.label("Pounds", class_name="text-xs font-medium text-gray-600 mb-1.5 font-semibold"),
            rx.el.input(
                type="number",
                step="0.1",
                on_change=lambda v: WarehouseReceiptState.update_dimension(
                    index, "pounds", v
                ),
                class_name="w-full px-3 py-2.5 bg-white border border-gray-300 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-orange-500 focus:border-orange-500 transition-all shadow-sm hover:shadow-md",
                default_value=dimension.pounds.to_string(),
            ),
        ),
        rx.el.div(
            rx.el.label(
                "Cubic Feet", class_name="text-xs font-medium text-gray-600 mb-1.5 font-semibold"
            ),
            rx.el.div(
                f"{dimension.cubic_feet:.3f}",
                class_name="px-3 py-2.5 bg-gray-50 border border-gray-300 rounded-lg text-sm text-right font-semibold text-gray-700",
            ),
        ),
        rx.el.div(
            rx.el.label("PT", class_name="text-xs font-medium text-gray-600 mb-1.5 font-semibold"),
            rx.el.input(
                type="number",
                step="0.1",
                on_change=lambda v: WarehouseReceiptState.update_dimension(
                    index, "pt", v
                ),
                class_name="w-full px-3 py-2.5 bg-white border border-gray-300 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-orange-500 focus:border-orange-500 transition-all shadow-sm hover:shadow-md",
                default_value=dimension.pt.to_string(),
            ),
        ),
        rx.el.div(
            rx.el.label(
                "Referencia", class_name="text-xs font-medium text-gray-600 mb-1.5 font-semibold"
            ),
            rx.el.input(
                on_change=lambda v: WarehouseReceiptState.update_dimension(
                    index, "referencia", v
                ),
                class_name="w-full px-3 py-2.5 bg-white border border-gray-300 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-orange-500 focus:border-orange-500 transition-all shadow-sm hover:shadow-md",
                default_value=dimension.referencia,
            ),
        ),
        class_name="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-4 items-start p-6 bg-white border border-gray-200 rounded-xl shadow-sm hover:shadow-lg transition-all duration-200",
    )


def warehouse_receipt_form() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            # Header section
            form_header("Información del Recibo", "file-text"),
            rx.el.div(
                input_group(
                    "Número de Recibo",
                    WarehouseReceiptState.receipt_number,
                    "receipt_number",
                    placeholder="225137",
                ),
                input_group(
                    "Ubicación",
                    WarehouseReceiptState.warehouse_location,
                    "warehouse_location",
                    placeholder="MIA",
                ),
                input_group(
                    "Fecha", WarehouseReceiptState.receipt_date, "receipt_date", "date"
                ),
                class_name="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8",
            ),
            class_name="bg-white p-8 rounded-2xl border border-gray-200 shadow-lg mb-8 hover:shadow-xl transition-shadow duration-200",
        ),
        rx.el.div(
            # Details section
            form_header("Detalles del Envío", "info"),
            rx.el.div(
                rx.el.div(
                    input_group("Oficina", WarehouseReceiptState.oficina, "oficina", placeholder="MIA/VLN"),
                    input_group("Remitente", WarehouseReceiptState.remitente, "remitente", placeholder="NOSGLOBAL/MARCELO CONTRERAS"),
                    input_group(
                        "Referencia", WarehouseReceiptState.referencia, "referencia", placeholder="REF-123"
                    ),
                    class_name="grid grid-cols-1 md:grid-cols-3 gap-6 mb-6"
                ),
                rx.el.div(
                    input_group(
                        "Destinatario",
                        WarehouseReceiptState.destinatario,
                        "destinatario",
                        placeholder="NOSGLOBAL/MARCELO CONTRERAS",
                    ),
                    input_group(
                        "No. Pedido", WarehouseReceiptState.no_pedido, "no_pedido", placeholder="PO-456"
                    ),
                    input_group(
                        "Entregado por",
                        WarehouseReceiptState.entregado_por,
                        "entregado_por",
                        placeholder="AMAZON",
                    ),
                    class_name="grid grid-cols-1 md:grid-cols-3 gap-6 mb-6"
                ),
                rx.el.div(
                    input_group(
                        "Tracking",
                        WarehouseReceiptState.tracking_number,
                        "tracking_number",
                        placeholder="TBA325639410316",
                    ),
                    input_group("Factura", WarehouseReceiptState.factura, "factura", placeholder="-0"),
                    class_name="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6"
                ),
                rx.el.div(
                    input_group(
                        "Descripción", WarehouseReceiptState.descripcion, "descripcion", placeholder="1 CREMA"
                    ),
                    class_name="mb-8",
                ),
            ),
            class_name="bg-white p-8 rounded-2xl border border-gray-200 shadow-lg mb-8 hover:shadow-xl transition-shadow duration-200",
        ),
        rx.el.div(
            # Dimensions table section
            form_header("Dimensiones de Paquetes", "box"),
            rx.el.div(
                rx.foreach(
                    WarehouseReceiptState.dimensions,
                    lambda dim, idx: dimension_row(dim, idx),
                ),
                class_name="space-y-3 mb-4",
            ),
            rx.el.button(
                rx.icon("plus", class_name="w-4 h-4"),
                "Agregar Dimensión",
                on_click=WarehouseReceiptState.add_dimension,
                class_name="flex items-center gap-2 px-6 py-3 bg-gradient-to-r from-orange-600 to-orange-700 text-white rounded-xl hover:from-orange-700 hover:to-orange-800 transition-all duration-200 text-sm font-semibold shadow-md hover:shadow-lg transform hover:scale-105",
            ),
            class_name="bg-white p-8 rounded-2xl border border-gray-200 shadow-lg mb-8 hover:shadow-xl transition-shadow duration-200",
        ),
        class_name="space-y-8 max-w-7xl mx-auto",
    )
