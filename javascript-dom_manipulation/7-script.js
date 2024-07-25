document.addEventListener('DOMContentLoaded', () => {
    // The URL to fetch the movie data from
    const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
    
    // Select the HTML ul element with id 'list_movies'
    const moviesList = document.querySelector('#list_movies');
    
    // Use the Fetch API to get the movie data
    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.json();
        })
        .then(data => {
            // Iterate through the list of movies and create li elements for each title
            data.results.forEach(movie => {
                const listItem = document.createElement('li');
                listItem.textContent = movie.title;
                moviesList.appendChild(listItem);
            });
        })
        .catch(error => {
            // Log any errors to the console
            console.error('There has been a problem with your fetch operation:', error);
        });
});
