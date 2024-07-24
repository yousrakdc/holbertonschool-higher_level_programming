const headerElement = document.querySelector('header');
const redHeaderButton = document.getElementById('red_header');


redHeaderButton.addEventListener('click', function () {

  headerElement.classList.add('red');
});