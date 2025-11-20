import reflex as rx
from app.components.navbar import navbar
from app.states.statement_state import StatementState
from app.components.statement.form import statement_form
from app.components.statement.preview import statement_preview


def action_bar() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1("Estado de Cuenta", class_name="text-2xl font-bold text-gray-900"),
            rx.el.p(
                "Edite los datos y genere el documento.",
                class_name="text-sm text-gray-500 mt-1",
            ),
        ),
        rx.el.div(
            rx.el.button(
                rx.icon("file-text", class_name="w-4 h-4"),
                "Exportar PDF",
                on_click=StatementState.export_pdf,
                disabled=StatementState.is_loading,
                class_name="flex items-center gap-2 px-4 py-2 bg-gray-900 text-white rounded-lg hover:bg-gray-800 transition-colors disabled:opacity-50 disabled:cursor-not-allowed text-sm font-medium shadow-sm",
            ),
            rx.el.button(
                rx.icon("table-2", class_name="w-4 h-4"),
                "Exportar Excel",
                on_click=StatementState.export_excel,
                disabled=StatementState.is_loading,
                class_name="flex items-center gap-2 px-4 py-2 bg-emerald-600 text-white rounded-lg hover:bg-emerald-700 transition-colors disabled:opacity-50 disabled:cursor-not-allowed text-sm font-medium shadow-sm",
            ),
            class_name="flex gap-3",
        ),
        class_name="flex flex-col md:flex-row md:items-center justify-between gap-4 mb-8 bg-white p-6 rounded-2xl border border-gray-200 shadow-sm",
    )


def statement_page() -> rx.Component:
    return rx.el.div(
        navbar(),
        rx.el.div(
            rx.el.div(
                action_bar(),
                rx.el.div(
                    rx.el.div(
                        statement_form(),
                        class_name="w-full lg:w-1/2 overflow-y-auto max-h-[calc(100vh-250px)] custom-scrollbar pr-2",
                    ),
                    rx.el.div(
                        statement_preview(), class_name="w-full lg:w-1/2 sticky top-8"
                    ),
                    class_name="flex flex-col lg:flex-row gap-8",
                ),
                class_name="max-w-[1600px] mx-auto px-4 py-8",
            ),
            class_name="min-h-screen bg-gray-50/50",
        ),
        class_name="font-['Inter']",
    )