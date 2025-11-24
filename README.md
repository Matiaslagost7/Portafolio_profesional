# Portafolio

Django • Python • SQLite

```bash
python manage.py runserver
```
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
