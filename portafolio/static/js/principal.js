// js/principal.js

// Importar los módulos de funcionalidad
import { inicializarDesplazamientoSuave } from '/static/js/desplazamiento-suave.js';
import { inicializarValidacionFormulario } from '/static/js/validacion-formulario.js';

/**
 * Inicializa todas las funcionalidades del sitio cuando el DOM está completamente cargado.
 */
document.addEventListener('DOMContentLoaded', () => {
    inicializarDesplazamientoSuave();
    inicializarValidacionFormulario();
});
