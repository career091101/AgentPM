// SideBiz AI - Landing Page JavaScript

// スムーズスクロール
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// フォーム送信処理
const form = document.querySelector('.signup-form');
if (form) {
    form.addEventListener('submit', function(e) {
        const button = form.querySelector('button');
        const originalText = button.textContent;
        button.textContent = '送信中...';
        button.disabled = true;
        
        // 3秒後にリセット（Formspreeが処理を完了するため）
        setTimeout(() => {
            button.textContent = '登録完了！';
            form.reset();
            
            setTimeout(() => {
                button.textContent = originalText;
                button.disabled = false;
            }, 3000);
        }, 1500);
    });
}

// スクロール時のナビゲーション背景変更
window.addEventListener('scroll', function() {
    const nav = document.querySelector('.nav');
    if (window.scrollY > 50) {
        nav.style.background = 'rgba(99, 102, 241, 0.95)';
        nav.style.backdropFilter = 'blur(10px)';
    } else {
        nav.style.background = 'transparent';
        nav.style.backdropFilter = 'none';
    }
});

// インターセクションオブザーバーでフェードインアニメーション
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// アニメーション対象の要素を監視
document.querySelectorAll('.feature, .problem-item, .benefit, .pricing-card, .faq-item').forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(20px)';
    el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
    observer.observe(el);
});

// 簡易アクセス解析
console.log('SideBiz AI - Page loaded:', new Date().toISOString());
console.log('Referrer:', document.referrer || 'Direct');
console.log('User Agent:', navigator.userAgent);
