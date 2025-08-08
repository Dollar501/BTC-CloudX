// script.js - Enhanced BTC-CloudX Web App with 3D Bitcoin Animation

// Current language state
let currentLanguage = 'ar';

// Language configuration
const LANGUAGE_CONFIG = {
    ar: { code: 'AR', name: 'العربية', dir: 'rtl' },
    en: { code: 'EN', name: 'English', dir: 'ltr' },
    zh: { code: 'CH', name: '中文', dir: 'ltr' }
};

// Bitcoin 3D Animation Class
class Bitcoin3DAnimation {
    constructor(containerId) {
        this.container = document.getElementById(containerId);
        this.bitcoins = [];
        this.animationId = null;
        this.init();
    }

    init() {
        this.container.style.position = 'absolute';
        this.container.style.width = '100%';
        this.container.style.height = '100%';
        this.container.style.overflow = 'hidden';
        this.container.style.pointerEvents = 'none';
        
        // Create initial bitcoins
        this.createBitcoins(15);
        this.animate();
        
        // Add new bitcoins periodically
        setInterval(() => {
            if (this.bitcoins.length < 20) {
                this.createBitcoins(1);
            }
        }, 2000);
    }

    createBitcoins(count) {
        for (let i = 0; i < count; i++) {
            const bitcoin = this.createBitcoin();
            this.bitcoins.push(bitcoin);
            this.container.appendChild(bitcoin.element);
        }
    }

    createBitcoin() {
        const element = document.createElement('div');
        element.innerHTML = '₿';
        element.style.position = 'absolute';
        element.style.fontSize = '20px';
        element.style.color = '#f7931a';
        element.style.fontWeight = 'bold';
        element.style.textShadow = '0 0 10px rgba(247, 147, 26, 0.5)';
        element.style.userSelect = 'none';
        element.style.pointerEvents = 'none';
        element.style.zIndex = '1';
        
        // Random starting position from far distance
        const startX = Math.random() * window.innerWidth;
        const startY = Math.random() * window.innerHeight;
        const startZ = Math.random() * -2000 - 1000; // Start from far back
        
        const bitcoin = {
            element: element,
            x: startX,
            y: startY,
            z: startZ,
            speedZ: Math.random() * 3 + 2, // Speed towards screen
            rotationX: Math.random() * 360,
            rotationY: Math.random() * 360,
            rotationZ: Math.random() * 360,
            rotationSpeedX: (Math.random() - 0.5) * 4,
            rotationSpeedY: (Math.random() - 0.5) * 4,
            rotationSpeedZ: (Math.random() - 0.5) * 4,
            bounceHeight: Math.random() * 50 + 20,
            bounceSpeed: Math.random() * 0.02 + 0.01,
            bouncePhase: Math.random() * Math.PI * 2,
            life: 1.0
        };
        
        return bitcoin;
    }

    animate() {
        this.bitcoins.forEach((bitcoin, index) => {
            // Move towards screen
            bitcoin.z += bitcoin.speedZ;
            
            // Rotate
            bitcoin.rotationX += bitcoin.rotationSpeedX;
            bitcoin.rotationY += bitcoin.rotationSpeedY;
            bitcoin.rotationZ += bitcoin.rotationSpeedZ;
            
            // Bounce effect
            bitcoin.bouncePhase += bitcoin.bounceSpeed;
            const bounceOffset = Math.sin(bitcoin.bouncePhase) * bitcoin.bounceHeight;
            
            // Calculate scale based on z position (perspective)
            const scale = Math.max(0.1, (bitcoin.z + 2000) / 2000);
            const opacity = Math.max(0, Math.min(1, (bitcoin.z + 1000) / 1000));
            
            // Apply transformations
            bitcoin.element.style.transform = `
                translate3d(${bitcoin.x}px, ${bitcoin.y + bounceOffset}px, 0)
                scale(${scale})
                rotateX(${bitcoin.rotationX}deg)
                rotateY(${bitcoin.rotationY}deg)
                rotateZ(${bitcoin.rotationZ}deg)
            `;
            
            bitcoin.element.style.opacity = opacity;
            bitcoin.element.style.fontSize = `${20 * scale}px`;
            
            // Remove bitcoin if it's too close or fade out
            if (bitcoin.z > 500 || opacity <= 0) {
                bitcoin.element.remove();
                this.bitcoins.splice(index, 1);
            }
        });
        
        this.animationId = requestAnimationFrame(() => this.animate());
    }

