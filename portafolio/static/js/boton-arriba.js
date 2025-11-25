// js/boton-arriba.js

/**
 * Crea y gestiona el botón "Regresar arriba" para mejorar la UX.
 * El botón aparece al hacer scroll hacia abajo y permite volver al inicio suavemente.
 */
function inicializarBotonArriba() {
    // Crear el botón si no existe
    let boton = document.getElementById('boton-arriba');
    if (!boton) {
        boton = document.createElement('button');
        boton.id = 'boton-arriba';
        boton.title = 'Volver arriba';
        boton.innerHTML = '<i class="fas fa-arrow-up"></i>';
        document.body.appendChild(boton);
    }
    // Mostrar/ocultar según el scroll
    window.addEventListener('scroll', () => {
        if (window.scrollY > 200) {
            boton.classList.add('visible');
        } else {
            boton.classList.remove('visible');
        }
    });
    // Scroll suave al hacer clic
    boton.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });
}

export { inicializarBotonArriba };
