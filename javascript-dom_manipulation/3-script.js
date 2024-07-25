// Add an event listener to the document that runs when the DOM content is fully loaded
document.addEventListener('DOMContentLoaded', () => {
    // Select the button element with the id 'toggle_header'
    const toggleHeaderButton = document.querySelector('#toggle_header');
    
    // Select the header element
    const header = document.querySelector('header');
    
    // Add a click event listener to the toggleHeaderButton
    toggleHeaderButton.addEventListener('click', () => {
        // Check if the header has the class 'red'
        if (header.classList.contains('red')) {
            // If it has the 'red' class, remove it and add the 'green' class
            header.classList.remove('red');
            header.classList.add('green');
        } else {
            // If it does not have the 'red' class, remove the 'green' class and add the 'red' class
            header.classList.remove('green');
            header.classList.add('red');
        }
    });
});