// This script can handle dynamic functionality like auto-scrolling chat messages, form validation, etc.

document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    const messageList = document.querySelector('ul');

    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the default form submission

        const username = form.querySelector('input[name="username"]').value;
        const message = form.querySelector('input[name="message"]').value;

        if (username && message) {
            // Simulate adding a new message to the list (in real app, this would be handled by the backend)
            const newMessage = document.createElement('li');
            newMessage.innerHTML = `<strong>${username}:</strong> ${message} <em>${new Date().toLocaleString()}</em>`;
            messageList.appendChild(newMessage);

            // Clear the form inputs
            form.reset();
        }
    });

    // Auto-scroll the chat window to the bottom
    function scrollToBottom() {
        window.scrollTo(0, document.body.scrollHeight);
    }

    // Call scrollToBottom on page load and whenever a new message is added
    scrollToBottom();
    messageList.addEventListener('DOMNodeInserted', scrollToBottom);
});
