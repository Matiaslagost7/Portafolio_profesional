// js/form-validation.js

/**
 * Valida un correo electrónico usando una expresión regular.
 * @param {string} email - El correo a validar.
 * @returns {boolean} - True si el correo es válido.
 */
function isEmailValid(email) {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
}

/**
 * Valida la longitud mínima de un texto.
 * @param {string} text - El texto a validar.
 * @param {number} minLength - La longitud mínima requerida.
 * @returns {boolean} - True si el texto cumple con la longitud mínima.
 */
function isTextValid(text, minLength) {
    return text.trim().length >= minLength;
}

/**
 * Muestra un mensaje de error para un campo del formulario.
 * @param {HTMLElement} field - El campo del formulario.
 * @param {string} message - El mensaje de error a mostrar.
 */
function showError(field, message) {
    field.classList.add('is-invalid');
    field.classList.remove('is-valid');
    const feedback = field.nextElementSibling;
    if (feedback && feedback.classList.contains('invalid-feedback')) {
        feedback.textContent = message;
    }
}

/**
 * Marca un campo como válido.
 * @param {HTMLElement} field - El campo del formulario.
 */
function showValid(field) {
    field.classList.remove('is-invalid');
    field.classList.add('is-valid');
}

/**
 * Muestra un mensaje de estado (éxito o error) para el formulario.
 * @param {string} type - 'success' o 'error'.
 * @param {string} text - El mensaje a mostrar.
 * @param {HTMLElement} messageDiv - El elemento donde mostrar el mensaje.
 */
function showFormMessage(type, text, messageDiv) {
    messageDiv.className = `mt-3 text-center alert alert-${type === 'success' ? 'success' : 'danger'}`;
    messageDiv.textContent = text;
    messageDiv.style.display = 'block';

    setTimeout(() => {
        messageDiv.style.display = 'none';
    }, 6000);
}

/**
 * Inicializa la validación y el envío AJAX del formulario de contacto.
 */
function initFormValidation() {
    const contactForm = document.getElementById('contactForm');
    if (!contactForm) return;

    const nameField = document.getElementById('nombre');
    const emailField = document.getElementById('email');
    const messageField = document.getElementById('mensaje');
    const formMessage = document.getElementById('formMessage');
    const submitButton = contactForm.querySelector('.btn-submit');

    const validateField = (field, minLength, errorMessage, emailValidation = false) => {
        const value = field.value;
        if (!isTextValid(value, 1)) {
            showError(field, 'Este campo es obligatorio.');
            return false;
        }
        if (emailValidation && !isEmailValid(value)) {
            showError(field, 'Por favor ingresa un correo electrónico válido.');
            return false;
        }
        if (!isTextValid(value, minLength)) {
            showError(field, errorMessage);
            return false;
        }
        showValid(field);
        return true;
    };

    nameField.addEventListener('blur', () => validateField(nameField, 3, 'El nombre debe tener al menos 3 caracteres.'));
    emailField.addEventListener('blur', () => validateField(emailField, 1, '', true));
    messageField.addEventListener('blur', () => validateField(messageField, 10, 'El mensaje debe tener al menos 10 caracteres.'));

    contactForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        const isNameValid = validateField(nameField, 3, 'El nombre debe tener al menos 3 caracteres.');
        const isEmailValid = validateField(emailField, 1, '', true);
        const isMessageValid = validateField(messageField, 10, 'El mensaje debe tener al menos 10 caracteres.');

        if (!isNameValid || !isEmailValid || !isMessageValid) {
            showFormMessage('error', 'Por favor corrige los errores antes de enviar.', formMessage);
            return;
        }

        submitButton.disabled = true;
        submitButton.textContent = 'Enviando...';

        const formData = new FormData(contactForm);
        
        try {
            const response = await fetch(contactForm.action, {
                method: 'POST',
                body: formData,
                headers: {
                    'Accept': 'application/json'
                }
            });

            if (response.ok) {
                showFormMessage('success', '¡Mensaje enviado con éxito! Gracias por contactarme.', formMessage);
                contactForm.reset();
                [nameField, emailField, messageField].forEach(field => field.classList.remove('is-valid', 'is-invalid'));
            } else {
                const data = await response.json();
                const errorMessage = data.errors ? data.errors.map(err => err.message).join(', ') : 'No se pudo enviar el mensaje.';
                showFormMessage('error', `Error: ${errorMessage}`, formMessage);
            }
        } catch (error) {
            showFormMessage('error', 'Hubo un problema con la red. Por favor, inténtalo de nuevo.', formMessage);
        } finally {
            submitButton.disabled = false;
            submitButton.textContent = 'Enviar Mensaje';
        }
    });
}

export { initFormValidation };
