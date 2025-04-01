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
    const circleOverlay = document.querySelector('.circle-overlay');
    
    if (menuToggle) {
        menuToggle.addEventListener('click', function() {
            document.body.classList.toggle('menu-open');
            
            const isExpanded = document.body.classList.contains('menu-open');
            menuToggle.setAttribute('aria-expanded', isExpanded);
            
            if (isExpanded) {
                // Position the circle origin near the menu toggle button
                const rect = menuToggle.getBoundingClientRect();
                circleOverlay.style.top = `${rect.top + rect.height/2}px`;
                circleOverlay.style.right = `${window.innerWidth - rect.right + rect.width/2}px`;
                
                // Expand the circle
                circleOverlay.classList.add('expand');
                
                // Show the menu with a slight delay to match circle expansion
                setTimeout(() => {
                    mobileNav.classList.add('active');
                    document.body.style.overflow = 'hidden';
                }, 150);
            } else {
                // Hide the menu
                mobileNav.classList.remove('active');
                
                // Collapse the circle
                setTimeout(() => {
                    circleOverlay.classList.remove('expand');
                    document.body.style.overflow = '';
                }, 100);
            }
        });
    }
});

document.body.style.overflow = 'hidden';
