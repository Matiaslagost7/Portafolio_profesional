#  Portafolio Profesional - Matías Lagos T.

> Plataforma web interactiva desarrollada con **Django**, **Python** y **CSS moderno**. Portafolio profesional completo con sistema de gestión de contenido integrado.

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.2.8-darkgreen?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![SQLite](https://img.shields.io/badge/SQLite-Database-lightblue?logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

##  Descripción General

Portafolio profesional full-stack desarrollado durante mi formación en desarrollo web. Sistema completo que permite gestionar y mostrar proyectos, habilidades y competencias profesionales sin necesidad de modificar código. Implementa buenas prácticas de seguridad, accesibilidad y rendimiento.

###  Características Principales

- ** Autenticación y Autorización:** Sistema seguro de login/register con sesiones de usuario
- ** Diseño Responsivo:** Mobile-first, optimizado para todos los dispositivos
- ** Interfaz Moderna:** Diseño profesional y visualmente atractivo
- ** Base de Datos:** Modelos relacionales con Django ORM
- ** Gestión Dinámica:** Agregar, editar y eliminar proyectos sin código
- ** Panel Administrativo:** Interfaz dedicada para administración de contenido
- ** Optimización:** Imágenes WebP, CSS modular, JavaScript optimizado
- ** Accesibilidad:** WCAG 2.1 compliant

---

##  Stack Tecnológico

### Backend
- **Framework:** Django 5.2.8
- **Lenguaje:** Python 3.x
- **Base de Datos:** SQLite
- **ORM:** Django ORM
- **Autenticación:** Django Auth

### Frontend
- **Markup:** HTML5 semántico
- **Estilos:** CSS3 personalizado y modular
- **Interactividad:** JavaScript vanilla
- **Imágenes:** WebP optimizado
- **Responsividad:** Media queries estratégicas

### Herramientas & DevOps
- **Control de Versiones:** Git & GitHub
- **Gestor de Dependencias:** pip
- **Diseño UI/UX:** Figma
- **Entorno Virtual:** venv

---

##  Estructura del Proyecto

\\\
portafolio/

 manage.py                      # Gestor de comandos Django
 db.sqlite3                     # Base de datos SQLite
 LICENSE                        # Licencia del proyecto
 README.md                      # Este archivo

 portafolio/                    # Configuración principal del proyecto
    settings.py               # Configuración de Django
    urls.py                   # Rutas principales del proyecto
    wsgi.py                   # Configuración WSGI para producción
    asgi.py                   # Configuración ASGI
    __pycache__/              # Caché de Python

 login/                         # App: Autenticación de usuarios
    models.py                 # Modelos (extiende User de Django)
    views.py                  # Vistas (login, register, logout)
    forms.py                  # Formularios personalizados
    urls.py                   # Rutas de autenticación
    admin.py                  # Configuración admin
    migrations/               # Migraciones de base de datos
    templates/
       login.html            # Página de login
       register.html         # Página de registro
       logout.html           # Confirmación de logout
    __pycache__/              # Caché de Python

 proyectos/                     # App: Portafolio (módulo principal)
    models.py                 # Modelos: Proyecto, Habilidad
    views.py                  # Vistas del portafolio y panel admin
    forms.py                  # Formularios de gestión
    admin.py                  # Configuración admin de Django
    urls.py                   # Rutas del portafolio
    apps.py                   # Configuración de la app
    migrations/               # Migraciones de BD
    templates/
       base.html             # Plantilla base (layout general)
       home.html             # Página principal
       panel_admin.html      # Panel administrativo
       habilidades/          # Templates dinámicas de habilidades
       proyectos/            # Templates dinámicas de proyectos
       home/                 # Templates de secciones del home
    __pycache__/              # Caché de Python

 static/                        # Archivos estáticos servidos por el servidor
    styles/                   # Hojas de estilos CSS
       base.css              # Estilos base globales
       heroe.css             # Sección hero
       habilidades.css       # Sección de habilidades
       proyectos.css         # Sección de proyectos
       acerca-de.css         # Sección about
       contacto.css          # Sección de contacto
       encabezado.css        # Header/Navbar
       pie-pagina.css        # Footer
       responsivo.css        # Media queries y responsive
    js/                       # Scripts JavaScript
        principal.js          # Funciones principales
        desplazamiento-suave.js  # Scroll suave
        validacion-formulario.js # Validación del formulario

 media/                         # Archivos multimedia subidos
    webp/                     # Imágenes optimizadas en WebP

 env/                           # Entorno virtual de Python
     Scripts/                  # Ejecutables (Windows)
     Lib/                      # Dependencias instaladas
        site-packages/        # Paquetes como Django, Pillow, etc.
     pyvenv.cfg               # Configuración del venv
\\\

---

##  Instalación y Configuración

###  Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- git
- Un editor de código (VS Code recomendado)

###  Pasos de Instalación

#### 1. Clonar el repositorio
\\\ash
git clone https://github.com/Matiaslagost7/Portafolio_profesional.git
cd Portafolio_profesional
\\\

#### 2. Crear y activar el entorno virtual

**En Windows (PowerShell):**
\\\powershell
python -m venv env
.\env\Scripts\Activate.ps1
\\\

**En macOS/Linux:**
\\\ash
python3 -m venv env
source env/bin/activate
\\\

#### 3. Instalar dependencias
\\\ash
pip install -r requirements.txt
\\\

#### 4. Aplicar migraciones de la base de datos
\\\ash
python manage.py migrate
\\\

#### 5. Crear usuario superadmin
\\\ash
python manage.py createsuperuser
\\\
Sigue las indicaciones para crear tu usuario admin.

#### 6. Ejecutar el servidor de desarrollo
\\\ash
python manage.py runserver
\\\

El portafolio estará disponible en: \http://127.0.0.1:8000/\

#### 7. Acceder al panel administrativo
Dirígete a: \http://127.0.0.1:8000/admin/\

Usa las credenciales del superuser que creaste en el paso 5.

---

##  Uso y Funcionalidades

### Para Visitantes
- Ver proyectos destacados
- Conocer habilidades y competencias
- Enviar mensajes de contacto
- Navegación fluida y responsiva

### Para el Administrador
- **Acceso Panel Admin:** \http://localhost:8000/admin/\
- Gestionar proyectos (crear, editar, eliminar)
- Gestionar habilidades
- Ver estadísticas
- Administrar usuarios

### Rutas Principales

| Ruta | Descripción |
|------|-------------|
| \/\ | Página principal |
| \/admin/\ | Panel administrativo Django |
| \/proyectos/\ | Listado de proyectos |
| \/habilidades/\ | Listado de habilidades |
| \/login/\ | Iniciar sesión |
| \/register/\ | Registrarse |
| \/logout/\ | Cerrar sesión |

---

##  Características Técnicas Destacadas

### Responsividad
- Diseño Mobile-First
- Breakpoints: 576px, 992px
- 100% adaptable a cualquier dispositivo
- Touch-friendly interfaces

### Optimización de Rendimiento
- Imágenes comprimidas en formato WebP
- CSS modular y minificado
- JavaScript sin dependencias externas
- Carga rápida (<3s en conexión 4G)

### Seguridad
- Protección CSRF en formularios
- Validación de datos en backend y frontend
- Autenticación requerida para ciertas áreas
- Contraseñas hasheadas con Django

### Accesibilidad
- HTML semántico
- Etiquetas ARIA
- Navegación por teclado
- Alto contraste de colores
- Textos alternativos en imágenes

---

##  Dependencias

\\\	xt
Django==5.2.8
Pillow==12.0.0  # Para manejo de imágenes
sqlparse==0.5.3  # Dependencia de Django
asgiref==3.11.0  # Dependencia de Django
tzdata==2025.2   # Zonas horarias
\\\

Para instalar automáticamente, usa:
\\\ash
pip install -r requirements.txt
\\\

---

##  Comandos Útiles de Django

\\\ash
# Crear nueva app
python manage.py startapp nombre_app

# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Shell interactiva de Django
python manage.py shell

# Recolectar archivos estáticos
python manage.py collectstatic

# Ejecutar servidor de desarrollo
python manage.py runserver
\\\

---

##  Proceso de Desarrollo

### Planificación & Diseño
- Bocetado de wireframes en Figma
- Definición de estructura de navegación
- Prototipo interactivo

### Desarrollo Iterativo
1. Implementación del backend (modelos y views)
2. Creación de templates HTML
3. Estilización con CSS modular
4. Añadir interactividad con JavaScript
5. Testing y ajustes
6. Optimización de rendimiento

### Mejoras Continuas
- Actualización regular de proyectos
- Feedback de usuarios
- Optimización SEO
- Mantenimiento de dependencias

---

##  Problemas Detectados y Soluciones

| Problema | Solución Aplicada |
|----------|-------------------|
| Imágenes pesadas ralentizaban la carga | Compresión y conversión a WebP |
| CSS monolítico difícil de mantener | Separación en módulos por sección |
| JavaScript sin estructura | Modularización de funcionalidades |
| Falta de autenticación | Sistema login/register implementado |
| Datos hardcodeados | Base de datos dinámica con Django ORM |

---

##  Próximas Mejoras

- [ ] Integración con CMS headless
- [ ] API REST completa
- [ ] Certificado SSL
- [ ] Hosting en producción
- [ ] Temas oscuro/claro
- [ ] Multiidioma
- [ ] Analytics avanzado
- [ ] Integración con redes sociales

---

##  Contacto

**Matías Lagos T.**
- Email: [tu email]
- GitHub: [@Matiaslagost7](https://github.com/Matiaslagost7)
- LinkedIn: [tu perfil]
- Portafolio: [URL cuando esté en producción]

---

##  Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

---

##  Contribuciones

Las contribuciones son bienvenidas. Para cambios mayores, abre un issue primero para discutir los cambios propuestos.

\\\ash
# Fork del proyecto
# Crea tu rama (git checkout -b feature/AmazingFeature)
# Commit tus cambios (git commit -m 'Add some AmazingFeature')
# Push a la rama (git push origin feature/AmazingFeature)
# Abre un Pull Request
\\\

---

**Última actualización:** Noviembre 2025

 Si te gusta este proyecto, no olvides darle una estrella en GitHub.
