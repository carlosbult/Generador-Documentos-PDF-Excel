import reflex as rx
from app.states.warehouse_receipt_state import WarehouseReceiptState, PackageDimension


def preview_header() -> rx.Component:
    return rx.el.div(
        # Left side - Company info
        rx.el.div(
            rx.cond(
                WarehouseReceiptState.company_logo_url,
                rx.el.img(
                    src=WarehouseReceiptState.company_logo_url,
                    alt="Logo",
                    class_name="h-16 w-auto mb-3",
                ),
                rx.el.div(),
            ),
            rx.el.h2(
                WarehouseReceiptState.company_name,
                class_name="text-xl font-bold text-gray-900 mb-2",
            ),
            class_name="flex flex-col",
        ),
        # Right side - Receipt info
        rx.el.div(
            rx.el.h1(
                f"RECIBO DE ALMACÉN {WarehouseReceiptState.receipt_number}",
                class_name="text-3xl font-bold text-right text-gray-900 mb-3",
            ),
            rx.el.div(
                WarehouseReceiptState.warehouse_location,
                class_name="text-lg font-semibold text-right text-gray-700",
            ),
            class_name="flex flex-col items-end justify-center",
        ),
        class_name="flex justify-between items-start mb-8 pb-6 border-b-2 border-gray-200 gap-8",
    )


def summary_box() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                "Bultos",
                class_name="text-[10px] font-bold text-gray-500 uppercase mb-1",
            ),
            rx.el.div(
                WarehouseReceiptState.total_bultos.to_string(),
                class_name="text-base font-bold text-gray-900",
            ),
            class_name="p-3 bg-orange-50 rounded-lg border border-orange-200 text-center",
        ),
        rx.el.div(
            rx.el.div(
                "Peso Bruto",
                class_name="text-[10px] font-bold text-gray-500 uppercase mb-1",
            ),
            rx.el.div(
                rx.text(
                    WarehouseReceiptState.calculated_peso_bruto, format_string=",.2f"
                ),
                " pound(s)",
                class_name="text-base font-bold text-gray-900",
            ),
            class_name="p-3 bg-orange-50 rounded-lg border border-orange-200 text-center",
        ),
        rx.el.div(
            rx.el.div(
                "Volumen",
                class_name="text-[10px] font-bold text-gray-500 uppercase mb-1",
            ),
            rx.el.div(
                rx.text(WarehouseReceiptState.calculated_volumen, format_string=",.3f"),
                " cubic feet",
                class_name="text-base font-bold text-gray-900",
            ),
            class_name="p-3 bg-orange-50 rounded-lg border border-orange-200 text-center",
        ),
        rx.el.div(
            rx.el.div(
                "Peso Tasable",
                class_name="text-[10px] font-bold text-gray-500 uppercase mb-1",
            ),
            rx.el.div(
                rx.text(WarehouseReceiptState.peso_tasable, format_string=",.2f"),
                " pound(s)",
                class_name="text-base font-bold text-gray-900",
            ),
            class_name="p-3 bg-orange-50 rounded-lg border border-orange-200 text-center",
        ),
        class_name="grid grid-cols-4 gap-3 mb-4",
    )


