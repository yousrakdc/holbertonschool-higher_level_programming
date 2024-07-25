// Add an event listener to the document that runs when the DOM content is fully loaded
document.addEventListener('DOMContentLoaded', () => {
    // Select the button element with the id 'update_header'
    const updateHeaderButton = document.querySelector('#update_header');
    // Select the header element
    const header = document.querySelector('header');

    // Add a click event listener to the updateHeaderButton
    updateHeaderButton.addEventListener('click', () => {
        // Change the text content of the header element when the button is clicked
        header.textContent = 'New Header!!!';
    });
});
