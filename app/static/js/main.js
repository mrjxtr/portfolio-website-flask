// Animation functions using Intersection Observer
function setupAnimations() {
    const animatedElements = document.querySelectorAll('.animate-on-scroll');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-fade-in');
            }
        });
    }, { threshold: 0.1 });

    animatedElements.forEach(element => {
        observer.observe(element);
    });
}

// Add animation classes to elements
document.addEventListener('DOMContentLoaded', function() {
    // Add animation classes to hero section
    const hero = document.querySelector('.hero-section');
    if (hero) {
        hero.classList.add('animate-on-scroll');
    }

    // Add animation classes to project cards
    const projectCards = document.querySelectorAll('.project-card');
    projectCards.forEach((card, index) => {
        card.classList.add('animate-on-scroll');
        card.style.animationDelay = `${index * 100}ms`;
    });

    // Add animation classes to testimonial cards
    const testimonialCards = document.querySelectorAll('.testimonial-card');
    testimonialCards.forEach((card, index) => {
        card.classList.add('animate-on-scroll');
        card.style.animationDelay = `${index * 100}ms`;
    });

    // Initialize animations
    setupAnimations();
}); 