def details_section() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    "Fecha:", class_name="text-xs font-bold text-gray-500 mb-1"
                ),
                rx.el.div(
                    WarehouseReceiptState.receipt_date,
                    class_name="text-sm text-gray-900",
                ),
                class_name="mb-3",
            ),
            rx.el.div(
                rx.el.div(
                    "Remitente:", class_name="text-xs font-bold text-gray-500 mb-1"
                ),
                rx.el.div(
                    WarehouseReceiptState.remitente,
                    class_name="text-sm text-gray-900",
                ),
                class_name="mb-3",
            ),
            rx.el.div(
                rx.el.div(
                    "Destinatario:", class_name="text-xs font-bold text-gray-500 mb-1"
                ),
                rx.el.div(
                    WarehouseReceiptState.destinatario,
                    class_name="text-sm text-gray-900",
                ),
                class_name="mb-3",
            ),
            rx.el.div(
                rx.el.div(
                    "Entregado por:", class_name="text-xs font-bold text-gray-500 mb-1"
                ),
                rx.el.div(
                    f"{WarehouseReceiptState.entregado_por} (Tracking: {WarehouseReceiptState.tracking_number})",
                    class_name="text-sm text-gray-900",
                ),
                class_name="mb-3",
            ),
            rx.el.div(
                rx.el.div(
                    "Descripción:", class_name="text-xs font-bold text-gray-500 mb-1"
                ),
                rx.el.div(
                    WarehouseReceiptState.descripcion,
                    class_name="text-sm text-gray-900",
                ),
            ),
            class_name="flex-1",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    "Oficina:", class_name="text-xs font-bold text-gray-500 mb-1"
                ),
                rx.el.div(
                    WarehouseReceiptState.oficina,
                    class_name="text-sm text-gray-900",
                ),
                class_name="mb-3",
            ),
            rx.el.div(
                rx.el.div(
                    "Referencia:", class_name="text-xs font-bold text-gray-500 mb-1"
                ),
                rx.el.div(
                    WarehouseReceiptState.referencia,
                    class_name="text-sm text-gray-900",
                ),
                class_name="mb-3",
            ),
            rx.el.div(
                rx.el.div(
                    "No. Pedido:", class_name="text-xs font-bold text-gray-500 mb-1"
                ),
                rx.el.div(
                    WarehouseReceiptState.no_pedido,
                    class_name="text-sm text-gray-900",
                ),
                class_name="mb-3",
            ),
            rx.el.div(
                rx.el.div(
                    "Factura:", class_name="text-xs font-bold text-gray-500 mb-1"
                ),
                rx.el.div(
                    WarehouseReceiptState.factura,
                    class_name="text-sm text-gray-900",
                ),
            ),
            class_name="flex-1",
        ),
        class_name="grid grid-cols-2 gap-6 p-4 bg-gray-50 rounded-lg border border-gray-200 mb-6",
    )


def action_buttons() -> rx.Component:
    return rx.el.div(
        rx.el.button(
            "INSTRUCCIONES",
            class_name="px-4 py-2 bg-gray-200 text-gray-700 text-xs font-bold rounded hover:bg-gray-300 transition-colors",
        ),
        rx.el.button(
            "RETENER",
            class_name="px-4 py-2 bg-gray-200 text-gray-700 text-xs font-bold rounded hover:bg-gray-300 transition-colors",
        ),
        rx.el.button(
            "ASOCIAR ARCHIVOS",
            class_name="px-4 py-2 bg-gray-200 text-gray-700 text-xs font-bold rounded hover:bg-gray-300 transition-colors",
        ),
        class_name="flex gap-3 mb-6",
    )


def dimension_table_row(dimension: PackageDimension) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            dimension.bultos.to_string(),
            class_name="py-2 px-3 text-xs text-gray-900 text-center border-b border-gray-100",
        ),
        rx.el.td(
            rx.cond(
                dimension.largo > 0,
                rx.text(dimension.largo, format_string=",.1f"),
                "X",
            ),
            class_name="py-2 px-3 text-xs text-gray-900 text-center border-b border-gray-100",
        ),
        rx.el.td(
            rx.cond(
                dimension.ancho > 0,
                rx.text(dimension.ancho, format_string=",.1f"),
                "X",
            ),
            class_name="py-2 px-3 text-xs text-gray-900 text-center border-b border-gray-100",
        ),
        rx.el.td(
            rx.cond(
                dimension.alto > 0, rx.text(dimension.alto, format_string=",.1f"), "X"
            ),
            class_name="py-2 px-3 text-xs text-gray-900 text-center border-b border-gray-100",
        ),
        rx.el.td(
            rx.text(dimension.pounds, format_string=",.1f"),
            " lbs",
            class_name="py-2 px-3 text-xs text-gray-900 text-center border-b border-gray-100",
        ),
        rx.el.td(
            rx.text(dimension.cubic_feet, format_string=",.3f"),
            class_name="py-2 px-3 text-xs text-gray-900 text-center border-b border-gray-100",
        ),
        rx.el.td(
            rx.cond(
                dimension.pt > 0,
                dimension.pt.to_string(),
                "",
            ),
            class_name="py-2 px-3 text-xs text-gray-900 text-center border-b border-gray-100",
        ),
        rx.el.td(
            dimension.referencia,
            class_name="py-2 px-3 text-xs text-gray-900 text-center border-b border-gray-100",
        ),
    )


