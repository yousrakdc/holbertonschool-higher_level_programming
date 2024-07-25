// Select the header element
const headerElement = document.querySelector('header');

// Select the button element with the id 'red_header'
const redHeaderButton = document.getElementById('red_header');

// Add a click event listener to the redHeaderButton
redHeaderButton.addEventListener('click', function () {
  // When the button is clicked, add the 'red' class to the header element
  headerElement.classList.add('red');
});