    destroy() {
        if (this.animationId) {
            cancelAnimationFrame(this.animationId);
        }
        this.bitcoins.forEach(bitcoin => bitcoin.element.remove());
        this.bitcoins = [];
    }
}

// Language Management
class LanguageManager {
    constructor() {
        this.currentLang = 'ar';
        this.init();
    }

    init() {
        // Set initial language
        this.setLanguage('ar');
        
        // Language toggle button
        const languageToggle = document.getElementById('language-toggle');
        const languageDropdown = document.getElementById('language-dropdown');
        const dropdownArrow = document.getElementById('dropdown-arrow');
        
        if (languageToggle && languageDropdown) {
            languageToggle.addEventListener('click', (e) => {
                e.stopPropagation();
                const isOpen = !languageDropdown.classList.contains('hidden');
                
                if (isOpen) {
                    languageDropdown.classList.add('hidden');
                    dropdownArrow.style.transform = 'rotate(0deg)';
                } else {
                    languageDropdown.classList.remove('hidden');
                    dropdownArrow.style.transform = 'rotate(180deg)';
                }
            });
            
            // Language options
            const langOptions = document.querySelectorAll('.lang-option');
            langOptions.forEach(option => {
                option.addEventListener('click', (e) => {
                    const lang = e.currentTarget.dataset.lang;
                    this.setLanguage(lang);
                    languageDropdown.classList.add('hidden');
                    dropdownArrow.style.transform = 'rotate(0deg)';
                });
            });
            
            // Close dropdown when clicking outside
            document.addEventListener('click', () => {
                languageDropdown.classList.add('hidden');
                dropdownArrow.style.transform = 'rotate(0deg)';
            });
        }
    }

    setLanguage(lang) {
        if (!LANG_PACK[lang]) return;
        
        this.currentLang = lang;
        currentLanguage = lang;
        
        // Update document direction
        document.documentElement.dir = LANGUAGE_CONFIG[lang].dir;
        document.documentElement.lang = lang;
        
        // Update language display
        const currentLangText = document.getElementById('current-lang-text');
        
        if (currentLangText) {
            currentLangText.textContent = LANGUAGE_CONFIG[lang].code;
        }
        
        // Update all translatable elements
        this.updateTranslations();
        
        // Save language preference
        localStorage.setItem('btc-cloudx-language', lang);
    }

