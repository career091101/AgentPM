// ========================================
// Analytics & Tracking
// ========================================

// Initialize tracking data
const trackingData = {
    pageViews: 0,
    scrollDepth: 0,
    sectionReached: {
        hero: false,
        problem: false,
        solution: false,
        howItWorks: false,
        pricing: false,
        caseStudies: false,
        contact: false
    },
    ctaClicks: {
        hero: 0,
        form: 0
    },
    formSubmissions: 0,
    timeOnPage: 0
};

// Track page view
trackingData.pageViews++;
const startTime = Date.now();

// Track time on page
window.addEventListener('beforeunload', () => {
    trackingData.timeOnPage = Math.floor((Date.now() - startTime) / 1000);
    console.log('Session Data:', trackingData);
    // In production, send to analytics endpoint
    // sendAnalytics(trackingData);
});

// ========================================
// Scroll Tracking
// ========================================

const sections = document.querySelectorAll('section');
const observerOptions = {
    threshold: 0.3,
    rootMargin: '0px'
};

const sectionObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const sectionId = entry.target.id;
            if (sectionId && !trackingData.sectionReached[sectionId]) {
                trackingData.sectionReached[sectionId] = true;
                console.log(`Section reached: ${sectionId}`);

                // Add animation class when section is visible
                entry.target.classList.add('animated');
            }
        }
    });
}, observerOptions);

sections.forEach(section => {
    sectionObserver.observe(section);
});

// Track scroll depth
window.addEventListener('scroll', () => {
    const windowHeight = window.innerHeight;
    const documentHeight = document.documentElement.scrollHeight;
    const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    const scrollPercentage = Math.floor((scrollTop / (documentHeight - windowHeight)) * 100);

    if (scrollPercentage > trackingData.scrollDepth) {
        trackingData.scrollDepth = scrollPercentage;
    }
});

// ========================================
// CTA Click Tracking
// ========================================

document.getElementById('cta-hero')?.addEventListener('click', (e) => {
    trackingData.ctaClicks.hero++;
    console.log('CTA Hero clicked', trackingData.ctaClicks.hero);
});

document.getElementById('cta-form')?.addEventListener('click', (e) => {
    // Form validation will handle actual submission
    console.log('CTA Form button clicked');
});

// ========================================
// Form Validation & Submission
// ========================================

const contactForm = document.getElementById('contact-form');

if (contactForm) {
    contactForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        // Get form data
        const formData = new FormData(contactForm);
        const formValues = {
            name: formData.get('name'),
            company: formData.get('company'),
            email: formData.get('email'),
            employees: formData.get('employees'),
            challenges: formData.getAll('challenge'),
            message: formData.get('message')
        };

        // Validation
        if (!validateEmail(formValues.email)) {
            alert('有効なメールアドレスを入力してください');
            return;
        }

        if (!formValues.name || !formValues.company || !formValues.employees) {
            alert('必須項目をすべて入力してください');
            return;
        }

        // Track submission
        trackingData.formSubmissions++;
        trackingData.ctaClicks.form++;
        console.log('Form submitted:', formValues);

        // Disable submit button
        const submitButton = contactForm.querySelector('button[type="submit"]');
        submitButton.disabled = true;
        submitButton.textContent = '送信中...';

        try {
            // In production, send to backend
            // const response = await fetch('/api/contact', {
            //     method: 'POST',
            //     headers: { 'Content-Type': 'application/json' },
            //     body: JSON.stringify(formValues)
            // });

            // Simulate API call
            await new Promise(resolve => setTimeout(resolve, 1000));

            // Success
            showSuccessMessage();
            contactForm.reset();
        } catch (error) {
            console.error('Form submission error:', error);
            alert('送信中にエラーが発生しました。もう一度お試しください。');
        } finally {
            submitButton.disabled = false;
            submitButton.textContent = '無料診断に申し込む';
        }
    });
}

function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

