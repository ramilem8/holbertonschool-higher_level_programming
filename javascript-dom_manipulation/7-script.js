// Fetch Star Wars films using Fetch API
fetch("https://swapi-api.hbtn.io/api/films/?format=json")
  .then((response) => response.json())
  .then((data) => {
    // Get the <ul> element where movies will be listed
    const list = document.getElementById("list_movies");

    // Loop through all films and create <li> elements
    data.results.forEach((film) => {
      const li = document.createElement("li");
      li.textContent = film.title;
      list.appendChild(li);
    });
  })
  .catch((error) => {
    console.error("Error fetching films:", error);
  });