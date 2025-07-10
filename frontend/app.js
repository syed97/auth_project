API_URL = 123;

document.getElementById('signupForm').addEventListener('submit', async function(e) {
    e.preventDefault(); // Prevent default form submission
    
    // Get form data
    const formData = new FormData(this);
    try {
        // Show loading state
        const submitButton = this.querySelector('button[type="submit"]');
        const originalText = submitButton.textContent;
        submitButton.textContent = 'Signing up...';
        submitButton.disabled = true;
        
        // Send data to backend
        const response = await fetch(`${API_URL}/signup`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(userData)
        });
        
        const result = await response.json();
        
        if (response.ok) {
            // Success
            document.getElementById('signupMessage').innerHTML = 
                '<span style="color: green;">Account created successfully!</span>';
            this.reset(); // Clear form
        } else {
            // Error from backend
            document.getElementById('signupMessage').innerHTML = 
                '<span style="color: red;">Error: ' + (result.message || 'Signup failed') + '</span>';
        }
        
    } catch (error) {
        // Network or other error
        document.getElementById('signupMessage').innerHTML = 
            '<span style="color: red;">Network error. Please try again.</span>';
        console.error('Error:', error);
    } finally {
        // Reset button
        const submitButton = this.querySelector('button[type="submit"]');
        submitButton.textContent = originalText;
        submitButton.disabled = false;
    }
});