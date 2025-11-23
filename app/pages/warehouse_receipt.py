import reflex as rx
from app.components.navbar import navbar
from app.states.warehouse_receipt_state import WarehouseReceiptState
from app.components.warehouse_receipt.form import warehouse_receipt_form
from app.components.warehouse_receipt.preview import warehouse_receipt_preview


def action_bar() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1(
                "Recibo de Almacén", class_name="text-2xl font-bold text-gray-900"
            ),
            rx.el.p(
                "Edite los detalles y genere su recibo de almacén.",
                class_name="text-sm text-gray-500 mt-1",
            ),
        ),
        rx.el.div(
            rx.el.button(
                rx.icon("file-text", class_name="w-4 h-4"),
                "Exportar PDF",
                on_click=WarehouseReceiptState.export_pdf,
                disabled=WarehouseReceiptState.is_loading,
                class_name="flex items-center gap-2 px-4 py-2 bg-gray-900 text-white rounded-lg hover:bg-gray-800 transition-colors disabled:opacity-50 disabled:cursor-not-allowed text-sm font-medium shadow-sm",
            ),
            rx.el.button(
                rx.icon("table-2", class_name="w-4 h-4"),
                "Exportar Excel",
                on_click=WarehouseReceiptState.export_excel,
                disabled=WarehouseReceiptState.is_loading,
                class_name="flex items-center gap-2 px-4 py-2 bg-orange-600 text-white rounded-lg hover:bg-orange-700 transition-colors disabled:opacity-50 disabled:cursor-not-allowed text-sm font-medium shadow-sm",
            ),
            class_name="flex gap-3",
        ),
        class_name="flex flex-col md:flex-row md:items-center justify-between gap-4 mb-8 bg-white p-6 rounded-2xl border border-gray-200 shadow-sm",
    )


def warehouse_receipt_page() -> rx.Component:
    return rx.el.div(
        navbar(),
        rx.el.div(
            rx.el.div(
                action_bar(),
                rx.el.div(
                    rx.el.div(
                        warehouse_receipt_form(),
                        class_name="w-full lg:w-1/2 overflow-y-auto max-h-[calc(100vh-250px)] custom-scrollbar pr-2",
                    ),
                    rx.el.div(
                        warehouse_receipt_preview(),
                        class_name="w-full lg:w-1/2 sticky top-8",
                    ),
                    class_name="flex flex-col lg:flex-row gap-8",
                ),
                class_name="max-w-[1600px] mx-auto px-4 py-8",
            ),
            class_name="min-h-screen bg-gray-50/50",
        ),
        class_name="font-['Inter']",
        on_mount=WarehouseReceiptState.on_load,
    )
