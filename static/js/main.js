document.addEventListener('DOMContentLoaded', function() {
    const loadingScreen = document.querySelector('.loading-screen');
    
    setTimeout(function() {
        if (document.readyState === 'complete') {
            hideLoadingScreen();
        } else {
            window.addEventListener('load', hideLoadingScreen);
        }
    }, 2000);
    
    function hideLoadingScreen() {
        loadingScreen.classList.add('hidden');
        document.body.style.overflow = '';
    }
    
    const menuToggle = document.querySelector('.mobile-menu-toggle');
    const mobileNav = document.querySelector('.mobile-nav');
    
    if (menuToggle) {
        menuToggle.addEventListener('click', function() {
            document.body.classList.toggle('menu-open');
            mobileNav.classList.toggle('active');
            
            const isExpanded = mobileNav.classList.contains('active');
            menuToggle.setAttribute('aria-expanded', isExpanded);
            
            if (isExpanded) {
                document.body.style.overflow = 'hidden';
            } else {
                document.body.style.overflow = '';
            }
        });
    }
});

document.body.style.overflow = 'hidden';
