document.addEventListener('DOMContentLoaded', () => {
    const updateHeaderButton = document.querySelector('#update_header');
    const header = document.querySelector('header');

    updateHeaderButton.addEventListener('click', () => {
        header.textContent = 'New Header!!!';
    });
});
