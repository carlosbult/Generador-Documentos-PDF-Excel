# Análisis del Proyecto y Guía de Instalación

## Análisis del Proyecto

Este proyecto es una aplicación web construida con **Reflex** (anteriormente Pynecone), un framework de Python para crear aplicaciones web full-stack.

**Funcionalidad Principal:**
El sistema es un "Generador de Documentos" que permite crear:
1.  **Estados de Cuenta**: Con tablas de transacciones, cálculos de balance y exportación.
2.  **Facturas (Invoices)**: Con detalles de emisor/receptor, líneas de productos, impuestos y totales.

**Tecnologías Clave:**
*   **Reflex (v0.8.20)**: Framework principal para frontend y backend en Python.
*   **ReportLab**: Motor para la generación programática de archivos PDF.
*   **OpenPyXL**: Librería para la creación y manipulación de archivos Excel.
*   **PyPDF2**: Utilidad para manipulación de PDFs.
*   **TailwindCSS**: Utilizado para el estilizado de la interfaz (integrado vía plugin de Reflex).

---

## Herramientas Necesarias (Prerrequisitos)

Para ejecutar este proyecto en tu PC (Mac), necesitas instalar las siguientes herramientas fundamentales.

### 1. Python (Versión 3.10 o superior)
Reflex 0.8.x requiere **Python 3.10** como mínimo. Tu sistema parece tener Python 3.9, lo cual causa que no encuentre la versión correcta de Reflex.
*   **Verificar si ya lo tienes:** Abre tu terminal y escribe `python3 --version`. Si dice 3.9.x, necesitas actualizar.
*   **Instalación:** Descarga la versión más reciente (3.11 o 3.12) desde [python.org](https://www.python.org/downloads/).

### 2. Node.js (Versión 16.8.0 o superior)
Reflex utiliza Node.js bajo el capó para construir la interfaz de usuario (el frontend).
*   **Verificar si ya lo tienes:** Escribe `node -v` en tu terminal.
*   **Instalación:** Descarga la versión "LTS" (Long Term Support) desde [nodejs.org](https://nodejs.org/).

### 3. Git (Opcional pero recomendado)
Para gestionar el código fuente.
*   **Verificar:** `git --version`.
*   **Instalación:** Si tienes Xcode instalado en tu Mac, ya lo tienes. Si no, puedes instalarlo o usar [git-scm.com](https://git-scm.com/).

---

## Pasos para Instalar y Correr el Proyecto

Una vez tengas Python y Node.js instalados, sigue estos pasos en tu terminal dentro de la carpeta del proyecto:

### 1. Crear un Entorno Virtual (Recomendado)
Es una buena práctica aislar las dependencias del proyecto.
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Instalar Dependencias
Instala las librerías listadas en `requirements.txt`.
```bash
pip install -r requirements.txt
```

### 3. Inicializar Reflex
Esto descargará e instalará las dependencias de frontend necesarias.
```bash
reflex init
```

### 4. Ejecutar la Aplicación
Para correr el servidor de desarrollo:
```bash
reflex run
```
La aplicación debería estar disponible en `http://localhost:3000`.

---

## Solución de Problemas Comunes

*   **Puerto ocupado:** Si el puerto 3000 o 8000 está ocupado, Reflex te avisará. Puedes liberar el puerto o cambiar la configuración.
*   **Versión de Reflex:** El proyecto especifica `reflex==0.8.20`. Si tienes una versión más nueva instalada globalmente, asegúrate de usar el entorno virtual para usar la versión correcta del proyecto y evitar incompatibilidades.
