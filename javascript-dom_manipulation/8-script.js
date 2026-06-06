// Run script after the DOM is fully loaded (important since script is in <head>)
document.addEventListener("DOMContentLoaded", function () {
    fetch("https://hellosalut.stefanbohacek.com/?lang=fr")
      .then((response) => response.json())
      .then((data) => {
        // Get the element where we will display the translation
        const helloDiv = document.getElementById("hello");
  
        // Set the translated "hello"
        helloDiv.textContent = data.hello;
      })
      .catch((error) => {
        console.error("Error fetching translation:", error);
      });
  });
  