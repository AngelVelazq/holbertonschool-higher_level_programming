addEventListener("DOMContentLoaded", function () {
    // Define the addItem function outside of the event listener
    const addItem = () => {
        const newItem = document.createElement("li");
        newItem.innerText = "Item";
        // Appending new <li> element to <ul> 'my_list'
        document.querySelector(".my_list").append(newItem);
    };

    const addItemElement = document.querySelector("#add_item");
    // Use the addItem function as an event listener
    addItemElement.addEventListener("click", addItem);
});
