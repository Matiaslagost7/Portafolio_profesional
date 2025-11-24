// js/main.js

// Importar los módulos de funcionalidad
import { initSmoothScroll } from './smooth-scroll.js';
import { initFormValidation } from './form-validation.js';

/**
 * Inicializa todas las funcionalidades del sitio cuando el DOM está completamente cargado.
 */
document.addEventListener('DOMContentLoaded', () => {
    initSmoothScroll();
    initFormValidation();
});
