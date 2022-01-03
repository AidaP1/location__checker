
// Sliding sidebar
const toggleBtn = document.querySelector('#location-sidebar-toggle');
const sidebar = document.querySelector('#locations-sidebar');

toggleBtn.addEventListener('click', function() {
  toggleBtn.classList.toggle('is-closed');
  sidebar.classList.toggle('is-closed');
})
