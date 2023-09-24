
const accordionItems = document.querySelectorAll(".accordion-item");


accordionItems.forEach((item) => {
  const header = item.querySelector(".accordion-header");
  header.addEventListener("click", () => {
    
    item.classList.toggle("active");


    const content = item.querySelector(".accordion-content");
    if (item.classList.contains("active")) {
      content.style.maxHeight = content.scrollHeight + "px";
    } else {
      content.style.maxHeight = 0;
    }
  });
});


const searchInput = document.querySelector("#search-bar");
const searchBtn = document.querySelector("#search-btn");

searchBtn.addEventListener("click", () => {
  const searchTerm = searchInput.value.toLowerCase();

  
  accordionItems.forEach((item) => {
    const headerText = item.querySelector("h3").textContent.toLowerCase();

    if (headerText.includes(searchTerm)) {
      
      item.classList.add("active");
      const content = item.querySelector(".accordion-content");
      content.style.maxHeight = content.scrollHeight + "px";
    } else {
      
      item.classList.remove("active");
      const content = item.querySelector(".accordion-content");
      content.style.maxHeight = 0;
    }
  });
});
