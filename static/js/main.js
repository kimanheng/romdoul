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
    
    // Set initial position for the circle overlay
    function setInitialCirclePosition() {
        if (menuToggle && circleOverlay) {
            const rect = menuToggle.getBoundingClientRect();
            const buttonCenterX = rect.right - (rect.width / 2);
            const buttonCenterY = rect.top + (rect.height / 2);
            
            circleOverlay.style.top = `${buttonCenterY}px`;
            circleOverlay.style.right = `${window.innerWidth - buttonCenterX}px`;
        }
    }
    
    // Call once on load
    setInitialCirclePosition();
    
    // Update position on resize
    window.addEventListener('resize', setInitialCirclePosition);
    
    if (menuToggle) {
        menuToggle.addEventListener('click', function() {
            document.body.classList.toggle('menu-open');
            
            const isExpanded = document.body.classList.contains('menu-open');
            menuToggle.setAttribute('aria-expanded', isExpanded);
            
            // Update position before expanding
            setInitialCirclePosition();
            
            if (isExpanded) {
                // Expand the circle
                circleOverlay.classList.add('expand');
                
                // Show the menu with a slight delay to match circle expansion
                setTimeout(() => {
                    mobileNav.classList.add('active');
                    document.body.style.overflow = 'hidden';
                }, 200);
            } else {
                // Hide the menu
                mobileNav.classList.remove('active');
                
                // Collapse the circle with slight delay
                setTimeout(() => {
                    circleOverlay.classList.remove('expand');
                    document.body.style.overflow = '';
                }, 100);
            }
        });
    }
});

document.body.style.overflow = 'hidden';
