// js/desplazamiento-suave.js

/**
 * Aplica un desplazamiento suave a los enlaces internos de la página.
 * Cuando se hace clic en un enlace que apunta a una sección (ej. #about),
 * la página se desplaza suavemente en lugar de saltar directamente.
 * También cierra el menú de navegación si está abierto en vista móvil.
 */
function inicializarDesplazamientoSuave() {
    document.querySelectorAll('a[href^="#"]').forEach(enlace => {
        enlace.addEventListener('click', function (evento) {
            evento.preventDefault();
            const idDestino = this.getAttribute('href');
            const elementoDestino = document.querySelector(idDestino);

            if (elementoDestino) {
                elementoDestino.scrollIntoView({
                    behavior: 'smooth'
                });
            }

            // Cerrar el menú de navegación de Bootstrap si está abierto
            const botonMenu = document.querySelector('.navbar-toggler');
            const menuCollapse = document.querySelector('.navbar-collapse');
            if (botonMenu && menuCollapse.classList.contains('show')) {
                botonMenu.click();
            }
        });
    });
}

export { inicializarDesplazamientoSuave };