function showSuccessMessage() {
    const successDiv = document.createElement('div');
    successDiv.className = 'success-message';
    successDiv.innerHTML = `
        <div style="background-color: #10b981; color: white; padding: 1.5rem; border-radius: 0.5rem; margin-top: 1rem; text-align: center;">
            <h3 style="margin-bottom: 0.5rem;">✓ 送信完了</h3>
            <p style="margin: 0;">24時間以内に担当者からご連絡いたします。</p>
        </div>
    `;
    contactForm.appendChild(successDiv);

    // Scroll to success message
    successDiv.scrollIntoView({ behavior: 'smooth', block: 'nearest' });

    // Remove after 5 seconds
    setTimeout(() => {
        successDiv.remove();
    }, 5000);
}

// ========================================
// Smooth Scroll for Anchor Links
// ========================================

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const targetId = this.getAttribute('href');
        if (targetId === '#') return;

        const targetElement = document.querySelector(targetId);
        if (targetElement) {
            targetElement.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// ========================================
// Bar Chart Animation
// ========================================

const barBefore = document.querySelector('.bar-before');
const barCompetitor = document.querySelector('.bar-competitor');
const barAfter = document.querySelector('.bar-after');

// Animate bars when hero section is visible
const heroObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            setTimeout(() => {
                if (barBefore) barBefore.style.width = '5%';
            }, 300);
            setTimeout(() => {
                if (barCompetitor) barCompetitor.style.width = '30%';
            }, 600);
            setTimeout(() => {
                if (barAfter) barAfter.style.width = '80%';
            }, 900);
            heroObserver.disconnect();
        }
    });
}, { threshold: 0.5 });

const heroSection = document.querySelector('.hero');
if (heroSection) {
    heroObserver.observe(heroSection);
}

// ========================================
// Performance Monitoring
// ========================================

// Track page load time
window.addEventListener('load', () => {
    const loadTime = performance.now();
    console.log(`Page loaded in ${Math.floor(loadTime)}ms`);

    // In production, send to analytics
    // sendPerformanceMetric('pageLoad', loadTime);
});

// ========================================
// A/B Testing (Placeholder)
// ========================================

// Example: Test different UVP variations
function getABTestVariant() {
    // In production, use proper A/B testing tool
    const variants = ['A', 'B'];
    const variant = variants[Math.floor(Math.random() * variants.length)];

    if (variant === 'B') {
        // Variant B: Alternative UVP wording
        const heroTitle = document.querySelector('.hero-title');
        if (heroTitle) {
            heroTitle.innerHTML = `
                <span class="highlight">6ヶ月で社員の80%</span>がAIを使いこなす、<br>
                ROI達成を<span class="highlight">12ヶ月</span>で実現
            `;
        }
    }

    console.log(`A/B Test Variant: ${variant}`);
    return variant;
}

// Uncomment to enable A/B testing
// const variant = getABTestVariant();
// trackingData.abTestVariant = variant;

// ========================================
// Utility Functions
// ========================================

// Debounce function for performance
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Format number with commas
function formatNumber(num) {
    return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',');
}

// ========================================
// FAQ Toggle (if needed in future)
// ========================================

function initFAQ() {
    const faqItems = document.querySelectorAll('.faq-item');
    faqItems.forEach(item => {
        const question = item.querySelector('.faq-question');
        const answer = item.querySelector('.faq-answer');

        question?.addEventListener('click', () => {
            const isOpen = answer.style.display === 'block';
            answer.style.display = isOpen ? 'none' : 'block';
            question.classList.toggle('open');
        });
    });
}

// ========================================
// Initialize
// ========================================

document.addEventListener('DOMContentLoaded', () => {
    console.log('AI Success Accelerator LP loaded');
    console.log('Tracking initialized:', trackingData);

    // Add fade-in animation to cards
    const cards = document.querySelectorAll('.problem-card, .solution-card, .case-card, .pricing-card');
    cards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'opacity 0.5s ease, transform 0.5s ease';

        setTimeout(() => {
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, 100 * index);
    });
});

// ========================================
// Export for testing (if needed)
// ========================================

if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        validateEmail,
        trackingData,
        formatNumber
    };
}
