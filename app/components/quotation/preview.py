"""Quotation preview component."""

import reflex as rx
from app.states.quotation_state import QuotationItem, QuotationState


def preview_header() -> rx.Component:
    """Create the preview header with company and quotation info."""
    return rx.el.div(
        # Left side - Company info
        rx.el.div(
            rx.cond(
                QuotationState.company_logo_url,
                rx.el.img(
                    src=QuotationState.company_logo_url,
                    alt="Logo",
                    class_name="h-16 w-auto mb-3",
                ),
                rx.el.div(),
            ),
            rx.el.h2(
                QuotationState.company_name,
                class_name="text-xl font-bold text-gray-900 mb-2",
            ),
            rx.el.p(
                QuotationState.company_address, class_name="text-sm text-gray-600"
            ),
            rx.el.p(QuotationState.company_phone, class_name="text-sm text-gray-600"),
            class_name="flex flex-col",
        ),
        # Right side - Quotation info
        rx.el.div(
            rx.el.h1(
                "COTIZACIÓN",
                class_name="text-3xl font-bold text-right text-purple-600 mb-3",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.span("No.", class_name="text-xs font-medium text-gray-500"),
                    rx.el.span(
                        QuotationState.quote_number,
                        class_name="text-sm font-bold text-gray-900",
                    ),
                    class_name="flex justify-between gap-4 mb-1",
                ),
                rx.el.div(
                    rx.el.span(
                        "Fecha", class_name="text-xs font-medium text-gray-500"
                    ),
                    rx.el.span(
                        QuotationState.quote_date, class_name="text-sm text-gray-900"
                    ),
                    class_name="flex justify-between gap-4 mb-1",
                ),
                rx.el.div(
                    rx.el.span(
                        "Válida hasta", class_name="text-xs font-medium text-gray-500"
                    ),
                    rx.el.span(
                        QuotationState.valid_until, class_name="text-sm text-gray-900"
                    ),
                    class_name="flex justify-between gap-4",
                ),
            ),
            class_name="flex flex-col items-end",
        ),
        class_name="flex justify-between items-start mb-8 pb-6 border-b-2 border-gray-200 gap-8",
    )


def client_section() -> rx.Component:
    """Create the client information section."""
    return rx.el.div(
        rx.el.h3(
            "Para:",
            class_name="text-xs font-bold text-gray-400 uppercase tracking-wider mb-3",
        ),
        rx.el.p(
            QuotationState.client_name,
            class_name="text-base font-bold text-gray-900",
        ),
        rx.cond(
            QuotationState.client_company,
            rx.el.p(
                QuotationState.client_company, class_name="text-sm text-gray-600"
            ),
        ),
        rx.cond(
            QuotationState.client_address,
            rx.el.p(QuotationState.client_address, class_name="text-sm text-gray-600"),
        ),
        # Optional fields - Only show if provided
        rx.cond(
            QuotationState.client_email,
            rx.el.p(
                rx.el.span("Email: ", class_name="font-medium"),
                QuotationState.client_email,
                class_name="text-sm text-gray-600 mt-2",
            ),
        ),
        rx.cond(
            QuotationState.client_phone,
            rx.el.p(
                rx.el.span("Tel: ", class_name="font-medium"),
                QuotationState.client_phone,
                class_name="text-sm text-gray-600",
            ),
        ),
        class_name="mb-8 bg-gray-50 p-6 rounded-xl border border-gray-100 inline-block min-w-[350px]",
    )


def item_table_row(item: QuotationItem) -> rx.Component:
    """Create a table row for a quotation item."""
    return rx.el.tr(
        rx.el.td(
            item.description,
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
                f"-${item.discount:.2f}",
                "-",
            ),
            class_name="py-4 text-sm text-red-600 text-right border-b border-gray-100",
        ),
        rx.el.td(
            f"${item.amount:.2f}",
            class_name="py-4 text-sm text-gray-900 font-semibold text-right border-b border-gray-100",
        ),
    )


def items_table() -> rx.Component:
    """Create the items table."""
    return rx.el.table(
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
        rx.el.tbody(rx.foreach(QuotationState.items, item_table_row)),
        class_name="w-full mb-8",
    )


