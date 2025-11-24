UTPL - Desarrollo Basado en Plataformas Web
Actividad Experimental AE1 - ORM con SQLAlchemy (SQLite)

Estructura:
- configuracion.py          -> Conexión y Base declarativa (SQLAlchemy 2.x)
- crear_base_entidades.py   -> Modelos ORM y creación de tablas
- poblar_base.py            -> Inserción de datos de ejemplo
- consultas.py              -> Consultas: all, filter, order_by, or, and y joinedload (bonus)
- investigacion.db          -> (Se crea al ejecutar crear_base_entidades.py)

Requisitos:
- Python 3.10+
- Paquetes: SQLAlchemy 2.x

Instalación en Windows (PowerShell):
1) python -m venv .venv
2) . .\.venv\Scripts\Activate.ps1
3) pip install --upgrade pip
4) pip install "SQLAlchemy==2.0.*"

Ejecutar en orden:
1) python crear_base_entidades.py
2) python poblar_base.py
3) python consultas.py

Notas:
- Si ya existe la base, puedes borrar investigacion.db para empezar de cero.
- Puedes activar echo=True en configuracion.py para ver el SQL generado.
