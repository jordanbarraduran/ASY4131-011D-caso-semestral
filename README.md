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

4. **Configurar la base de datos**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Crear un superusuario (cuenta de administrador)**
   ```bash
   python manage.py createsuperuser
   # Sigue las indicaciones para crear una cuenta de administrador
   ```

6. **Ejecutar el servidor de desarrollo**
   ```bash
   python manage.py runserver
   ```

7. **Acceder al sitio web**
   - Sitio principal: http://127.0.0.1:8000/blog/
   - Panel de administración: http://127.0.0.1:8000/admin

## Características Principales
- Autenticación de usuarios (registro, inicio de sesión, cierre de sesión)
- Creación de publicaciones con soporte para markdown
- Sistema de comentarios
- Diseño responsive con Tailwind CSS

## Notas Importantes
1. **Base de datos**: El proyecto usa SQLite por defecto (archivo db.sqlite3)

## Problemas Comunes y Soluciones
1. **Los archivos estáticos no cargan**
   ```bash
   python manage.py collectstatic
   ```

2. **Problemas con la base de datos**
   ```bash
   python manage.py migrate
   ```

3. **Problemas con la instalación de Pillow**
   - Windows: Asegúrate de tener Microsoft Visual C++ Build Tools
   - Linux: `sudo apt-get install python3-dev libjpeg-dev zlib1g-dev`

4. **Problemas de permisos con la carga de archivos**
   - Asegúrate de que el directorio 'media' existe y tiene permisos de escritura

## Probando la Instalación
1. Crear un superusuario
2. Iniciar sesión en el panel de administración o directamente en la página del blog
3. Crear una publicación de prueba
5. Probar el formato markdown
