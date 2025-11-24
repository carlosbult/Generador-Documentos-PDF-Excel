import reflex as rx
from app.states.statement_state import StatementState, Transaction


def form_section_header(title: str, icon: str) -> rx.Component:
    return rx.el.div(
        rx.icon(icon, class_name="w-5 h-5 text-blue-600"),
        rx.el.h3(title, class_name="text-lg font-semibold text-gray-800"),
        class_name="flex items-center gap-2 mb-4 pb-2 border-b border-gray-100",
    )


def input_field(
    label: str,
    value: str,
    on_change: rx.event.EventType,
    type_: str = "text",
    placeholder: str = "",
) -> rx.Component:
    return rx.el.div(
        rx.el.label(
            label,
            class_name="block text-xs font-medium text-gray-500 mb-1 uppercase tracking-wide",
        ),
        rx.el.input(
            on_change=on_change,
            type=type_,
            placeholder=placeholder,
            class_name="w-full px-3 py-2 bg-gray-50 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 transition-all text-sm",
            default_value=value,
        ),
        class_name="flex-1",
    )


def transaction_row(transaction: Transaction, index: int) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.button(
                rx.icon("trash-2", class_name="w-4 h-4"),
                on_click=StatementState.remove_transaction(index),
                class_name="p-2 text-red-400 hover:text-red-600 hover:bg-red-50 rounded-lg transition-colors",
                title="Eliminar fila",
            ),
            class_name="flex items-center justify-center mt-6",
        ),
        rx.el.div(
            input_field(
                "Fecha",
                transaction.date,
                lambda v: StatementState.update_transaction(index, "date", v),
                type_="date",
            ),
            input_field(
                "Nota de entrega #",
                transaction.invoice_no,
                lambda v: StatementState.update_transaction(index, "invoice_no", v),
                placeholder="146038",
            ),
            class_name="grid grid-cols-2 gap-2 col-span-2 md:col-span-2 lg:col-span-2",
        ),
        rx.el.div(
            input_field(
                "Descripción",
                transaction.description,
                lambda v: StatementState.update_transaction(index, "description", v),
                placeholder="WHS: 224033, BULTOS: 1, DESTINATARIO: NOSGLOBAL",
            ),
            class_name="col-span-3 md:col-span-3 lg:col-span-3",
        ),
        rx.el.div(
            input_field(
                "Monto",
                transaction.amount.to_string(),
                lambda v: StatementState.update_transaction(index, "amount", v),
                type_="number",
                placeholder="154.00",
            ),
            input_field(
                "Pagado",
                transaction.paid.to_string(),
                lambda v: StatementState.update_transaction(index, "paid", v),
                type_="number",
                placeholder="0.00",
            ),
            class_name="grid grid-cols-2 gap-2 col-span-3 md:col-span-3 lg:col-span-2",
        ),
        class_name="grid grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-4 p-4 bg-white border border-gray-100 rounded-xl shadow-sm hover:shadow-md transition-shadow items-start",
    )


def statement_form() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            form_section_header("Datos del Proveedor", "building-2"),
            rx.el.div(
                input_field(
                    "Nombre Empresa",
                    StatementState.provider_name,
                    lambda v: StatementState.set_field("provider_name", v),
                ),
                input_field(
                    "Dirección",
                    StatementState.provider_address,
                    lambda v: StatementState.set_field("provider_address", v),
                ),
                input_field(
                    "Ciudad/Estado/Zip",
                    StatementState.provider_city_state_zip,
                    lambda v: StatementState.set_field("provider_city_state_zip", v),
                ),
                input_field(
                    "Teléfono",
                    StatementState.provider_phone,
                    lambda v: StatementState.set_field("provider_phone", v),
                ),
                class_name="grid grid-cols-1 md:grid-cols-2 gap-4",
            ),
            class_name="bg-white p-6 rounded-2xl shadow-sm border border-gray-200 mb-6",
        ),
        rx.el.div(
            form_section_header("Datos del Cliente", "users"),
            rx.el.div(
                input_field(
                    "Nombre Cliente",
                    StatementState.client_name,
                    lambda v: StatementState.set_field("client_name", v),
                    placeholder="Cliente Ejemplo",
                ),
                input_field(
                    "Dirección",
                    StatementState.client_address,
                    lambda v: StatementState.set_field("client_address", v),
                    placeholder="Av. Comercial 456, Edificio Central",
                ),
                class_name="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4",
            ),
            rx.el.div(
                input_field(
                    "Ciudad",
                    StatementState.client_city,
                    lambda v: StatementState.set_field("client_city", v),
                    placeholder="Caracas",
                ),
                input_field(
                    "Estado",
                    StatementState.client_state,
                    lambda v: StatementState.set_field("client_state", v),
                    placeholder="Distrito Capital",
                ),
                input_field(
                    "País",
                    StatementState.client_country,
                    lambda v: StatementState.set_field("client_country", v),
                    placeholder="Venezuela",
                ),
                class_name="grid grid-cols-1 md:grid-cols-3 gap-4",
            ),
            class_name="bg-white p-6 rounded-2xl shadow-sm border border-gray-200 mb-6",
        ),
        rx.el.div(
            form_section_header("Detalles del Estado", "file-text"),
            rx.el.div(
                input_field(
                    "Número de Cuenta",
                    StatementState.account_number,
                    lambda v: StatementState.set_field("account_number", v),
                    placeholder="34829",
                ),
                input_field(
                    "Términos",
                    StatementState.terms,
                    lambda v: StatementState.set_field("terms", v),
                    placeholder="CONTADO",
                ),
                input_field(
                    "Fecha del Estado",
                    StatementState.statement_date,
                    lambda v: StatementState.set_field("statement_date", v),
                    type_="date",
                ),
                class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4",
            ),
            class_name="bg-white p-6 rounded-2xl shadow-sm border border-gray-200 mb-6",
        ),
        rx.el.div(
            rx.el.div(
                form_section_header("Transacciones", "list"),
                rx.el.button(
                    rx.el.span("Agregar Fila"),
                    rx.icon("plus", class_name="w-4 h-4"),
                    on_click=StatementState.add_transaction,
                    class_name="flex items-center gap-2 px-3 py-1.5 bg-blue-50 text-blue-600 rounded-lg text-sm font-medium hover:bg-blue-100 transition-colors",
                ),
                class_name="flex items-center justify-between mb-4",
            ),
            rx.el.div(
                rx.foreach(
                    StatementState.transactions,
                    lambda t, i: rx.box(
                        transaction_row(t, i),
                        key=t.id,
                    ),
                ),
                class_name="space-y-3",
            ),
            class_name="bg-white p-6 rounded-2xl shadow-sm border border-gray-200",
        ),
        class_name="space-y-6",
    )