    updateTranslations() {
        const translations = LANG_PACK[this.currentLang];
        
        // Update home page
        const homeTitle = document.getElementById('home-title');
        const homeSubtitle = document.getElementById('home-subtitle');
        
        if (homeTitle) homeTitle.textContent = translations.home_title;
        if (homeSubtitle) homeSubtitle.textContent = translations.home_subtitle;
        
        // Update platform elements
        const platformElements = {
            'platform-tagline': translations.platform_tagline,
            'article-title': translations.article_title,
            'article-content': translations.article_content,
            'article-note': translations.article_note,
            'enter-platform-text': translations.enter_platform_text
        };
        
        Object.keys(platformElements).forEach(elementId => {
            const element = document.getElementById(elementId);
            if (element) element.textContent = platformElements[elementId];
        });
        
        // Update coupon system elements
        const couponElements = {
            'coupon-title': translations.coupon_title,
            'reveal-coupon-text': translations.reveal_coupon_text,
            'coupon-code-label': translations.coupon_code_label,
            'rewards-title': translations.rewards_title,
            'reward-amount': translations.reward_amount,
            'reward-condition': translations.reward_condition,
            'countdown-label': translations.countdown_label,
            'days-label': translations.days_label,
            'hours-label': translations.hours_label,
            'minutes-label': translations.minutes_label
        };
        
        Object.keys(couponElements).forEach(elementId => {
            const element = document.getElementById(elementId);
            if (element) element.textContent = couponElements[elementId];
        });
        
        // Update navigation with specific IDs (both main and bottom nav)
        const navElements = {
            'nav-home': translations.nav_home,
            'nav-plans': translations.nav_plans,
            'nav-hardware': translations.nav_hardware,
            'nav-custom-plan': translations.nav_custom_plan,
            'nav-faq': translations.nav_faq,
            'nav-home-bottom': translations.nav_home,
            'nav-plans-bottom': translations.nav_plans,
            'nav-hardware-bottom': translations.nav_hardware,
            'nav-custom-plan-bottom': translations.nav_custom_plan,
            'nav-faq-bottom': translations.nav_faq
        };
        
        Object.keys(navElements).forEach(elementId => {
            const element = document.getElementById(elementId);
            if (element) element.textContent = navElements[elementId];
        });
        
        // Update page titles
        const pageTitles = {
            'plans-title': translations.plans_title,
            'hardware-title': translations.hardware_title,
            'custom-plan-title': translations.custom_plan_title,
            'faq-title': translations.faq_title
        };
        
        Object.keys(pageTitles).forEach(elementId => {
            const element = document.getElementById(elementId);
            if (element) element.textContent = pageTitles[elementId];
        });
        
        // Update form labels and buttons
        this.updateFormElements();
        
        // Re-render dynamic content with new language
        this.loadPlans();
        this.loadHardware();
        this.loadFAQ();
        
        // Reload dynamic content
        this.loadPlans();
        this.loadHardware();
        this.loadFAQ();
    }

    updateFormElements() {
        const translations = LANG_PACK[this.currentLang];
        
        // Custom plan form with specific IDs
        const formElements = {
            'amount-label': translations.custom_plan_amount_label,
            'duration-label': translations.custom_plan_duration_label,
            'year-1-label': translations.year_one,
            'year-2-label': translations.year_two,
            'year-3-label': translations.year_three,
            'year-unit': translations.year_unit
        };
        
        Object.keys(formElements).forEach(elementId => {
            const element = document.getElementById(elementId);
            if (element) element.textContent = formElements[elementId];
        });
        
        // Input placeholders and button text
        const amountInput = document.getElementById('investment_amount');
        const calculateBtn = document.getElementById('calculate-plan-btn');
        
        if (amountInput) amountInput.placeholder = translations.custom_plan_amount_placeholder;
        if (calculateBtn) calculateBtn.textContent = translations.calculate_button;
    }

    // Load investment plans dynamically
    loadPlans() {
        const translations = LANG_PACK[this.currentLang];
        const plansContainer = document.getElementById('plans-container');
        
        if (!plansContainer) return;
        
        // Sample plans data - in real app this would come from API
        const plans = [
            {
                name: 'العقد الاحترافي (Pro)',
                nameEn: 'Professional Contract (Pro)',
                nameZh: '专业合约 (Pro)',
                price: '$200',
                hashrate: '10 TH/s',
                device: 'Antminer S21 XP',
                dailyProfit: '$0.41',
                annualProfit: '$148.73',
                semiAnnualBonus: '$50.00'
            },
            {
                name: 'العقد المتقدم (Advanced)',
                nameEn: 'Advanced Contract',
                nameZh: '高级合约',
                price: '$500',
                hashrate: '26 TH/s',
                device: 'Antminer S21 XP',
                dailyProfit: '$1.06',
                annualProfit: '$386.71',
                semiAnnualBonus: '$125.00'
            },
            {
                name: 'عقد النخبة المائي (Elite Hydro)',
                nameEn: 'Elite Hydro Contract',
                nameZh: '精英水冷合约',
                price: '$1000',
                hashrate: '55 TH/s',
                device: 'Antminer S21 XP Hydro',
                dailyProfit: '$2.41',
                annualProfit: '$878.19',
                semiAnnualBonus: '$250.00'
            }
        ];
        
        plansContainer.innerHTML = '';
        
        plans.forEach(plan => {
            const planName = this.currentLang === 'ar' ? plan.name : 
                           this.currentLang === 'en' ? plan.nameEn : plan.nameZh;
            
            const planCard = document.createElement('div');
            planCard.className = 'plan-card bg-[var(--tg-theme-secondary-bg-color)] p-4 rounded-lg space-y-3';
            planCard.innerHTML = `
                <h3 class="text-xl font-bold text-center">${planName}</h3>
                <div class="grid grid-cols-2 gap-3 text-sm">
                    <div><strong>${translations.price}:</strong> ${plan.price}</div>
                    <div><strong>${translations.hashrate}:</strong> ${plan.hashrate}</div>
                    <div><strong>${translations.device}:</strong> ${plan.device}</div>
                    <div><strong>${translations.daily_profit}:</strong> ${plan.dailyProfit}</div>
                    <div class="col-span-2"><strong>${translations.annual_profit}:</strong> ${plan.annualProfit}</div>
                    <div class="col-span-2"><strong>${translations.semi_annual_bonus}:</strong> ${plan.semiAnnualBonus}</div>
                </div>
                <button class="w-full p-3 rounded-lg font-bold text-white" style="background-color: var(--tg-theme-button-color);">
                    ${translations.subscribe_now}
                </button>
            `;
            
            plansContainer.appendChild(planCard);
        });
    }

