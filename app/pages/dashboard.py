import reflex as rx
from app.components.navbar import navbar
from app.components.card import document_selection_card


def dashboard() -> rx.Component:
    return rx.el.div(
        navbar(),
        rx.el.main(
            rx.el.div(
                rx.el.div(
                    rx.el.span(
                        "Nosglobal Logistic",
                        class_name="text-blue-600 font-semibold tracking-wider uppercase text-xs mb-2 block",
                    ),
                    rx.el.h1(
                        "Generador de Documentos",
                        class_name="text-4xl md:text-5xl font-bold text-gray-900 mb-6 tracking-tight",
                    ),
                    rx.el.p(
                        "Selecciona el tipo de documento que deseas generar. Podrás editar los datos en tiempo real y exportar los resultados a PDF o Excel con un solo clic.",
                        class_name="text-lg text-gray-600 max-w-2xl mx-auto leading-relaxed",
                    ),
                    class_name="text-center py-20 px-4",
                ),
                rx.el.div(
                    document_selection_card(
                        "Estado de Cuenta",
                        "Genera reportes detallados de transacciones, incluyendo débitos, créditos y balances por cliente. Ideal para cortes mensuales.",
                        "landmark",
                        "/statement",
                        "text-blue-600",
                        "bg-blue-50",
                    ),
                    document_selection_card(
                        "Nota de entrega",
                        "Crea notas de entrega profesionales desglosadas con items, impuestos, subtotales y notas personalizadas. Formato estándar internacional.",
                        "receipt",
                        "/invoice",
                        "text-emerald-600",
                        "bg-emerald-50",
                    ),
                    document_selection_card(
                        "Recibo de Almacén",
                        "Genera recibos de almacén con información detallada de paquetes, dimensiones, tracking y documentación completa de envíos.",
                        "package",
                        "/warehouse-receipt",
                        "text-orange-600",
                        "bg-orange-50",
                    ),
                    document_selection_card(
                        "Cotización / Presupuesto",
                        "Crea cotizaciones profesionales para tus clientes con detalles de servicios, precios y términos. Incluye función de copiar al portapapeles para emails.",
                        "calculator",
                        "/quotation",
                        "text-purple-600",
                        "bg-purple-50",
                    ),
                    class_name="grid md:grid-cols-2 lg:grid-cols-4 gap-6 max-w-7xl mx-auto px-4",
                ),
                class_name="container mx-auto pb-20",
            ),
            class_name="min-h-[calc(100vh-64px)] bg-gray-50/50",
        ),
        class_name="font-['Inter']",
    )