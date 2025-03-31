document.addEventListener('DOMContentLoaded', () => {
    const loadingScreen = document.getElementById('loading-screen');
    const loadingBar = document.querySelector('.loading-bar');
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const mobileNav = document.querySelector('.mobile-nav');
    const nav = document.querySelector('nav');

    setTimeout(() => { loadingBar.style.width = "30%" }, 200);
    setTimeout(() => { loadingBar.style.width = "60%" }, 600);
    setTimeout(() => { loadingBar.style.width = "100%" }, 900);
    
    setTimeout(() => {
        loadingScreen.classList.add('fade-out');
    }, 1200);
    
    mobileMenuBtn.addEventListener('click', () => {
        mobileMenuBtn.classList.toggle('open');
        mobileNav.classList.toggle('open');
        document.body.classList.toggle('menu-open');
    });
})