    // Load hardware information dynamically
    loadHardware() {
        const translations = LANG_PACK[this.currentLang];
        const hardwareContainer = document.getElementById('hardware-container');
        
        if (!hardwareContainer) return;
        
        const hardware = [
            {
                name: 'Antminer S21 XP Hydro',
                efficiency: '12.0 J/TH',
                image: 'img/antminer_s21xp_hydro.jpg'
            },
            {
                name: 'Antminer S21 XP',
                efficiency: '13.5 J/TH',
                image: 'img/Antminer_S21_XP_270TH.jpg'
            },
            {
                name: 'WhatsMiner M66S++',
                efficiency: '14.0 J/TH',
                image: 'img/WhatsMiner_M66S++.jpg'
            }
        ];
        
        hardwareContainer.innerHTML = '';
        
        hardware.forEach(device => {
            const hardwareCard = document.createElement('div');
            hardwareCard.className = 'hardware-card bg-[var(--tg-theme-secondary-bg-color)] p-4 rounded-lg text-center space-y-3';
            hardwareCard.innerHTML = `
                <img src="${device.image}" alt="${device.name}" class="w-full h-32 object-contain rounded-lg" onerror="this.src='data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTAwIiBoZWlnaHQ9IjEwMCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cmVjdCB3aWR0aD0iMTAwIiBoZWlnaHQ9IjEwMCIgZmlsbD0iIzMzMzMzMyIvPjx0ZXh0IHg9IjUwIiB5PSI1NSIgZm9udC1mYW1pbHk9IkFyaWFsLCBzYW5zLXNlcmlmIiBmb250LXNpemU9IjE0IiBmaWxsPSIjNjY2NjY2IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5JbWFnZTwvdGV4dD48L3N2Zz4='">
                <h3 class="text-lg font-bold">${device.name}</h3>
                <p><strong>${translations.efficiency}:</strong> ${device.efficiency}</p>
                <button class="w-full p-2 rounded-lg font-bold text-white" style="background-color: var(--tg-theme-button-color);">
                    ${translations.hardware_modal_info.substring(0, 20)}...
                </button>
            `;
            
            hardwareContainer.appendChild(hardwareCard);
        });
    }

