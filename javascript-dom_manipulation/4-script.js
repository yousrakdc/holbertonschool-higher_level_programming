// Add an event listener to the document that runs when the DOM content is fully loaded
document.addEventListener('DOMContentLoaded', () => {
    // Select the button element with the id 'add_item'
    const addItemButton = document.querySelector('#add_item');
    // Select the ul element with the class 'my_list'
    const ulList = document.querySelector('ul.my_list');

    // Add a click event listener to the addItemButton
    addItemButton.addEventListener('click', () => {
        // Create a new li element
        const newItem = document.createElement('li');
        // Set the text content of the new li element to 'Item'
        newItem.textContent = 'Item';

        // Append the new li element to the ulList
        ulList.appendChild(newItem);
    });
});
