addEventListener('DOMContentLoaded', function () {
    // fuction for updating text
    const updateText = () => (document.querySelector('header').innerText = 'New Header!!!');
    // get element and add eventListener
    document.querySelector('#update_header').addEventListener('click', updateText);
});
