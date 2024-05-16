/*select*/
document.addEventListener('DOMContentLoaded', function () {
    const userTypeSelect = document.getElementById('userType');
    const userTypeError = document.getElementById('userType-error');

    userTypeSelect.addEventListener('input', function () {
        validateUserType();
    });

    // Function to validate the select element
    function validateUserType() {
        const userTypeValue = userTypeSelect.value;

        if (userTypeValue === 'Select') {
            userTypeSelect.setCustomValidity('Please select a user type.');
        } else {
            userTypeSelect.setCustomValidity('');
        }
    }

    // Validate the select element on page load
    validateUserType();
});


/*phonenumber*/
 document.addEventListener('DOMContentLoaded', function () {
    document.querySelector('#phone').addEventListener('input', function (event) {
        const phoneInput = event.target;
        const phonePattern = /^\d{10}$/;

        if (!phonePattern.test(phoneInput.value)) {
            phoneInput.setCustomValidity('Please enter a valid 10-digit phone number.');
        } else {
            phoneInput.setCustomValidity('');
        }
    });
});

