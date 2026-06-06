// Wait for the DOM to be fully loaded
document.addEventListener("DOMContentLoaded", function () {
    // Get the element that will trigger the update
    const updateButton = document.getElementById("update_header");
  
    // Get the header element
    const header = document.querySelector("header");
  
    // Add click event listener
    updateButton.addEventListener("click", function () {
      header.textContent = "New Header!!!";
    });
  });