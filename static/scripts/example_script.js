// Example JavaScript file

// Function to toggle navigation menu
function toggleNav() {
  const nav = document.querySelector('nav');
  nav.classList.toggle('open');
}

// Function to animate header
function animateHeader() {
  const header = document.querySelector('header');
  header.style.transform = 'translateY(0)';
  header.style.transition = 'transform 0.5s ease-in-out';
}

// Function to load data from API
function loadData() {
  const apiUrl = 'https://example.com/api/data';
  fetch(apiUrl)
   .then(response => response.json())
   .then(data => {
      const mainContent = document.querySelector('main');
      mainContent.innerHTML = '';
      data.forEach(item => {
        const element = document.createElement('div');
        element.textContent = item.name;
        mainContent.appendChild(element);
      });
    })
   .catch(error => console.error(error));
}

// Event listeners
document.addEventListener('DOMContentLoaded', () => {
  const navToggle = document.querySelector('.nav-toggle');
  navToggle.addEventListener('click', toggleNav);
  const header = document.querySelector('header');
  header.addEventListener('mouseover', animateHeader);
  loadData();
});
