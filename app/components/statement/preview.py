import reflex as rx
from app.states.statement_state import StatementState, Transaction


def preview_header() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h2(
                StatementState.provider_name,
                class_name="font-bold text-gray-900 uppercase",
            ),
            rx.el.p(
                StatementState.provider_address,
                class_name="text-gray-600 text-xs uppercase",
            ),
            rx.el.p(
                StatementState.provider_city_state_zip,
                class_name="text-gray-600 text-xs uppercase",
            ),
            rx.el.p(
                f"Tel : {StatementState.provider_phone}",
                class_name="text-gray-600 text-xs",
            ),
        ),
        rx.el.div(
            rx.el.h1(
                "ESTADO DE CUENTA",
                class_name="text-xl font-bold text-right text-gray-900 mb-4",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        "NÚMERO DE CUENTA",
                        class_name="text-[10px] font-bold bg-gray-200 p-1 border-b border-white",
                    ),
                    rx.el.div(
                        StatementState.account_number,
                        class_name="text-[10px] p-1 border-b border-gray-200",
                    ),
                    class_name="grid grid-cols-2",
                ),
                rx.el.div(
                    rx.el.div(
                        "TÉRMINOS",
                        class_name="text-[10px] font-bold bg-gray-200 p-1 border-b border-white",
                    ),
                    rx.el.div(
                        StatementState.terms,
                        class_name="text-[10px] p-1 border-b border-gray-200",
                    ),
                    class_name="grid grid-cols-2",
                ),
                rx.el.div(
                    rx.el.div(
                        "FECHA ESTADO",
                        class_name="text-[10px] font-bold bg-gray-200 p-1",
                    ),
                    rx.el.div(
                        StatementState.statement_date, class_name="text-[10px] p-1"
                    ),
                    class_name="grid grid-cols-2",
                ),
                class_name="border border-gray-300",
            ),
            class_name="flex flex-col items-end",
        ),
        class_name="flex justify-between items-start mb-8",
    )


def client_section() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.p(
                StatementState.client_name, class_name="font-bold text-sm uppercase"
            ),
            rx.el.p(StatementState.client_address, class_name="text-xs uppercase"),
            rx.el.p(
                f"{StatementState.client_city} {StatementState.client_state}",
                class_name="text-xs uppercase",
            ),
            rx.el.p(StatementState.client_country, class_name="text-xs uppercase"),
            class_name="p-4 border border-gray-200 rounded w-1/2",
        ),
        class_name="mb-8",
    )


def transaction_table_header() -> rx.Component:
    return rx.el.tr(
        rx.el.th(
            "FECHA",
            class_name="p-2 text-left text-[10px] font-bold text-gray-800 border-b border-gray-300",
        ),
        rx.el.th(
            "NOTA DE ENTREGA",
            class_name="p-2 text-left text-[10px] font-bold text-gray-800 border-b border-gray-300",
        ),
        rx.el.th(
            "CUENTA",
            class_name="p-2 text-left text-[10px] font-bold text-gray-800 border-b border-gray-300",
        ),
        rx.el.th(
            "DESCRIPCIÓN",
            class_name="p-2 text-left text-[10px] font-bold text-gray-800 border-b border-gray-300 w-1/3",
        ),
        rx.el.th(
            "CANTIDAD",
            class_name="p-2 text-right text-[10px] font-bold text-gray-800 border-b border-gray-300",
        ),
        rx.el.th(
            "PAGADO",
            class_name="p-2 text-right text-[10px] font-bold text-gray-800 border-b border-gray-300",
        ),
        rx.el.th(
            "DEBIDO",
            class_name="p-2 text-right text-[10px] font-bold text-gray-800 border-b border-gray-300",
        ),
    )


