document.addEventListener('DOMContentLoaded', () => {
    const loadingScreen = document.getElementById('loading-screen');
    const loadingBar = document.querySelector('.loading-bar');
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const mobileNav = document.querySelector('.mobile-nav');
    const mobileNavLinks = document.querySelectorAll('.mobile-nav a');

    setTimeout(() => { loadingBar.style.width = "30%" }, 200);
    setTimeout(() => { loadingBar.style.width = "60%" }, 600);
    setTimeout(() => { loadingBar.style.width = "100%" }, 900);
    
    setTimeout(() => {
        loadingScreen.classList.add('fade-out');
    }, 1200);
    
    function toggleMobileMenu() {
        mobileMenuBtn.classList.toggle('open');
        mobileNav.classList.toggle('open');
        document.body.classList.toggle('menu-open');
    }
    
    mobileMenuBtn.addEventListener('click', toggleMobileMenu);
    
    // Close mobile menu when a link is clicked
    mobileNavLinks.forEach(link => {
        link.addEventListener('click', () => {
            toggleMobileMenu();
        });
    });
})