def dimensions_table() -> rx.Component:
    return rx.el.div(
        rx.el.h3(
            "Dimensiones de Paquetes",
            class_name="text-sm font-bold text-gray-700 mb-2",
        ),
        rx.el.table(
            rx.el.thead(
                rx.el.tr(
                    rx.el.th(
                        "Bultos",
                        class_name="text-left text-xs font-bold text-gray-600 pb-2 px-3 border-b border-gray-300",
                    ),
                    rx.el.th(
                        "Largo",
                        class_name="text-center text-xs font-bold text-gray-600 pb-2 px-3 border-b border-gray-300",
                    ),
                    rx.el.th(
                        "Ancho",
                        class_name="text-center text-xs font-bold text-gray-600 pb-2 px-3 border-b border-gray-300",
                    ),
                    rx.el.th(
                        "Alto",
                        class_name="text-center text-xs font-bold text-gray-600 pb-2 px-3 border-b border-gray-300",
                    ),
                    rx.el.th(
                        "Pounds",
                        class_name="text-center text-xs font-bold text-gray-600 pb-2 px-3 border-b border-gray-300",
                    ),
                    rx.el.th(
                        "Cubic Feet",
                        class_name="text-center text-xs font-bold text-gray-600 pb-2 px-3 border-b border-gray-300",
                    ),
                    rx.el.th(
                        "PT",
                        class_name="text-center text-xs font-bold text-gray-600 pb-2 px-3 border-b border-gray-300",
                    ),
                    rx.el.th(
                        "Referencia",
                        class_name="text-center text-xs font-bold text-gray-600 pb-2 px-3 border-b border-gray-300",
                    ),
                )
            ),
            rx.el.tbody(
                rx.foreach(
                    WarehouseReceiptState.dimensions,
                    lambda dim: rx.fragment(dimension_table_row(dim), key=dim.id),
                )
            ),
            class_name="w-full border-collapse mb-6",
        ),
        class_name="bg-white rounded-lg border border-gray-200 p-4",
    )


def archive_section() -> rx.Component:
    return rx.el.div(
        rx.el.h3("Archivo", class_name="text-sm font-bold text-gray-700 mb-2"),
        rx.el.div(
            "No se han encontrado registros",
            class_name="text-xs text-gray-500 italic p-4 bg-gray-50 rounded border border-gray-200",
        ),
        class_name="mb-6",
    )


def legal_footer() -> rx.Component:
    return rx.el.div(
        rx.el.p(
            WarehouseReceiptState.legal_disclaimer,
            class_name="text-[8px] text-gray-500 leading-tight text-justify",
        ),
        class_name="mt-6 pt-4 border-t border-gray-200",
    )


def warehouse_receipt_preview() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            preview_header(),
            details_section(),
            # action_buttons(),  # Commented out as per user request
            # summary_box(),
            dimensions_table(),
            archive_section(),
            legal_footer(),
            class_name="bg-white p-8 shadow-lg min-h-[800px] w-full max-w-[816px] mx-auto border border-gray-200",
        ),
        class_name="bg-gray-500/10 p-8 rounded-2xl overflow-auto flex justify-center",
    )
