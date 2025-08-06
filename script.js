// script.js - Enhanced BTC-CloudX Web App with 3D Bitcoin Animation

// Current language state
let currentLanguage = 'ar';

// Language configuration
const LANGUAGE_CONFIG = {
    ar: { flag: '🇸🇦', name: 'العربية', dir: 'rtl' },
    en: { flag: '🇺🇸', name: 'English', dir: 'ltr' },
    zh: { flag: '🇨🇳', name: '中文', dir: 'ltr' }
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
        
        // Update language selector display
        const currentLangFlag = document.getElementById('current-lang-flag');
        const currentLangText = document.getElementById('current-lang-text');
        
        if (currentLangFlag && currentLangText) {
            currentLangFlag.textContent = LANGUAGE_CONFIG[lang].flag;
            currentLangText.textContent = LANGUAGE_CONFIG[lang].name;
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
        
        // Update navigation with specific IDs
        const navElements = {
            'nav-home': translations.nav_home,
            'nav-plans': translations.nav_plans,
            'nav-hardware': translations.nav_hardware,
            'nav-custom-plan': translations.nav_custom_plan,
            'nav-faq': translations.nav_faq
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

// Initialize everything when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    // Load saved language preference
    const savedLang = localStorage.getItem('btc-cloudx-language') || 'ar';
    
    // Initialize components
    const bitcoinAnimation = new Bitcoin3DAnimation('bitcoin-animation');
    const languageManager = new LanguageManager();
    
    // Set saved language
    languageManager.setLanguage(savedLang);
    
    // Initialize other components
    ButtonAnimations.init();
    PageNavigation.init();
    
    // Initialize Telegram WebApp if available
    if (window.Telegram && window.Telegram.WebApp) {
        window.Telegram.WebApp.ready();
        window.Telegram.WebApp.expand();
    }
    
    console.log('🚀 BTC-CloudX Enhanced Web App Initialized!');
});

// Export for global access
window.BitcoinAnimation = Bitcoin3DAnimation;
window.LanguageManager = LanguageManager;
window.currentLanguage = currentLanguage;