def transaction_table_row(transaction: Transaction) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            transaction.date,
            class_name="p-2 text-[10px] text-gray-600 border-b border-gray-100",
        ),
        rx.el.td(
            transaction.invoice_no,
            class_name="p-2 text-[10px] text-gray-600 border-b border-gray-100",
        ),
        rx.el.td(
            transaction.reference,
            class_name="p-2 text-[10px] text-gray-600 border-b border-gray-100",
        ),
        rx.el.td(
            transaction.description,
            class_name="p-2 text-[10px] text-gray-600 border-b border-gray-100",
        ),
        rx.el.td(
            f"{transaction.amount:.2f}",
            class_name="p-2 text-right text-[10px] text-gray-600 border-b border-gray-100",
        ),
        rx.el.td(
            f"{transaction.paid:.2f}",
            class_name="p-2 text-right text-[10px] text-gray-600 border-b border-gray-100",
        ),
        rx.el.td(
            f"{transaction.amount - transaction.paid:.2f}",
            class_name="p-2 text-right text-[10px] text-gray-600 border-b border-gray-100",
        ),
    )


def aging_table() -> rx.Component:
    return rx.el.div(
        rx.el.table(
            rx.el.thead(
                rx.el.tr(
                    rx.el.th(
                        "CURRENCY",
                        class_name="p-2 text-left text-[10px] font-bold bg-gray-100 border border-gray-300",
                    ),
                    rx.el.th(
                        "-30",
                        class_name="p-2 text-right text-[10px] font-bold bg-gray-100 border border-gray-300",
                    ),
                    rx.el.th(
                        "+30",
                        class_name="p-2 text-right text-[10px] font-bold bg-gray-100 border border-gray-300",
                    ),
                    rx.el.th(
                        "+60",
                        class_name="p-2 text-right text-[10px] font-bold bg-gray-100 border border-gray-300",
                    ),
                    rx.el.th(
                        "+90",
                        class_name="p-2 text-right text-[10px] font-bold bg-gray-100 border border-gray-300",
                    ),
                )
            ),
            rx.el.tbody(
                rx.el.tr(
                    rx.el.td(
                        "USD",
                        class_name="p-2 text-left text-[10px] font-bold border border-gray-300",
                    ),
                    rx.el.td(
                        rx.text(
                            StatementState.aging_buckets["current"],
                            format_string=",.2f",
                        ),
                        class_name="p-2 text-right text-[10px] border border-gray-300",
                    ),
                    rx.el.td(
                        rx.text(
                            StatementState.aging_buckets["30"], format_string=",.2f"
                        ),
                        class_name="p-2 text-right text-[10px] border border-gray-300",
                    ),
                    rx.el.td(
                        rx.text(
                            StatementState.aging_buckets["60"], format_string=",.2f"
                        ),
                        class_name="p-2 text-right text-[10px] border border-gray-300",
                    ),
                    rx.el.td(
                        rx.text(
                            StatementState.aging_buckets["90"], format_string=",.2f"
                        ),
                        class_name="p-2 text-right text-[10px] border border-gray-300",
                    ),
                )
            ),
            class_name="w-full border-collapse mb-4",
        ),
        rx.el.div(
            rx.el.span("TOTAL DEBIDO USD...", class_name="font-bold text-xs mr-2"),
            rx.el.span(
                rx.text(StatementState.total_due, format_string=",.2f"),
                class_name="font-bold text-sm",
            ),
            class_name="flex justify-end items-center border-t-2 border-black pt-2",
        ),
        class_name="mt-8 w-full",
    )


def statement_preview() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            preview_header(),
            client_section(),
            rx.el.div(
                f"A CONTINUACION LE MOSTRAMOS UNA LISTA DE NOTAS DE ENTREGA PENDIENTES DE PAGO A {StatementState.statement_date}",
                class_name="text-xs font-bold mb-4",
            ),
            rx.el.table(
                rx.el.thead(transaction_table_header()),
                rx.el.tbody(
                    rx.foreach(StatementState.transactions, transaction_table_row)
                ),
                class_name="w-full border-collapse mb-6",
            ),
            aging_table(),
            class_name="bg-white p-8 shadow-lg min-h-[800px] w-full max-w-[816px] mx-auto border border-gray-200",
        ),
        class_name="bg-gray-500/10 p-8 rounded-2xl overflow-auto flex justify-center",
    )