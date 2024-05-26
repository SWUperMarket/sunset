const burger = document.querySelector('.burger');
const navLinks = document.querySelector('.nav-links');

burger.addEventListener('click', () => {
    navLinks.classList.toggle('active');
});
document.querySelector('.logo a').addEventListener('click', function(event) {
    event.preventDefault();
    window.location.href = "mainpage.html";
});