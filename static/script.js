// script.js - Future JavaScript for interactivity
console.log('JavaScript Loaded');
// Notify when a quote is favorited
function notifyFavorite() {
    alert('Quote has been added to your favorites!');
}
document.addEventListener("DOMContentLoaded", function() {
    const toggleButton = document.getElementById('toggle-dark-mode');

    toggleButton.addEventListener('click', function() {
        document.body.classList.toggle('dark-mode');
        toggleButton.textContent = document.body.classList.contains('dark-mode') ? '🌞' : '🌙';
    });
});
