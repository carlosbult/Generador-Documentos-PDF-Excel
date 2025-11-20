import reflex as rx


def document_selection_card(
    title: str,
    description: str,
    icon_name: str,
    href: str,
    color_class: str,
    bg_color_class: str,
) -> rx.Component:
    return rx.el.a(
        rx.el.div(
            rx.el.div(
                rx.icon(icon_name, class_name=f"w-6 h-6 {color_class}"),
                class_name=f"p-3 rounded-xl {bg_color_class} w-fit mb-5 group-hover:scale-110 transition-transform duration-300",
            ),
            rx.el.h3(title, class_name="text-lg font-semibold text-gray-900 mb-2"),
            rx.el.p(
                description, class_name="text-sm text-gray-500 leading-relaxed mb-6"
            ),
            rx.el.div(
                rx.el.span(
                    "Crear Documento", class_name="text-sm font-semibold text-gray-900"
                ),
                rx.icon(
                    "arrow-right",
                    class_name="w-4 h-4 text-gray-900 group-hover:translate-x-1 transition-transform",
                ),
                class_name="flex items-center gap-2 mt-auto opacity-60 group-hover:opacity-100 transition-opacity duration-200",
            ),
            class_name="h-full p-6 rounded-2xl bg-white border border-gray-200 shadow-sm hover:shadow-xl hover:border-blue-200 transition-all duration-300 group flex flex-col",
        ),
        href=href,
        class_name="block h-full",
    )