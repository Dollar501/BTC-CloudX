# data_store.py
from decimal import Decimal

# Data for hardware used in plans and displayed in the app
MINING_HARDWARE = [
    {
        'id': 's21xp_hydro',
        'name': 'Antminer S21 XP Hydro',
        'efficiency': '12.0 J/TH',
        'image': 'img/antminer_s21xp_hydro.jpg'
    },
    {
        'id': 's21xp',
        'name': 'Antminer S21 XP',
        'efficiency': '13.5 J/TH',
        'image': 'img/Antminer_S21_XP_270TH.jpg'
    },
    {
        'id': 'm66s',
        'name': 'WhatsMiner M66S++',
        'efficiency': '14.0 J/TH',
        'image': 'img/WhatsMiner_M66S++.jpg'
    }
]

# Updated investment plans with semi-annual bonus
INVESTMENT_PLANS = [
    {
        'name': {
            'ar': 'العقد الاحترافي (Pro)',
            'en': '🌟 Professional Contract (Pro)',
            'zh': '🌟 专业合约 (Pro)'
        },
        'price': Decimal('200'),
        'duration_months': 12,
        'hashrate': Decimal('10'),
        'device_source': 'Antminer S21 XP',
        'daily_profit': Decimal('0.41'),
        'monthly_profit': Decimal('12.22'),
        'annual_profit': Decimal('148.73'),
        'semi_annual_bonus': Decimal('50.00')  # 25% of 200
    },
    {
        'name': {
            'ar': 'العقد المتقدم (Advanced)',
            'en': '🚀 Advanced Contract (Advanced)',
            'zh': '🚀 高级合约 (Advanced)'
        },
        'price': Decimal('500'),
        'duration_months': 12,
        'hashrate': Decimal('26'),
        'device_source': 'Antminer S21 XP',
        'daily_profit': Decimal('1.06'),
        'monthly_profit': Decimal('31.78'),
        'annual_profit': Decimal('386.71'),
        'semi_annual_bonus': Decimal('125.00')  # 25% of 500
    },
    {
        'name': {
            'ar': 'عقد النخبة المائي (Elite Hydro)',
            'en': '💎 Elite Hydro Contract (Elite Hydro)',
            'zh': '💎 精英水冷合约 (Elite Hydro)'
        },
        'price': Decimal('1000'),
        'duration_months': 12,
        'hashrate': Decimal('55'),
        'device_source': 'Antminer S21 XP Hydro',
        'daily_profit': Decimal('2.41'),
        'monthly_profit': Decimal('72.18'),
        'annual_profit': Decimal('878.19'),
        'semi_annual_bonus': Decimal('250.00')  # 25% of 1000
    }
]

# FAQ data (Question, Answer)
FAQ_DATA = [
    ("ما هي طبيعة عملكم؟", "نحن شركة BTC-CloudX، نوفر لك فرصة للاستثمار في تعدين العملات الرقمية عبر شراء قوة تعدينية (Hashrate) من مزارعنا المجهزة بأحدث الأجهزة. نحن نتولى كل شيء من صيانة وتشغيل، وأنت تحصل على الأرباح بشكل يومي."),
    ("كيف يتم حساب الأرباح والخسائر؟", "الأرباح تعتمد على القوة التعدينية التي تملكها، سعر البيتكوين الحالي، وصعوبة الشبكة. يتم خصم رسوم الكهرباء والصيانة بشكل يومي من الناتج الخام، والباقي هو ربحك الصافي. الاستثمار يحمل مخاطر تقلب الأسعار."),
    ("هل أحصل على شهادة أو إثبات؟", "نعم، عند الاشتراك في أي خطة، تحصل على شهادة استثمار رقمية تحتوي على تفاصيل عقدك، بالإضافة إلى كود اشتراك فريد (ID) خاص بك لمتابعة استثمارك."),
    ("كيف يمكنني التواصل مع الدعم؟", "يمكنك التواصل مع فريق الدعم مباشرة عبر زر \"تواصل معنا\" في البوت، أو الانضمام لقناتنا على تليجرام لمتابعة آخر الأخبار وتحديثات الأرباح.")
]

