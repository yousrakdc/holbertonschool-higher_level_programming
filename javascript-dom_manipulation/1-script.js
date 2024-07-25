// Define a function named redHead that sets the text color of the header element to red
const redHead = () => {
    document.querySelector('header').style.color = '#FF0000';  // Change the header text color to red (#FF0000)
};

// Add a click event listener to the button element with the id 'red_header'
// When the button is clicked, the redHead function will be executed
document.getElementById('red_header').addEventListener('click', redHead);
