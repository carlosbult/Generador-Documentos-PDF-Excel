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
            class_name="block text-xs font-medium text-gray-500 mb-1 uppercase tracking-wide",
        ),
        rx.el.input(
            on_change=lambda v: WarehouseReceiptState.set_field(field_name, v),
            type=type_,
            class_name="w-full px-3 py-2 bg-gray-50 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500/20 focus:border-orange-500 transition-all text-sm",
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
                "Bultos", class_name="text-xs font-medium text-gray-500 mb-1"
            ),
            rx.el.input(
                type="number",
                on_change=lambda v: WarehouseReceiptState.update_dimension(
                    index, "bultos", v
                ),
                class_name="w-full px-3 py-2 bg-gray-50 border border-gray-200 rounded-lg text-sm",
                default_value=dimension.bultos.to_string(),
            ),
        ),
        rx.el.div(
            rx.el.label("Largo", class_name="text-xs font-medium text-gray-500 mb-1"),
            rx.el.input(
                type="number",
                step="0.1",
                on_change=lambda v: WarehouseReceiptState.update_dimension(
                    index, "largo", v
                ),
                class_name="w-full px-3 py-2 bg-gray-50 border border-gray-200 rounded-lg text-sm",
                default_value=dimension.largo.to_string(),
            ),
        ),
        rx.el.div(
            rx.el.label("Ancho", class_name="text-xs font-medium text-gray-500 mb-1"),
            rx.el.input(
                type="number",
                step="0.1",
                on_change=lambda v: WarehouseReceiptState.update_dimension(
                    index, "ancho", v
                ),
                class_name="w-full px-3 py-2 bg-gray-50 border border-gray-200 rounded-lg text-sm",
                default_value=dimension.ancho.to_string(),
            ),
        ),
        rx.el.div(
            rx.el.label("Alto", class_name="text-xs font-medium text-gray-500 mb-1"),
            rx.el.input(
                type="number",
                step="0.1",
                on_change=lambda v: WarehouseReceiptState.update_dimension(
                    index, "alto", v
                ),
                class_name="w-full px-3 py-2 bg-gray-50 border border-gray-200 rounded-lg text-sm",
                default_value=dimension.alto.to_string(),
            ),
        ),
        rx.el.div(
            rx.el.label("Pounds", class_name="text-xs font-medium text-gray-500 mb-1"),
            rx.el.input(
                type="number",
                step="0.1",
                on_change=lambda v: WarehouseReceiptState.update_dimension(
                    index, "pounds", v
                ),
                class_name="w-full px-3 py-2 bg-gray-50 border border-gray-200 rounded-lg text-sm",
                default_value=dimension.pounds.to_string(),
            ),
        ),
        rx.el.div(
            rx.el.label(
                "Cubic Feet", class_name="text-xs font-medium text-gray-500 mb-1"
            ),
            rx.el.div(
                f"{dimension.cubic_feet:.3f}",
                class_name="px-3 py-2 bg-gray-100 border border-gray-200 rounded-lg text-sm text-right font-medium text-gray-700",
            ),
        ),
        rx.el.div(
            rx.el.label("PT", class_name="text-xs font-medium text-gray-500 mb-1"),
            rx.el.input(
                type="number",
                step="0.1",
                on_change=lambda v: WarehouseReceiptState.update_dimension(
                    index, "pt", v
                ),
                class_name="w-full px-3 py-2 bg-gray-50 border border-gray-200 rounded-lg text-sm",
                default_value=dimension.pt.to_string(),
            ),
        ),
        rx.el.div(
            rx.el.label(
                "Referencia", class_name="text-xs font-medium text-gray-500 mb-1"
            ),
            rx.el.input(
                on_change=lambda v: WarehouseReceiptState.update_dimension(
                    index, "referencia", v
                ),
                class_name="w-full px-3 py-2 bg-gray-50 border border-gray-200 rounded-lg text-sm",
                default_value=dimension.referencia,
            ),
        ),
        class_name="grid grid-cols-[auto_repeat(8,1fr)] gap-3 items-start p-4 bg-white border border-gray-100 rounded-xl shadow-sm hover:shadow-md transition-all",
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
                class_name="grid grid-cols-3 gap-4 mb-6",
            ),
            class_name="bg-white p-6 rounded-2xl border border-gray-200 shadow-sm mb-6",
        ),
        rx.el.div(
            # Summary section (read-only calculated fields)
            form_header("Resumen de Paquete", "package"),
            rx.el.div(
                rx.el.div(
                    rx.el.label(
                        "Total Bultos",
                        class_name="block text-xs font-medium text-gray-500 mb-1 uppercase tracking-wide",
                    ),
                    rx.el.div(
                        WarehouseReceiptState.total_bultos.to_string(),
                        class_name="px-3 py-2 bg-orange-50 border border-orange-200 rounded-lg text-sm font-bold text-orange-700",
                    ),
                ),
                rx.el.div(
                    rx.el.label(
                        "Peso Bruto (lbs)",
                        class_name="block text-xs font-medium text-gray-500 mb-1 uppercase tracking-wide",
                    ),
                    rx.el.div(
                        rx.text(
                            WarehouseReceiptState.calculated_peso_bruto,
                            format_string=",.2f",
                        ),
                        class_name="px-3 py-2 bg-orange-50 border border-orange-200 rounded-lg text-sm font-bold text-orange-700",
                    ),
                ),
                rx.el.div(
                    rx.el.label(
                        "Volumen (ft³)",
                        class_name="block text-xs font-medium text-gray-500 mb-1 uppercase tracking-wide",
                    ),
                    rx.el.div(
                        rx.text(
                            WarehouseReceiptState.calculated_volumen,
                            format_string=",.3f",
                        ),
                        class_name="px-3 py-2 bg-orange-50 border border-orange-200 rounded-lg text-sm font-bold text-orange-700",
                    ),
                ),
                input_group(
                    "Peso Tasable (lbs)",
                    WarehouseReceiptState.peso_tasable.to_string(),
                    "peso_tasable",
                    "number",
                ),
                class_name="grid grid-cols-4 gap-4 mb-6",
            ),
            class_name="bg-white p-6 rounded-2xl border border-gray-200 shadow-sm mb-6",
        ),
        rx.el.div(
            # Details section
            form_header("Detalles del Envío", "info"),
            rx.el.div(
                input_group("Oficina", WarehouseReceiptState.oficina, "oficina", placeholder="MIA/VLN"),
                input_group("Remitente", WarehouseReceiptState.remitente, "remitente", placeholder="NOSGLOBAL/MARCELO CONTRERAS"),
                input_group(
                    "Referencia", WarehouseReceiptState.referencia, "referencia", placeholder="REF-123"
                ),
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
                input_group(
                    "Tracking",
                    WarehouseReceiptState.tracking_number,
                    "tracking_number",
                    placeholder="TBA325639410316",
                ),
                input_group("Factura", WarehouseReceiptState.factura, "factura", placeholder="-0"),
                class_name="grid grid-cols-2 gap-4 mb-4",
            ),
            rx.el.div(
                input_group(
                    "Descripción", WarehouseReceiptState.descripcion, "descripcion", placeholder="1 CREMA"
                ),
                class_name="mb-6",
            ),
            class_name="bg-white p-6 rounded-2xl border border-gray-200 shadow-sm mb-6",
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
                class_name="flex items-center gap-2 px-4 py-2 bg-orange-600 text-white rounded-lg hover:bg-orange-700 transition-colors text-sm font-medium shadow-sm",
            ),
            class_name="bg-white p-6 rounded-2xl border border-gray-200 shadow-sm mb-6",
        ),
        class_name="space-y-6",
    )