    // Load FAQ dynamically
    loadFAQ() {
        const translations = LANG_PACK[this.currentLang];
        const faqContainer = document.getElementById('faq-container');
        
        if (!faqContainer || !translations.faq_data) return;
        
        faqContainer.innerHTML = '';
        
        translations.faq_data.forEach((faq, index) => {
            const faqItem = document.createElement('div');
            faqItem.className = 'bg-[var(--tg-theme-secondary-bg-color)] rounded-lg overflow-hidden';
            faqItem.innerHTML = `
                <button class="w-full p-4 text-left font-bold flex justify-between items-center" onclick="this.nextElementSibling.classList.toggle('hidden'); this.querySelector('span').style.transform = this.nextElementSibling.classList.contains('hidden') ? 'rotate(0deg)' : 'rotate(180deg)'">
                    ${faq.q}
                    <span class="transform transition-transform duration-200">▼</span>
                </button>
                <div class="hidden p-4 pt-0 text-gray-300">
                    ${faq.a}
                </div>
            `;
            
            faqContainer.appendChild(faqItem);
        });
    }

    getCurrentLanguage() {
        return this.currentLang;
    }
}

// Enhanced Button Animations
class ButtonAnimations {
    static init() {
        // Add hover effects to all buttons
        const buttons = document.querySelectorAll('button, .btn');
        
        buttons.forEach(button => {
            button.addEventListener('mouseenter', () => {
                button.style.transform = 'translateY(-2px)';
                button.style.boxShadow = '0 4px 12px rgba(0, 0, 0, 0.3)';
                button.style.transition = 'all 0.2s ease';
            });
            
            button.addEventListener('mouseleave', () => {
                button.style.transform = 'translateY(0)';
                button.style.boxShadow = 'none';
            });
            
            button.addEventListener('mousedown', () => {
                button.style.transform = 'translateY(1px) scale(0.98)';
            });
            
            button.addEventListener('mouseup', () => {
                button.style.transform = 'translateY(-2px)';
            });
        });
    }
}

// Page Navigation with smooth transitions
class PageNavigation {
    static init() {
        const navButtons = document.querySelectorAll('.nav-btn');
        const pages = document.querySelectorAll('.page');
        
        navButtons.forEach(button => {
            button.addEventListener('click', () => {
                const targetPageId = button.dataset.page;
                
                // Remove active class from all nav buttons and pages
                navButtons.forEach(btn => btn.classList.remove('active'));
                pages.forEach(page => page.classList.remove('active'));
                
                // Add active class to clicked button and target page
                button.classList.add('active');
                const targetPage = document.getElementById(targetPageId);
                if (targetPage) {
                    targetPage.classList.add('active');
                }
            });
        });
    }
}

// Coupon System Class
class CouponSystem {
    constructor() {
        this.rewards = [
            { amount: 10, condition: 'متاح سحبها مع استلام أرباح الشهر الثالث' },
            { amount: 15, condition: 'متاح سحبها مع استلام أرباح الشهر الثالث' },
            { amount: 20, condition: 'متاح سحبها مع استلام أرباح الشهر الثالث' },
            { amount: 25, condition: 'متاح سحبها مع استلام أرباح الشهر الثالث' },
            { amount: 30, condition: 'متاح سحبها مع استلام أرباح الشهر الثالث' },
            { amount: 'certificate', condition: 'استلام شهادة استثمارك في يدك' }
        ];
        this.init();
    }

    init() {
        const revealBtn = document.getElementById('reveal-coupon-btn');
        if (revealBtn) {
            revealBtn.addEventListener('click', () => this.revealCoupon());
        }
        
        // Check if coupon was already revealed
        const isRevealed = localStorage.getItem('coupon-revealed');
        if (isRevealed) {
            this.showCouponContent();
            this.startCountdown();
        }
    }

    generateUserCode() {
        // Simulate user ID (in real app, this would come from Telegram WebApp)
        const userId = localStorage.getItem('user-id') || this.generateUserId();
        
        // Use same logic as Python backend
        const encoder = new TextEncoder();
        const data = encoder.encode(userId);
        
        // Simple hash function to simulate SHA256
        let hash = 0;
        for (let i = 0; i < data.length; i++) {
            const char = data[i];
            hash = ((hash << 5) - hash) + char;
            hash = hash & hash; // Convert to 32-bit integer
        }
        
        const uniquePart = Math.abs(hash).toString(16).substr(0, 7).toUpperCase();
        return `BTC-X-77-${uniquePart}`;
    }

