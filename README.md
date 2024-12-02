# GameLog - Plataforma de Blog

## Requisitos Previos
- Python 3.12 o superior
- pip (instalador de paquetes de Python)
- Git (opcional, para clonar el repositorio)

## Instrucciones de Configuración
1. **Clonar o descargar el proyecto**
   ```bash
   git clone <url-del-repositorio>
   # o descargar y extraer el archivo ZIP
   ```

2. **Crear y activar un entorno virtual**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instalar paquetes requeridos**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar el servidor de desarrollo**
   ```bash
   cd gamelog
   python manage.py runserver
   ```

5. **Acceder al sitio web**
   - Sitio principal: http://127.0.0.1:[puerto]/blog/
   - Panel de administración: http://127.0.0.1:[puerto]/admin

## Características Principales
- Autenticación de usuarios (registro, inicio de sesión, cierre de sesión)
- Creación de publicaciones con soporte para markdown
- Sistema de comentarios
- Diseño responsive con Tailwind CSS

## Notas Importantes
1. **Base de datos**: El proyecto usa SQLite por defecto (archivo db.sqlite3)