# Static informational messages with multi-language support
STATIC_MESSAGES = {
    'ar': {
        'how_it_works': """*⚙️ طبيعة عملنا في BTC-CloudX*

🚀 ببساطة، أنت لا تشتري جهاز تعدين مادي وتضعه في منزلك، بل تستثمر في قوة الحوسبة (المعروفة باسم Hashrate) التي تنتجها أجهزتنا المتطورة في مزارع التعدين الخاصة بنا.

*📋 خطوات الاستثمار:*
1. *🎯 اختيار الخطة:* اختر إحدى خططنا المميزة أو قم بإنشاء خطة مخصصة تناسب ميزانيتك.
2. *⚡ شراء القوة التعدينية:* استثمارك يترجم إلى كمية معينة من القوة التعدينية (تقاس بالـ TH/s).
3. *🔄 بدء التعدين:* نقوم فوراً بتخصيص هذه القوة لك، وتبدأ أجهزتنا بالعمل لصالحك على مدار 24 ساعة.
4. *💰 تحصيل الأرباح:* يتم إيداع أرباحك من التعدين (بالبيتكوين) في حسابك بشكل يومي بعد خصم رسوم التشغيل (كهرباء وصيانة).

✨ نحن نتكفل بكل التعقيدات التقنية، مما يتيح لك تجربة استثمارية سهلة وشفافة.
""",
        'privacy_policy': """
*📄 الخصوصية وسياسة العمل*

*💹 1. حساب الأرباح والشفافية:*
تعتمد أرباحك على 3 عوامل رئيسية: (1) مقدار القوة التعدينية التي تمتلكها، (2) سعر البيتكوين في السوق العالمي، (3) صعوبة شبكة البيتكوين. يتم تحديث هذه العوامل باستمرار. نقوم بخصم رسوم الكهرباء والصيانة اليومية بشفافية تامة من إجمالي العائد، والناتج الصافي هو ربحك.

*📜 2. شهادة الاستثمار وكود الاشتراك (ID):*
عند إتمام اشتراكك، تصدر لك شركة BTC-CloudX شهادة استثمار رقمية كإثبات لعقدك معنا. كما تحصل على كود اشتراك فريد (ID) خاص بك، والذي يستخدم لتعريفك في جميع معاملاتك ومراسلاتك مع فريق الدعم.

*⚠️ 3. المخاطر:*
الاستثمار في تعدين العملات الرقمية، مثل أي استثمار آخر، ينطوي على مخاطر، أهمها تقلبات أسعار العملات الرقمية. نحن نوفر أفضل التقنيات لزيادة الأرباح، ولكن لا نضمن أرباحًا ثابتة.

*🔒 4. أمان البيانات:*
نحن نلتزم بحماية بياناتك الشخصية ومعلومات استثمارك باستخدام أفضل معايير الأمان الرقمي.
"""
    },
    'en': {
        'how_it_works': """*⚙️ How BTC-CloudX Works*

🚀 Simply put, you don't buy a physical mining device to place in your home. Instead, you invest in computing power (known as Hashrate) generated by our advanced equipment in our specialized mining farms.

*📋 Investment Steps:*
1. *🎯 Choose Your Plan:* Select one of our premium plans or create a custom plan that fits your budget.
2. *⚡ Purchase Mining Power:* Your investment translates to a specific amount of mining power (measured in TH/s).
3. *🔄 Start Mining:* We immediately allocate this power to you, and our machines work for you 24/7.
4. *💰 Collect Profits:* Your mining profits (in Bitcoin) are deposited into your account daily after deducting operational fees (electricity and maintenance).

✨ We handle all the technical complexities, providing you with an easy and transparent investment experience.
""",
        'privacy_policy': """
*📄 Privacy Policy & Terms of Service*

*💹 1. Profit Calculation & Transparency:*
Your profits depend on 3 main factors: (1) the amount of mining power you own, (2) Bitcoin's price in the global market, (3) Bitcoin network difficulty. These factors are constantly updated. We transparently deduct daily electricity and maintenance fees from the gross return, and the net result is your profit.

*📜 2. Investment Certificate & Subscription ID:*
Upon completing your subscription, BTC-CloudX issues you a digital investment certificate as proof of your contract with us. You also receive a unique subscription ID, which is used to identify you in all your transactions and communications with our support team.

*⚠️ 3. Risks:*
Investing in cryptocurrency mining, like any other investment, involves risks, most notably cryptocurrency price volatility. We provide the best technologies to maximize profits, but we do not guarantee fixed returns.

*🔒 4. Data Security:*
We are committed to protecting your personal data and investment information using the best digital security standards.
"""
    },
    'zh': {
        'how_it_works': """*⚙️ BTC-CloudX 工作原理*

🚀 简单来说，您不需要购买物理挖矿设备放在家中。相反，您投资于我们专业挖矿农场中先进设备产生的计算能力（称为算力）。

*📋 投资步骤:*
1. *🎯 选择计划:* 选择我们的高级计划之一或创建适合您预算的自定义计划。
2. *⚡ 购买挖矿算力:* 您的投资转化为特定数量的挖矿算力（以TH/s为单位）。
3. *🔄 开始挖矿:* 我们立即为您分配这些算力，我们的机器24/7为您工作。
4. *💰 收取利润:* 您的挖矿利润（比特币）在扣除运营费用（电费和维护费）后每日存入您的账户。

✨ 我们处理所有技术复杂性，为您提供简单透明的投资体验。
""",
        'privacy_policy': """
*📄 隐私政策和服务条款*

*💹 1. 利润计算和透明度:*
您的利润取决于3个主要因素：(1) 您拥有的挖矿算力数量，(2) 比特币在全球市场的价格，(3) 比特币网络难度。这些因素会不断更新。我们透明地从总收益中扣除每日电费和维护费，净结果就是您的利润。

*📜 2. 投资证书和订阅ID:*
完成订阅后，BTC-CloudX会向您颁发数字投资证书，作为您与我们合同的证明。您还会收到一个唯一的订阅ID，用于在所有交易和与我们支持团队的沟通中识别您的身份。

*⚠️ 3. 风险:*
投资加密货币挖矿，像任何其他投资一样，涉及风险，最主要的是加密货币价格波动。我们提供最好的技术来最大化利润，但我们不保证固定回报。

*🔒 4. 数据安全:*
我们致力于使用最佳数字安全标准保护您的个人数据和投资信息。
"""
    }
}