    generateUserId() {
        const userId = Math.random().toString(36).substr(2, 9);
        localStorage.setItem('user-id', userId);
        return userId;
    }

    getRandomReward() {
        const savedReward = localStorage.getItem('user-reward');
        if (savedReward) {
            return JSON.parse(savedReward);
        }
        
        // Use user ID to generate consistent random reward
        const userId = localStorage.getItem('user-id') || this.generateUserId();
        let seed = 0;
        for (let i = 0; i < userId.length; i++) {
            seed += userId.charCodeAt(i);
        }
        
        const rewardIndex = seed % this.rewards.length;
        const randomReward = this.rewards[rewardIndex];
        localStorage.setItem('user-reward', JSON.stringify(randomReward));
        return randomReward;
    }

    revealCoupon() {
        this.showCouponContent();
        this.startCountdown();
        localStorage.setItem('coupon-revealed', 'true');
        
        // Hide reveal button
        const revealBtn = document.getElementById('reveal-coupon-btn');
        if (revealBtn) {
            revealBtn.style.display = 'none';
        }
    }

    showCouponContent() {
        const couponContent = document.getElementById('coupon-content');
        const userCodeElement = document.getElementById('user-coupon-code');
        const rewardAmountElement = document.getElementById('reward-amount');
        const rewardConditionElement = document.getElementById('reward-condition');
        
        if (couponContent) {
            couponContent.classList.remove('hidden');
        }
        
        if (userCodeElement) {
            userCodeElement.textContent = this.generateUserCode();
        }
        
        const reward = this.getRandomReward();
        const currentLang = localStorage.getItem('btc-cloudx-language') || 'ar';
        const translations = LANG_PACK[currentLang];
        
        if (rewardAmountElement && rewardConditionElement) {
            if (reward.amount === 'certificate') {
                if (currentLang === 'ar') {
                    rewardAmountElement.textContent = 'مكافأة استلام شهادة استثمارك في يدك';
                    rewardConditionElement.textContent = 'شهادة رقمية معتمدة';
                } else if (currentLang === 'en') {
                    rewardAmountElement.textContent = 'Investment Certificate Reward';
                    rewardConditionElement.textContent = 'Certified digital certificate';
                } else if (currentLang === 'zh') {
                    rewardAmountElement.textContent = '投资证书奖励';
                    rewardConditionElement.textContent = '认证数字证书';
                }
            } else {
                if (currentLang === 'ar') {
                    rewardAmountElement.textContent = `مكافأة ${reward.amount}$ أسبوعياً`;
                    rewardConditionElement.textContent = reward.condition;
                } else if (currentLang === 'en') {
                    rewardAmountElement.textContent = `$${reward.amount} Weekly Reward`;
                    rewardConditionElement.textContent = 'Available for withdrawal with third month profits';
                } else if (currentLang === 'zh') {
                    rewardAmountElement.textContent = `每周${reward.amount}美元奖励`;
                    rewardConditionElement.textContent = '可在第三个月利润中提取';
                }
            }
        }
    }

    startCountdown() {
        // Get or set countdown end time (30 days from first reveal)
        let countdownEnd = localStorage.getItem('countdown-end');
        if (!countdownEnd) {
            countdownEnd = Date.now() + (30 * 24 * 60 * 60 * 1000); // 30 days
            localStorage.setItem('countdown-end', countdownEnd);
        } else {
            countdownEnd = parseInt(countdownEnd);
        }

        const updateCountdown = () => {
            const now = Date.now();
            const timeLeft = countdownEnd - now;

            if (timeLeft <= 0) {
                // Reset countdown for next month
                const newCountdownEnd = Date.now() + (30 * 24 * 60 * 60 * 1000);
                localStorage.setItem('countdown-end', newCountdownEnd);
                this.startCountdown();
                return;
            }

            const days = Math.floor(timeLeft / (1000 * 60 * 60 * 24));
            const hours = Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));

            const daysElement = document.getElementById('days-count');
            const hoursElement = document.getElementById('hours-count');
            const minutesElement = document.getElementById('minutes-count');