def totals_section() -> rx.Component:
    """Create the totals section."""
    return rx.el.div(
        rx.el.div(
            # Subtotal
            rx.el.div(
                rx.el.span("Subtotal", class_name="text-sm font-medium text-gray-500"),
                rx.el.span(
                    f"${QuotationState.subtotal:.2f}",
                    class_name="text-sm font-semibold text-gray-900",
                ),
                class_name="flex justify-between mb-2",
            ),
            # Global Discount (if applicable)
            rx.cond(
                QuotationState.discount_global > 0,
                rx.el.div(
                    rx.el.span(
                        "Descuento", class_name="text-sm font-medium text-gray-500"
                    ),
                    rx.el.span(
                        f"-${QuotationState.discount_global:.2f}",
                        class_name="text-sm font-semibold text-red-600",
                    ),
                    class_name="flex justify-between mb-2",
                ),
            ),
            # Tax (if applicable)
            rx.cond(
                QuotationState.tax_rate > 0,
                rx.el.div(
                    rx.el.span(
                        f"Impuestos ({QuotationState.tax_rate}%)",
                        class_name="text-sm font-medium text-gray-500",
                    ),
                    rx.el.span(
                        f"${QuotationState.tax_amount:.2f}",
                        class_name="text-sm font-semibold text-gray-900",
                    ),
                    class_name="flex justify-between mb-2",
                ),
            ),
            # Shipping (if applicable)
            rx.cond(
                QuotationState.shipping_cost > 0,
                rx.el.div(
                    rx.el.span("Envío", class_name="text-sm font-medium text-gray-500"),
                    rx.el.span(
                        f"${QuotationState.shipping_cost:.2f}",
                        class_name="text-sm font-semibold text-gray-900",
                    ),
                    class_name="flex justify-between mb-4 pb-4 border-b border-gray-100",
                ),
            ),
            # Total
            rx.el.div(
                rx.el.span("TOTAL", class_name="text-lg font-bold text-gray-900"),
                rx.el.span(
                    f"${QuotationState.total:.2f}",
                    class_name="text-lg font-bold text-purple-600",
                ),
                class_name="flex justify-between",
            ),
            class_name="w-64 ml-auto",
        ),
        class_name="flex justify-end mb-8",
    )


def additional_sections() -> rx.Component:
    """Create additional sections for notes, payment terms, etc."""
    return rx.el.div(
        # Notes
        rx.cond(
            QuotationState.notes,
            rx.el.div(
                rx.el.h3(
                    "Notas:",
                    class_name="text-xs font-bold text-gray-400 uppercase tracking-wider mb-2",
                ),
                rx.el.p(QuotationState.notes, class_name="text-sm text-gray-600"),
                class_name="mb-6",
            ),
        ),
        # Payment Terms
        rx.cond(
            QuotationState.payment_terms,
            rx.el.div(
                rx.el.h3(
                    "Términos de Pago:",
                    class_name="text-xs font-bold text-gray-400 uppercase tracking-wider mb-2",
                ),
                rx.el.p(
                    QuotationState.payment_terms, class_name="text-sm text-gray-600"
                ),
                class_name="mb-6",
            ),
        ),
        # Terms and Conditions
        rx.cond(
            QuotationState.terms_conditions,
            rx.el.div(
                rx.el.h3(
                    "Términos y Condiciones:",
                    class_name="text-xs font-bold text-gray-400 uppercase tracking-wider mb-2",
                ),
                rx.el.p(
                    QuotationState.terms_conditions, class_name="text-sm text-gray-600"
                ),
                class_name="mb-6",
            ),
        ),
    )


def quotation_preview() -> rx.Component:
    """Create the main quotation preview."""
    return rx.el.div(
        rx.el.div(
            preview_header(),
            client_section(),
            items_table(),
            totals_section(),
            additional_sections(),
            class_name="bg-white p-12 shadow-lg min-h-[800px] w-full max-w-[816px] mx-auto border border-gray-200",
        ),
        class_name="bg-gray-500/10 p-8 rounded-2xl overflow-auto flex justify-center",
    )
