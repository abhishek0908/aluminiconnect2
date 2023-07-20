document.addEventListener('DOMContentLoaded', function () {
    const readFullBtn = document.getElementById('readFullBtn');
    
    readFullBtn.addEventListener('click', function (event) {
        if (!isAuthenticated) {
            event.preventDefault(); // Prevent default link behavior

            // Redirect to the login page
            window.location.href = "{% url 'login' %}";
        }
    });
});
