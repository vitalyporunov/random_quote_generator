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
const quotes = [
    { text: "The only way to do great work is to love what you do.", author: "Steve Jobs" },
    { text: "Life is what happens when you're busy making other plans.", author: "John Lennon" },
    { text: "Get busy living or get busy dying.", author: "Stephen King" },
];

function getRandomQuote() {
    const randomIndex = Math.floor(Math.random() * quotes.length);
    return quotes[randomIndex];
}

function displayQuote() {
    const quoteBlock = document.getElementById('quote-block');
    const quoteText = document.getElementById('quote-text');
    const quoteAuthor = document.getElementById('quote-author');

    // Add fade-out class before changing the quote
    quoteBlock.classList.add('fade-out');

    // Wait for the animation to complete before updating the quote
    setTimeout(() => {
        const quote = getRandomQuote();
        quoteText.textContent = quote.text;
        quoteAuthor.textContent = `— ${quote.author}`;
        
        // Remove fade-out class to reset for next quote
        quoteBlock.classList.remove('fade-out');
        quoteBlock.classList.add('quote'); // Add fade-in class
    }, 500); // Match this duration to the CSS animation duration
}

// Event Listeners
document.getElementById('new-quote-button').addEventListener('click', displayQuote);

// Initial quote display
displayQuote();

// Accordion Functionality
const accordionButtons = document.querySelectorAll('.accordion-button');

accordionButtons.forEach(button => {
    button.addEventListener('click', () => {
        const content = button.nextElementSibling;

        // Toggle the content visibility
        if (content.style.display === "block") {
            content.style.display = "none";
            button.classList.remove('active');
        } else {
            content.style.display = "block";
            button.classList.add('active');
        }
    });
});