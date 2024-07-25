document.addEventListener('DOMContentLoaded', () => {
    // The URL to fetch the greeting data from
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

    // Select the HTML element with id 'hello'
    const helloElement = document.querySelector('#hello');

    // Use the Fetch API to get the greeting data
    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.json();
        })
        .then(data => {
            // Update the text content of the hello element with the fetched greeting
            helloElement.textContent = data.hello;
        })
        .catch(error => {
            // Log any errors to the console
            console.error('There has been a problem with your fetch operation:', error);
        });
});
