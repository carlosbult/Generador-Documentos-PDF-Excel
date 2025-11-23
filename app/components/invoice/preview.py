import reflex as rx
from app.states.invoice_state import InvoiceState, InvoiceItem


def preview_item_row(item: InvoiceItem) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            rx.cond(
                item.code,
                f"{item.code} - {item.description}",
                item.description,
            ),
            class_name="py-4 text-sm text-gray-900 font-medium border-b border-gray-100",
        ),
        rx.el.td(
            item.quantity.to_string(),
            class_name="py-4 text-sm text-gray-600 text-right border-b border-gray-100",
        ),
        rx.el.td(
            f"${item.unit_price:.2f}",
            class_name="py-4 text-sm text-gray-600 text-right border-b border-gray-100",
        ),
        rx.el.td(
            rx.cond(
                item.discount > 0,
                f"${item.discount:.2f}",
                "-",
            ),
            class_name="py-4 text-sm text-red-600 text-right border-b border-gray-100",
        ),
        rx.el.td(
            f"${item.amount:.2f}",
            class_name="py-4 text-sm text-gray-900 font-semibold text-right border-b border-gray-100",
        ),
    )


def invoice_preview() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    # Logo si está disponible
                    rx.cond(
                        InvoiceState.logo_url,
                        rx.el.img(
                            src=InvoiceState.logo_url,
                            alt="Logo",
                            class_name="h-16 w-auto mb-4"
                        ),
                        rx.el.div()  # Empty div if no logo
                    ),
                    rx.el.h2(
                        InvoiceState.from_name,
                        class_name="text-xl font-bold text-gray-900",
                    ),
                    rx.el.p(
                        InvoiceState.from_address,
                        class_name="text-sm text-gray-500 mt-1",
                    ),
                    rx.el.p(
                        InvoiceState.from_details, class_name="text-sm text-gray-500"
                    ),
                    rx.el.p(
                        f"RIF/Cédula: {InvoiceState.from_tax_id}", class_name="text-sm text-gray-500 mt-1"
                    ),
                    rx.el.p(
                        InvoiceState.from_email, class_name="text-sm text-gray-500 mt-2"
                    ),
                    rx.el.p(
                        InvoiceState.from_phone, class_name="text-sm text-gray-500"
                    ),
                ),
                rx.el.div(
                    rx.el.h1(
                        "NOTA DE ENTREGA",
                        class_name="text-4xl font-bold text-gray-200 text-right tracking-tight",
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.el.span(
                                "No.", class_name="text-sm font-medium text-gray-400"
                            ),
                            rx.el.span(
                                InvoiceState.invoice_number,
                                class_name="text-sm font-semibold text-gray-900 text-right",
                            ),
                            class_name="flex justify-between gap-8 mt-4",
                        ),
                        rx.el.div(
                            rx.el.span(
                                "Fecha", class_name="text-sm font-medium text-gray-400"
                            ),
                            rx.el.span(
                                InvoiceState.invoice_date,
                                class_name="text-sm font-semibold text-gray-900 text-right",
                            ),
                            class_name="flex justify-between gap-8 mt-1",
                        ),
                        rx.el.div(
                            rx.el.span(
                                "Vence", class_name="text-sm font-medium text-gray-400"
                            ),
                            rx.el.span(
                                InvoiceState.due_date,
                                class_name="text-sm font-semibold text-gray-900 text-right",
                            ),
                            class_name="flex justify-between gap-8 mt-1",
                        ),
                        class_name="flex flex-col",
                    ),
                    class_name="flex flex-col items-end",
                ),
                class_name="flex justify-between items-start mb-12",
            ),
            rx.el.div(
                rx.el.h3(
                    "Entregar a:",
                    class_name="text-xs font-bold text-gray-400 uppercase tracking-wider mb-3",
                ),
                rx.el.p(
                    InvoiceState.to_name, class_name="text-base font-bold text-gray-900"
                ),
                rx.el.p(InvoiceState.to_company, class_name="text-sm text-gray-600"),
                rx.el.p(InvoiceState.to_address, class_name="text-sm text-gray-600"),
                rx.el.p(InvoiceState.to_details, class_name="text-sm text-gray-600"),
                rx.el.p(
                    f"RIF/Cédula: {InvoiceState.to_tax_id}", class_name="text-sm text-gray-600 mt-1"
                ),
                class_name="mb-12 bg-gray-50 p-6 rounded-xl border border-gray-100 inline-block min-w-[300px]",
            ),
            rx.el.table(
                rx.el.thead(
                    rx.el.tr(
                        rx.el.th(
                            "DESCRIPCIÓN",
                            class_name="text-left text-xs font-bold text-gray-400 pb-4 border-b border-gray-200",
                        ),
                        rx.el.th(
                            "CANT.",
                            class_name="text-right text-xs font-bold text-gray-400 pb-4 border-b border-gray-200 w-20",
                        ),
                        rx.el.th(
                            "PRECIO",
                            class_name="text-right text-xs font-bold text-gray-400 pb-4 border-b border-gray-200 w-24",
                        ),
                        rx.el.th(
                            "DESC.",
                            class_name="text-right text-xs font-bold text-gray-400 pb-4 border-b border-gray-200 w-20",
                        ),
                        rx.el.th(
                            "TOTAL",
                            class_name="text-right text-xs font-bold text-gray-400 pb-4 border-b border-gray-200 w-28",
                        ),
                    )
                ),
                rx.el.tbody(rx.foreach(InvoiceState.items, preview_item_row)),
                class_name="w-full mb-8",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.span(
                            "Subtotal", class_name="text-sm font-medium text-gray-500"
                        ),
                        rx.el.span(
                            f"${InvoiceState.subtotal:.2f}",
                            class_name="text-sm font-semibold text-gray-900",
                        ),
                        class_name="flex justify-between mb-2",
                    ),
                    rx.el.div(
                        rx.el.span(
                            f"Impuestos ({InvoiceState.tax_rate}%)",
                            class_name="text-sm font-medium text-gray-500",
                        ),
                        rx.el.span(
                            f"${InvoiceState.tax_amount:.2f}",
                            class_name="text-sm font-semibold text-gray-900",
                        ),
                        class_name="flex justify-between mb-4 pb-4 border-b border-gray-100",
                    ),
                    rx.el.div(
                        rx.el.span(
                            "Total", class_name="text-lg font-bold text-gray-900"
                        ),
                        rx.el.span(
                            f"${InvoiceState.total:.2f}",
                            class_name="text-lg font-bold text-emerald-600",
                        ),
                        class_name="flex justify-between",
                    ),
                    class_name="w-64 ml-auto",
                ),
                class_name="flex justify-end",
            ),
            # Payment Information Section
            rx.cond(
                InvoiceState.payment_method,
                rx.el.div(
                    rx.el.h3(
                        "Información de Pago:",
                        class_name="text-xs font-bold text-gray-400 uppercase tracking-wider mb-3",
                    ),
                    rx.el.p(
                        f"Método: {InvoiceState.payment_method}", 
                        class_name="text-sm text-gray-600 mb-1"
                    ),
                    rx.el.p(
                        f"Banco: {InvoiceState.bank_name}", 
                        class_name="text-sm text-gray-600 mb-1"
                    ),
                    rx.el.p(
                        f"Cuenta: {InvoiceState.bank_account}", 
                        class_name="text-sm text-gray-600 mb-4"
                    ),
                    class_name="mb-8 bg-blue-50 p-4 rounded-xl border border-blue-100 inline-block",
                ),
            ),
            # Terms and Conditions Section
            rx.cond(
                InvoiceState.terms_conditions,
                rx.el.div(
                    rx.el.h3(
                        "Términos y Condiciones:",
                        class_name="text-xs font-bold text-gray-400 uppercase tracking-wider mb-2",
                    ),
                    rx.el.p(
                        InvoiceState.terms_conditions, 
                        class_name="text-sm text-gray-600 mb-4"
                    ),
                    class_name="mb-8",
                ),
            ),
            # Notes Section
            rx.cond(
                InvoiceState.notes,
                rx.el.div(
                    rx.el.h3(
                        "Notas:",
                        class_name="text-xs font-bold text-gray-400 uppercase tracking-wider mb-2",
                    ),
                    rx.el.p(
                        InvoiceState.notes, 
                        class_name="text-sm text-gray-600 mb-4"
                    ),
                    class_name="mb-8",
                ),
            ),
            # Authorization Section
            rx.cond(
                InvoiceState.authorized_by,
                rx.el.div(
                    rx.el.div(
                        rx.el.div(
                            rx.el.p(
                                "Autorizado por:",
                                class_name="text-xs font-medium text-gray-500 mb-1"
                            ),
                            rx.el.p(
                                InvoiceState.authorized_by,
                                class_name="text-sm font-bold text-gray-900"
                            ),
                            class_name="flex-1",
                        ),
                        rx.el.div(
                            rx.el.p(
                                "Firma:",
                                class_name="text-xs font-medium text-gray-500 mb-1"
                            ),
                            rx.el.div(
                                class_name="w-32 h-16 border-b-2 border-gray-300 border-dashed"
                            ),
                            class_name="flex-1",
                        ),
                        class_name="flex gap-8 items-end",
                    ),
                    class_name="mt-12 pt-8 border-t border-gray-200",
                ),
            ),
            class_name="bg-white p-12 shadow-lg min-h-[800px] w-full max-w-[816px] mx-auto border border-gray-200",
        ),
        class_name="bg-gray-500/10 p-8 rounded-2xl overflow-auto flex justify-center",
    )