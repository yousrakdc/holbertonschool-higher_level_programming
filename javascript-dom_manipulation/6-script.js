document.addEventListener('DOMContentLoaded', () => {
    // The URL to fetch the character data from
    const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
    
    // Select the HTML element with id 'character'
    const characterElement = document.querySelector('#character');
    
    // Use the Fetch API to get the character data
    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.json();
        })
        .then(data => {
            // Update the text content of the character element with the fetched name
            characterElement.textContent = data.name;
        })
        .catch(error => {
            // Log any errors to the console
            console.error('There has been a problem with your fetch operation:', error);
        });
});
