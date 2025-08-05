# data_store.py
# This file acts as the database for the bot.
# It contains all information about mining hardware and our realistic investment plans.

# Data for the high-end hardware used in the farm.
# Efficiency is in Joules per Terahash (J/TH) - lower is better.
# Hashrate is in Terahashes per second (TH/s).
# Power is in Watts.
MINING_HARDWARE = [
    {
        'id': 's21_xp', 
        'name': 'Antminer S21 XP', 
        'hashrate': 270, # TH/s
        'power': 3645,  # Watts
        'efficiency': 13.5, # J/TH
        'image': 'https://i.imgur.com/Oq10n4f.png',
        'description': 'أفضل جهاز تبريد هوائي في فئته، يجمع بين القوة والكفاءة العالية.'
    },
    {
        'id': 'm66s_plus', 
        'name': 'WhatsMiner M66S++', 
        'hashrate': 348, # TH/s
        'power': 5394, # Watts
        'efficiency': 15.5, # J/TH
        'image': 'https://i.imgur.com/u15gKgs.png',
        'description': 'جهاز قوي وموثوق يعمل بنظام التبريد بالغطس، مصمم للعمليات الصناعية الكبيرة.'
    },
    {
        'id': 's21_hydro', 
        'name': 'Antminer S21 XP Hydro', 
        'hashrate': 473, # TH/s
        'power': 5676, # Watts
        'efficiency': 12.0, # J/TH
        'image': 'https://i.imgur.com/E8w9eJ1.png',
        'description': 'الجهاز الأكثر كفاءة في العالم، يعمل بنظام تبريد مائي متقدم لتحقيق أقصى أداء وهدوء.'
    },
]

# The new, realistic annual plans based on our discussion.
# These are the plans that will be displayed on the "Featured Plans" page.
ANNUAL_PLANS = [
    {
        'id': 'pro_200',
        'name': 'العقد الاحترافي (Pro Contract)',
        'price': 200, # USD
        'duration_months': 12,
        'hashrate': 10, # TH/s
        'source_device': 'Antminer S21 XP',
        'daily_fee_usd': 0.38
    },
    {
        'id': 'advanced_500',
        'name': 'العقد المتقدم (Advanced Contract)',
        'price': 500, # USD
        'duration_months': 12,
        'hashrate': 26, # TH/s
        'source_device': 'Antminer S21 XP',
        'daily_fee_usd': 0.988
    },
    {
        'id': 'elite_1000',
        'name': 'العقد المائي للنخبة (Elite Hydro Contract)',
        'price': 1000, # USD
        'duration_months': 12,
        'hashrate': 55, # TH/s
        'source_device': 'Antminer S21 XP Hydro',
        'daily_fee_usd': 1.925
    }
]

# --- Real-world data for calculation ---
# In a real production environment, this data should be fetched periodically from a reliable API.
# For this example, we will use the realistic estimates we discussed.
BTC_PRICE_USD = 75000.0
# Daily BTC mined per 1 TH/s of hashrate
BTC_PER_TH_PER_DAY = 0.00000105

# --- FAQ Data ---
FAQ_DATA = {
    'faq_1': {
        'q': 'ما هي طبيعة الاستثمار معكم؟',
        'a': 'استثمارك معنا هو في صورة عقد إيجار لجزء من القوة التعدينية (Hashrate) الخاصة بأجهزتنا الحقيقية. أنت لا تشتري جهازًا بحد ذاته، بل تشتري قدرته على التعدين لمدة زمنية محددة، ونحن نتكفل بكل الجوانب التشغيلية من صيانة وكهرباء وتبريد.'
    },
    'faq_2': {
        'q': 'هل الأرباح ثابتة ومضمونة؟',
        'a': 'لا، الأرباح ليست ثابتة على الإطلاق، وهذا هو جوهر الشفافية في نموذجنا. تتغير الأرباح يوميًا بناءً على عاملين رئيسيين: 1. سعر عملة البيتكوين في السوق. 2. صعوبة التعدين على الشبكة العالمية. نحن نضمن لك فقط القوة التعدينية التي اشتريتها، والعائد يكون نتاج عمل هذه القوة في السوق الحقيقي.'
    },
    'faq_3': {
        'q': 'كيف أضمن حقوقي عند الاستثمار؟',
        'a': 'عند إتمام أي خطة استثمارية، يتم إصدار شهادة استثمار إلكترونية موثقة باسمك ورقم هويتك الخاص (User ID) داخل البوت. هذه الشهادة توضح بالتفصيل قيمة استثمارك، حجم القوة التعدينية، مدة العقد، وتكون بمثابة إثبات لحقوقك لدينا.'
    },
    'faq_4': {
        'q': 'ماذا يحدث بعد انتهاء مدة العقد؟',
        'a': 'قبل انتهاء مدة عقدك بفترة، سيتم إعلامك. سيكون لديك الخيار بين: 1. تجديد عقدك بنفس الشروط أو بشروط جديدة متاحة وقتها. 2. عدم التجديد، وفي هذه الحالة يتوقف تزويدك بالقوة التعدينية، ويمكنك سحب أي رصيد متبقٍ في حسابك.'
    }
}