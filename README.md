

# Suite de Métodos Numéricos

Proyecto desarrollado para el curso de **Análisis Numérico (7mo Semestre)**. Esta aplicación permite resolver sistemas de ecuaciones lineales y encontrar raíces de ecuaciones no lineales mediante una interfaz web moderna construida en **Angular** y un potente motor de cálculo en **FastAPI (Python)**.

## 📂 Estructura del Proyecto

```text
Metodos_Numericos/
├── backend/    # Servidor de cálculos (FastAPI)
└── frontend/   # Interfaz de usuario (Angular)

```

---

## Guía de Inicio Rápido

### 1. Configuración del Backend (Python)

Entra a la carpeta de backend y prepara el entorno:

```bash
cd backend
# Crear entorno virtual
python -m venv .venv

# Activar entorno (Windows)
.\.venv\Scripts\activate
# Activar entorno (Linux/Mac)
source .venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

```

**Para iniciar el servicio de la API:**

```bash
uvicorn api:app --reload

```

> **Nota:** La API estará disponible en `http://127.0.0.1:8000`. Puedes ver la documentación interactiva en `/docs`.

---

### 2. Configuración del Frontend (Angular)

Asegúrate de tener instalado **Node.js** y el **Angular CLI**.

```bash
cd ../frontend

# Instalar dependencias (necesario después de un git pull)
npm install

# Iniciar servidor de desarrollo
npm start

```

> **Nota:** La aplicación abrirá automáticamente en `http://localhost:4200`.

---

## Qué hacer después de un `git pull` o descarga

Si acabas de clonar el repositorio o actualizarlo, sigue estos pasos para asegurar que todo funcione:

1. **Backend**:
* Activa tu `.venv`.
* Ejecuta `pip install -r requirements.txt` para asegurar que tienes todas las librerías (como `FastAPI`, `SymPy` o `NumPy`).


2. **Frontend**:
* Ejecuta `npm install`. Esto recreará la carpeta `node_modules` con todas las dependencias necesarias.


3. **Servicios**:
* Recuerda que para que el software funcione, **ambas terminales deben estar activas**: una corriendo el backend (Uvicorn) y otra el frontend (Angular).



---

## Métodos Disponibles

* **Ecuaciones No Lineales**: Bisección, Falsa Posición, Newton-Raphson, Punto Fijo.
* **Sistemas de Ecuaciones Lineales**: Jacobi, Gauss-Seidel.
* **Visualización**: Generación de tablas de iteraciones detalladas por cada método.

---

### Tips de Uso

* **Sintaxis**: Para las funciones matemáticas, utiliza el formato de Python (ej: `x2 + 5*x - 10`).
* **Matrices**: Asegúrate de que las matrices para métodos iterativos sean diagonalmente dominantes para garantizar la convergencia.

---

