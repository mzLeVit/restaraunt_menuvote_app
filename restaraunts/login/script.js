// Sample user data (database usage)
const validUsers = [
    { username: 'user1', password: 'password1' },
    { username: 'user2', password: 'password2' }
];

// Handle form submission
document.getElementById('login-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the form from submitting the traditional way

    // Get the input values
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Check if the credentials are valid
    const user = validUsers.find(user => user.username === username && user.password === password);

    if (user) {
        // Successful login
        alert('Login successful!');
        // Redirect or perform any further actions
        window.location.href = 'lunch_decision.html'; // do not forget to change this if homepage is changed !
    } else {
        // Login failed
        alert('Invalid username or password. Please try again.');
    }
});
