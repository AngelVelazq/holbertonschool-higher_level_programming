addEventListener("DOMContentLoaded", function () {
    // Using promises because of fetch...
    fetch("https://swapi-api.hbtn.io/api/films/?format=json")
        .then((response) => {
            // If status ok, return content from fetch for next .then
            if (!response.ok) {
                throw new Error("Network response was not ok");
            }
            return response.json();
        })
        .then((content) => {
            // After awaiting results, make new <li> with the movie title as text
            const movies = content.results;
            for (const movie of movies) { // Declare 'movie' with 'const'
                const li = document.createElement("li");
                li.innerText = movie.title;
                document.querySelector("#list_movies").append(li);
            }
        })
        .catch((error) => {
            console.error("Fetch error:", error);
        });
});
