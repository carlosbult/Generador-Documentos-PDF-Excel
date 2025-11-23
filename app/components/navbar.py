import reflex as rx


def navbar() -> rx.Component:
    return rx.el.nav(
        rx.el.div(
            rx.el.a(
                rx.el.img(
                    src="/nosglobal-logo.png",
                    alt="Nosglobal Logistic",
                    class_name="w-8 h-8 object-contain",
                ),
                rx.el.span(
                    "Nosglobal Logistic",
                    class_name="text-lg font-bold text-gray-900 tracking-tight",
                ),
                class_name="flex items-center gap-3",
                href="/",
            ),
            rx.el.div(
                rx.el.a(
                    "Dashboard",
                    href="/",
                    class_name="text-sm font-medium text-gray-600 hover:text-blue-600 transition-colors px-3 py-2 rounded-md hover:bg-gray-50",
                ),
                rx.el.a(
                    "Estado de Cuenta",
                    href="/statement",
                    class_name="text-sm font-medium text-gray-600 hover:text-blue-600 transition-colors px-3 py-2 rounded-md hover:bg-gray-50",
                ),
                rx.el.a(
                    "Nota de entrega",
                    href="/invoice",
                    class_name="text-sm font-medium text-gray-600 hover:text-blue-600 transition-colors px-3 py-2 rounded-md hover:bg-gray-50",
                ),
                rx.el.a(
                    "Recibo de Almacén",
                    href="/warehouse-receipt",
                    class_name="text-sm font-medium text-gray-600 hover:text-blue-600 transition-colors px-3 py-2 rounded-md hover:bg-gray-50",
                ),
                class_name="flex gap-1 items-center",
            ),
            class_name="max-w-7xl mx-auto px-4 h-16 flex items-center justify-between",
        ),
        class_name="border-b border-gray-200 bg-white sticky top-0 z-50",
    )