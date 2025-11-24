// js/principal.js

// Importar los módulos de funcionalidad
import { inicializarDesplazamientoSuave } from './desplazamiento-suave.js';
import { inicializarValidacionFormulario } from './validacion-formulario.js';

/**
 * Inicializa todas las funcionalidades del sitio cuando el DOM está completamente cargado.
 */
document.addEventListener('DOMContentLoaded', () => {
    inicializarDesplazamientoSuave();
    inicializarValidacionFormulario();
});