            if (daysElement) daysElement.textContent = days.toString().padStart(2, '0');
            if (hoursElement) hoursElement.textContent = hours.toString().padStart(2, '0');
            if (minutesElement) minutesElement.textContent = minutes.toString().padStart(2, '0');
        };

        // Update immediately and then every minute
        updateCountdown();
        setInterval(updateCountdown, 60000);
    }
}

// Page Navigation Class
class PageNavigation {
    constructor() {
        this.currentPage = 'home-page';
    }

    init() {
        // Show home page by default
        this.showPage('home-page');
    }

    showPage(pageId) {
        // Hide all pages
        const pages = document.querySelectorAll('.page');
        pages.forEach(page => {
            page.classList.remove('active');
            page.style.display = 'none';
        });

        // Show selected page
        const targetPage = document.getElementById(pageId);
        if (targetPage) {
            targetPage.style.display = 'block';
            targetPage.classList.add('active');
            this.currentPage = pageId;
            
            // Scroll to top
            window.scrollTo(0, 0);
            
            console.log(`Navigated to: ${pageId}`);
        } else {
            console.error(`Page not found: ${pageId}`);
        }
    }

    getCurrentPage() {
        return this.currentPage;
    }
}

// Initialize everything when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    // Load saved language preference
    const savedLang = localStorage.getItem('btc-cloudx-language') || 'ar';
    
    // Initialize components
    const bitcoin3D = new Bitcoin3DAnimation('bitcoin-animation');
    const languageManager = new LanguageManager();
    const buttonAnimations = new ButtonAnimations();
    const pageNavigation = new PageNavigation();
    const couponSystem = new CouponSystem();
    
    // Set initial language
    languageManager.setLanguage(savedLang);
    
    // Initialize button animations
    buttonAnimations.init();
    
    // Initialize page navigation
    pageNavigation.init();
    
    // Enhanced navigation button functionality with creative animation
    const navButtons = document.querySelectorAll('.nav-btn-bottom');
    navButtons.forEach(button => {
        // Remove any existing listeners to prevent duplicates
        button.removeEventListener('click', handleNavClick);
        button.addEventListener('click', handleNavClick);
    });
    
    function handleNavClick(e) {
        e.preventDefault();
        e.stopPropagation();
        
        const button = e.currentTarget;
        const page = button.getAttribute('data-page');
        
        if (page) {
            try {
                // Remove active class from all buttons
                navButtons.forEach(btn => {
                    btn.classList.remove('active');
                    // Remove any existing Bitcoin icons
                    const existingIcon = btn.querySelector('.bitcoin-click-icon');
                    if (existingIcon) {
                        existingIcon.remove();
                    }
                });
                
                // Add active class to clicked button
                button.classList.add('active');
                
                // Add creative Bitcoin animation
                addBitcoinClickAnimation(button);
                
                // Show the page
                pageNavigation.showPage(page);
                
                console.log(`Navigation clicked: ${page}`);
            } catch (error) {
                console.error('Navigation error:', error);
            }
        }
    }
    
    // Function to add Bitcoin click animation
    function addBitcoinClickAnimation(button) {
        // Create Bitcoin icon element
        const bitcoinIcon = document.createElement('div');
        bitcoinIcon.className = 'bitcoin-click-icon absolute top-1 right-1 w-6 h-6 bg-gradient-to-r from-orange-400 to-yellow-500 rounded-full flex items-center justify-center shadow-lg animate-pulse';
        bitcoinIcon.innerHTML = '<span class="text-xs font-bold text-white">₿</span>';
        
        // Make button relative if not already
        button.style.position = 'relative';
        
        // Add the icon to the button
        button.appendChild(bitcoinIcon);
        
        // Add desktop arrow animation if on desktop
        if (window.innerWidth > 768) {
            addDesktopArrowAnimation(button);
        }
        
        // Remove the icon after animation
        setTimeout(() => {
            if (bitcoinIcon.parentNode) {
                bitcoinIcon.remove();
            }
        }, 3000);
    }
    
    // Function to add desktop arrow animation
    function addDesktopArrowAnimation(button) {
        const arrow = document.createElement('div');
        arrow.className = 'desktop-arrow absolute -top-8 left-1/2 transform -translate-x-1/2 text-orange-400 text-xl animate-bounce';
        arrow.innerHTML = '↑';
        
        button.appendChild(arrow);
        
        // Remove arrow after animation
        setTimeout(() => {
            if (arrow.parentNode) {
                arrow.remove();
            }
        }, 2000);
    }
    
    // Add enter platform button functionality with maintenance message
    const enterPlatformBtn = document.getElementById('enter-platform-btn');
    if (enterPlatformBtn) {
        enterPlatformBtn.addEventListener('click', () => {
            // Show maintenance message
            const message = languageManager.getCurrentLanguage() === 'ar' ? 
                'منصة التعدين السحابية في حاجة للمعالجة الآن حرصاً على أموالكم. نحن نعمل على تحسين الأمان والأداء لضمان أفضل تجربة استثمارية لعملائنا الكرام.\n\n💡 سيتم إشعاركم بانتهاء أعمال الصيانة قريباً' :
                languageManager.getCurrentLanguage() === 'en' ?
                'The cloud mining platform needs maintenance now to protect your funds. We are working on improving security and performance to ensure the best investment experience for our valued customers.\n\n💡 You will be notified when maintenance is complete soon' :
                '云挖矿平台现在需要维护以保护您的资金。我们正在努力改善安全性和性能，以确保为我们尊贵的客户提供最佳的投资体验。\n\n💡 维护完成后我们会尽快通知您';
            
            alert(message);
        });
    }
    
    // Add back button functionality with improved error handling
    const backButtons = document.querySelectorAll('.back-btn');
    backButtons.forEach(button => {
        button.removeEventListener('click', handleBackClick);
        button.addEventListener('click', handleBackClick);
    });
    
    function handleBackClick(e) {
        e.preventDefault();
        e.stopPropagation();
        
        const button = e.currentTarget;
        const targetPage = button.getAttribute('data-page');
        
        if (targetPage) {
            try {
                pageNavigation.showPage(targetPage);
                console.log(`Back button clicked: ${targetPage}`);
            } catch (error) {
                console.error('Back button error:', error);
                // Fallback to home page
                pageNavigation.showPage('home-page');
            }
        }
    }
    
    // Add touch event support for better mobile responsiveness
    function addTouchSupport() {
        const touchElements = document.querySelectorAll('.nav-btn-bottom, .back-btn, button');
        touchElements.forEach(element => {
            // Add touch feedback
            element.addEventListener('touchstart', function(e) {
                this.style.transform = 'scale(0.95)';
                this.style.transition = 'transform 0.1s ease';
            });
            
            element.addEventListener('touchend', function(e) {
                this.style.transform = 'scale(1)';
            });
            
            element.addEventListener('touchcancel', function(e) {
                this.style.transform = 'scale(1)';
            });
        });
    }
    
    // Initialize touch support
    addTouchSupport();
    // --- منصة التعدين Modal ---
    const openPlatformBtn = document.getElementById('open-platform-btn');
    const platformModal = document.getElementById('platform-modal');
    const closePlatformModal = document.getElementById('close-platform-modal');
    if (openPlatformBtn && platformModal && closePlatformModal) {
        openPlatformBtn.addEventListener('click', () => {
            platformModal.classList.remove('hidden');
            document.body.style.overflow = 'hidden';
        });
        closePlatformModal.addEventListener('click', () => {
            platformModal.classList.add('hidden');
            document.body.style.overflow = '';
        });
        // إغلاق عند الضغط خارج المحتوى
        platformModal.addEventListener('click', (e) => {
            if (e.target === platformModal) {
                platformModal.classList.add('hidden');
                document.body.style.overflow = '';
            }
        });
    }
    
    console.log('🚀 BTC-CloudX Enhanced Web App Initialized!');
});

// Export for global access
window.BitcoinAnimation = Bitcoin3DAnimation;
window.LanguageManager = LanguageManager;
window.currentLanguage = currentLanguage;