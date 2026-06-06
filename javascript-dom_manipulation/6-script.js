// Fetch Star Wars character data using Fetch API
fetch("https://swapi-api.hbtn.io/api/people/5/?format=json")
  .then((response) => response.json())
  .then((data) => {
    // Get the element where we will display the name
    const characterDiv = document.getElementById("character");

    // Insert the character name into the HTML
    characterDiv.textContent = data.name;
  })
  .catch((error) => {
    console.error("Error fetching character:", error);
  });