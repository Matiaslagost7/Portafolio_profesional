// js/validacion-formulario.js

/**
 * Valida un correo electrónico usando una expresión regular.
 * @param {string} correo - El correo a validar.
 * @returns {boolean} - True si el correo es válido.
 */
function esCorreoValido(correo) {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(correo);
}

/**
 * Valida la longitud mínima de un texto.
 * @param {string} texto - El texto a validar.
 * @param {number} longitudMinima - La longitud mínima requerida.
 * @returns {boolean} - True si el texto cumple con la longitud mínima.
 */
function esTextoValido(texto, longitudMinima) {
    return texto.trim().length >= longitudMinima;
}

/**
 * Muestra un mensaje de error para un campo del formulario.
 * @param {HTMLElement} campo - El campo del formulario.
 * @param {string} mensaje - El mensaje de error a mostrar.
 */
function mostrarError(campo, mensaje) {
    campo.classList.add('is-invalid');
    campo.classList.remove('is-valid');
    const retroalimentacion = campo.nextElementSibling;
    if (retroalimentacion && retroalimentacion.classList.contains('invalid-feedback')) {
        retroalimentacion.textContent = mensaje;
    }
}

/**
 * Marca un campo como válido.
 * @param {HTMLElement} campo - El campo del formulario.
 */
function mostrarValido(campo) {
    campo.classList.remove('is-invalid');
    campo.classList.add('is-valid');
}

/**
 * Muestra un mensaje de estado (éxito o error) para el formulario.
 * @param {string} tipo - 'exito' o 'error'.
 * @param {string} texto - El mensaje a mostrar.
 * @param {HTMLElement} divMensaje - El elemento donde mostrar el mensaje.
 */
function mostrarMensajeFormulario(tipo, texto, divMensaje) {
    divMensaje.className = `mt-3 text-center alert alert-${tipo === 'exito' ? 'success' : 'danger'}`;
    divMensaje.textContent = texto;
    divMensaje.style.display = 'block';

    setTimeout(() => {
        divMensaje.style.display = 'none';
    }, 6000);
}

/**
 * Inicializa la validación y el envío AJAX del formulario de contacto.
 */
function inicializarValidacionFormulario() {
    const formularioContacto = document.getElementById('contactForm');
    if (!formularioContacto) return;

    const campoNombre = document.getElementById('nombre');
    const campoEmail = document.getElementById('email');
    const campoMensaje = document.getElementById('mensaje');
    const mensajeFormulario = document.getElementById('formMessage');
    const botonEnviar = formularioContacto.querySelector('.btn-submit') || formularioContacto.querySelector('button[type="submit"]');

    const validarCampo = (campo, longitudMinima, mensajeError, validacionEmail = false) => {
        const valor = campo.value;
        if (!esTextoValido(valor, 1)) {
            mostrarError(campo, 'Este campo es obligatorio.');
            return false;
        }
        if (validacionEmail && !esCorreoValido(valor)) {
            mostrarError(campo, 'Por favor ingresa un correo electrónico válido.');
            return false;
        }
        if (!esTextoValido(valor, longitudMinima)) {
            mostrarError(campo, mensajeError);
            return false;
        }
        mostrarValido(campo);
        return true;
    };

    campoNombre.addEventListener('blur', () => validarCampo(campoNombre, 3, 'El nombre debe tener al menos 3 caracteres.'));
    campoEmail.addEventListener('blur', () => validarCampo(campoEmail, 1, '', true));
    campoMensaje.addEventListener('blur', () => validarCampo(campoMensaje, 10, 'El mensaje debe tener al menos 10 caracteres.'));

    formularioContacto.addEventListener('submit', async (evento) => {
        evento.preventDefault();

        const esNombreValido = validarCampo(campoNombre, 3, 'El nombre debe tener al menos 3 caracteres.');
        const esEmailValido = validarCampo(campoEmail, 1, '', true);
        const esMensajeValido = validarCampo(campoMensaje, 10, 'El mensaje debe tener al menos 10 caracteres.');

        if (!esNombreValido || !esEmailValido || !esMensajeValido) {
            mostrarMensajeFormulario('error', 'Por favor corrige los errores antes de enviar.', mensajeFormulario);
            return;
        }

        botonEnviar.disabled = true;
        botonEnviar.textContent = 'Enviando...';

        const datosFormulario = new FormData(formularioContacto);
        
        try {
            const respuesta = await fetch(formularioContacto.action, {
                method: 'POST',
                body: datosFormulario,
                headers: {
                    'Accept': 'application/json'
                }
            });

            if (respuesta.ok) {
                mostrarMensajeFormulario('exito', '¡Mensaje enviado con éxito! Gracias por contactarme.', mensajeFormulario);
                formularioContacto.reset();
                [campoNombre, campoEmail, campoMensaje].forEach(campo => campo.classList.remove('is-valid', 'is-invalid'));
            } else {
                const datos = await respuesta.json();
                const mensajeError = datos.errors ? datos.errors.map(err => err.message).join(', ') : 'No se pudo enviar el mensaje.';
                mostrarMensajeFormulario('error', `Error: ${mensajeError}`, mensajeFormulario);
            }
        } catch (error) {
            mostrarMensajeFormulario('error', 'Hubo un problema con la red. Por favor, inténtalo de nuevo.', mensajeFormulario);
        } finally {
            botonEnviar.disabled = false;
            botonEnviar.textContent = 'Enviar Mensaje';
        }
    });
}

export { inicializarValidacionFormulario };
