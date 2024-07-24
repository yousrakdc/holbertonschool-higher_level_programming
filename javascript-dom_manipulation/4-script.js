document.addEventListener('DOMContentLoaded', () => {
    const addItemButton = document.querySelector('#add_item');
    const ulList = document.querySelector('ul.my_list');

    addItemButton.addEventListener('click', () => {
        const newItem = document.createElement('li');
        newItem.textContent = 'Item';

        ulList.appendChild(newItem);
    });
});
