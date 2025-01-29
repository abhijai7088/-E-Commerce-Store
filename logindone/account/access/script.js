// Toggle Password Visibility
function togglePasswordVisibility() {
    const passwordInput = document.getElementById('password');
    const confirmPasswordInput = document.getElementById('confirm-password');
    const eyeIcon = document.querySelector('.eye-icon');
    
    if (passwordInput.type === 'password') {
        passwordInput.type = 'text';
        if (confirmPasswordInput) confirmPasswordInput.type = 'text';
        eyeIcon.textContent = '🙈';
    } else {
        passwordInput.type = 'password';
        if (confirmPasswordInput) confirmPasswordInput.type = 'password';
        eyeIcon.textContent = '👁️';
    }
}

// Phone Verification (Simulated)
function verifyPhone() {
    const phoneNumber = document.getElementById('phone').value;
    if (!phoneNumber) {
        alert('Please enter a phone number.');
    } else {
        alert('Verification code sent to your phone.');
    }
}

// Google Signup (Placeholder)
function googleSignup() {
    alert('Google signup functionality not implemented.');
}
