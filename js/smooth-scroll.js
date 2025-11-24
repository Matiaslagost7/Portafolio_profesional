// js/smooth-scroll.js

/**
 * Aplica un desplazamiento suave a los enlaces internos de la página.
 * Cuando se hace clic en un enlace que apunta a una sección (ej. #about),
 * la página se desplaza suavemente en lugar de saltar directamente.
 * También cierra el menú de navegación si está abierto en vista móvil.
 */
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);

            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth'
                });
            }

            // Cerrar el menú de navegación de Bootstrap si está abierto
            const navbarToggler = document.querySelector('.navbar-toggler');
            const navbarCollapse = document.querySelector('.navbar-collapse');
            if (navbarToggler && navbarCollapse.classList.contains('show')) {
                navbarToggler.click();
            }
        });
    });
}

export { initSmoothScroll };
