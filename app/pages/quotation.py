"""Quotation page."""

import reflex as rx
from app.components.navbar import navbar
from app.components.quotation.form import quotation_form
from app.components.quotation.preview import quotation_preview
from app.states.quotation_state import QuotationState


def action_bar() -> rx.Component:
    """Create the action bar with export buttons."""
    return rx.el.div(
        rx.el.div(
            rx.el.h1(
                "Cotización / Presupuesto", class_name="text-2xl font-bold text-gray-900"
            ),
            rx.el.p(
                "Edite los detalles y genere su cotización profesional.",
                class_name="text-sm text-gray-500 mt-1",
            ),
        ),
        rx.el.div(
            # Copy to Clipboard button
            rx.el.button(
                rx.icon("copy", class_name="w-4 h-4"),
                "Copiar al portapapeles",
                on_click=QuotationState.copy_to_clipboard,
                disabled=QuotationState.is_loading,
                class_name="flex items-center gap-2 px-4 py-2 bg-gray-600 text-white rounded-lg hover:bg-gray-700 transition-colors disabled:opacity-50 disabled:cursor-not-allowed text-sm font-medium shadow-sm",
            ),
            # PDF Export button
            rx.el.button(
                rx.icon("file-text", class_name="w-4 h-4"),
                "Exportar PDF",
                on_click=QuotationState.export_pdf,
                disabled=QuotationState.is_loading,
                class_name="flex items-center gap-2 px-4 py-2 bg-gray-900 text-white rounded-lg hover:bg-gray-800 transition-colors disabled:opacity-50 disabled:cursor-not-allowed text-sm font-medium shadow-sm",
            ),
            # Excel Export button
            rx.el.button(
                rx.icon("table-2", class_name="w-4 h-4"),
                "Exportar Excel",
                on_click=QuotationState.export_excel,
                disabled=QuotationState.is_loading,
                class_name="flex items-center gap-2 px-4 py-2 bg-purple-600 text-white rounded-lg hover:bg-purple-700 transition-colors disabled:opacity-50 disabled:cursor-not-allowed text-sm font-medium shadow-sm",
            ),
            class_name="flex gap-3",
        ),
        class_name="flex flex-col md:flex-row md:items-center justify-between gap-4 mb-8 bg-white p-6 rounded-2xl border border-gray-200 shadow-sm",
    )


def quotation_page() -> rx.Component:
    """Create the main quotation page."""
    return rx.el.div(
        navbar(),
        rx.el.div(
            rx.el.div(
                action_bar(),
                rx.el.div(
                    rx.el.div(
                        quotation_form(),
                        class_name="w-full lg:w-1/2 overflow-y-auto max-h-[calc(100vh-250px)] custom-scrollbar pr-2",
                    ),
                    rx.el.div(
                        quotation_preview(),
                        class_name="w-full lg:w-1/2 sticky top-8",
                    ),
                    class_name="flex flex-col lg:flex-row gap-8",
                ),
                class_name="max-w-[1600px] mx-auto px-4 py-8",
            ),
            class_name="min-h-screen bg-gray-50/50",
        ),
        class_name="font-['Inter']",
        on_mount=QuotationState.on_load,
    )
