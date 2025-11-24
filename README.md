# Portafolio - Matias Lagos T.

Portafolio personal desarrollado con HTML, CSS (sin frameworks pesados) y Bootstrap CDN para la grilla y componentes básicos.

## Resumen del proceso de creación

Este portafolio fue creado como parte de mi formación en desarrollo web, aplicando buenas prácticas de diseño, accesibilidad y optimización. El proceso incluyó:

- **Planificación y diseño:** Bocetado en Figma y definición de la estructura de navegación y secciones.
- **Desarrollo iterativo:** Implementación progresiva de las secciones principales (inicio, sobre mí, habilidades, proyectos y contacto), priorizando la experiencia de usuario y la adaptabilidad a dispositivos móviles.
- **Optimización:** Compresión de imágenes, uso de formatos modernos (WebP), modularización de CSS y JavaScript, y mejoras en el rendimiento para despliegue en GitHub Pages.
- **Accesibilidad:** Formularios accesibles, navegación con teclado y uso de atributos ARIA.

El portafolio se mantiene actualizado con nuevos proyectos y aprendizajes adquiridos durante el bootcamp y experiencias profesionales.

## Estructura
- `index.html`: Página principal.
- `style.css`: Estilos personalizados optimizados para GitHub Pages.
- `script.js`: Scroll suave y validación básica del formulario de contacto.
- `images/`: Recursos gráficos locales.

## Características
- Diseño responsive con solo dos media queries (>=576px y >=992px).
- Navegación fija con compensación (`scroll-margin-top`) para evitar que el contenido quede oculto al usar enlaces internos.
- Formulario accesible con mensajes dinámicos (`aria-live`).
- Imágenes con atributos `width` y `height` para evitar CLS (Layout Shift) en GitHub Pages.
- Favicon y meta `theme-color` para mejorar apariencia en móviles.


## Proyectos Destacados

- **Protege tu Mundo Digital: Ciberseguridad**
	- Sitio educativo sobre ciberseguridad, privacidad y navegación segura.
	- Tecnologías: HTML5, CSS3, JavaScript.
	- [Ver proyecto](https://matiaslagost7.github.io/M2_Evaluacion_del_modulo/index.html) | [Código fuente](https://github.com/Matiaslagost7/M2_Evaluacion_del_modulo)

- **Concesionaria**
	- Sistema web para gestión de vehículos, clientes y ventas en una concesionaria de autos.
	- Tecnologías: Python, CSS, HTML.
	- [Ver proyecto](https://modulo6-concesionaria.onrender.com/) | [Código fuente](https://github.com/Matiaslagost7/Modulo6.Concesionaria) | [Diseño en Behance](https://www.behance.net/gallery/239101539/Portafolio-behance)

- **Cafetería**
	- Aplicación web para administración de productos y ventas en una cafetería.
	- Tecnologías: Python, CSS, HTML.
	- [Código fuente](https://github.com/Matiaslagost7/Modulo-6.-Cafeteria)

## Instrucciones de uso

1. **Clona el repositorio:**
	```bash
	git clone https://github.com/Matiaslagost7/Portafolio.git
	```
2. **Abre la carpeta en tu editor o navegador:**
	- Puedes abrir `index.html` directamente en tu navegador para ver el portafolio localmente.
3. **Publicar en GitHub Pages:**
	- Ve a la configuración del repositorio en GitHub.
	- Busca la sección "Pages".
	- Selecciona la rama `main` y la carpeta raíz (`/`).
	- Guarda y accede a la URL que te proporciona GitHub Pages.

## Dependencias

- [Bootstrap 5.3 (CDN)](https://getbootstrap.com/): Para la grilla y componentes responsivos.
- [Google Fonts: Montserrat](https://fonts.google.com/specimen/Montserrat): Fuente principal.
- No requiere instalación de paquetes ni dependencias adicionales.

## Problemáticas Detectadas y Mejoras Aplicadas

Se identificaron áreas de mejora en el proyecto y se aplicaron las siguientes soluciones:

- **Optimización de imágenes:**
  - **Problemática:** Las imágenes de alta resolución ralentizaban la carga del sitio.
  - **Solución:** Se comprimieron las imágenes para reducir su peso sin una pérdida notable de calidad. Se considera el uso de formatos modernos como WebP para futuras actualizaciones, que ofrecen una compresión superior a JPEG y PNG.

- **Refactorización y organización de CSS:**
  - **Problemática:** El archivo `style.css` podía volverse difícil de mantener a medida que el proyecto creciera.
  - **Solución:** Se recomienda dividir el CSS en archivos más pequeños y específicos (por ejemplo, `header.css`, `projects.css`) e importarlos en un archivo principal para mejorar la modularidad.

- **Modularidad en JavaScript:**
  - **Problemática:** Un único archivo JavaScript para toda la interactividad puede dificultar la depuración y escalabilidad.
  - **Solución:** Se sugiere dividir el código JavaScript en módulos que manejen funcionalidades específicas (ej. un módulo para el carrusel, otro para el formulario). Esto facilita el mantenimiento y asegura que el sitio permanezca funcional si JavaScript está deshabilitado.
