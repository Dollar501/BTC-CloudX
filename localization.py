# localization.py
# This file handles all text strings and supports multiple languages.
LANGUAGES = {
    'ar': {
        # --- General ---
        'back_button': '🔙 رجوع',
        'app_title': 'BTC-CloudX | الاستثمار الذكي',
        'error_message': 'حدث خطأ ما، يرجى المحاولة مرة أخرى.',

        # --- Bot Menu Buttons ---
        'our_mission_button': '📄 طبيعة عملنا',
        'featured_plans_button': '📊 الخطط المميزة',
        'custom_plan_button': '💡 إنشاء خطة مخصصة',
        'contact_us_button': '📞 تواصل معنا',
        'faq_button': '❓ أسئلة شائعة',
        'privacy_button': '🛡️ الخصوصية والشفافية',
        'get_id_button': '🆔 الحصول على كود الاشتراك',
        'language_button': '🌐 اللغة',
        'open_app_button': '📱 فتح التطبيق',

        # --- Bot Content ---
        'welcome_message': 'أهلاً بك في *BTC-CloudX*، بوابتك الآمنة للاستثمار في التعدين السحابي.\n\nاستخدم الأزرار أدناه لاستكشاف خدماتنا أو افتح التطبيق لتجربة تفاعلية كاملة.',
        
        'our_mission_title': '📄 *طبيعة عملنا*',
        'our_mission_content': (
            "نحن في BTC-CloudX نؤمن بالشفافية الكاملة. ببساطة، نحن نمتلك وندير مزارع تعدين حقيقية مجهزة بأحدث وأقوى الأجهزة في العالم.\n\n"
            "عندما تستثمر معنا، فأنت لا تشتري جهازًا افتراضيًا، بل تقوم بتأجير حصة من القوة التعدينية الحقيقية (Hashrate) لهذه الأجهزة.\n\n"
            "*مهمتنا هي:* إزالة كل العوائق التقنية والتعقيدات عنك. لا داعي للقلق بشأن شراء الأجهزة، صيانتها، تبريدها، أو فواتير الكهرباء الباهظة. نحن نتولى كل ذلك، وأنت تحصل على ناتج التعدين الصافي من حصتك مباشرة إلى حسابك."
        ),

        'featured_plans_title': '📊 *الخطط السنوية المميزة*',
        'featured_plans_intro': 'هذه أفضل الخطط لدينا، مصممة بعناية لتوفر قيمة ممتازة على المدى الطويل. اختر الخطة التي تناسبك لترى تفاصيلها التقديرية.',

        'plan_details_title': '📖 تفاصيل الخطة',
        'plan_price': '💰 السعر',
        'plan_duration': '⏳ المدة',
        'plan_hashrate': '⚙️ القوة التعدينية',
        'plan_source_device': 'Source Device', # Will be translated later
        'plan_daily_fee': '💸 الرسوم اليومية',
        'plan_estimated_profit_title': '📈 الأرباح التقديرية (حسب ظروف السوق الحالية)',
        'plan_daily_profit': 'ربح اليوم',
        'plan_monthly_profit': 'ربح الشهر',
        'plan_annual_profit': 'ربح السنة',
        'profit_warning': '⚠️ *هذه الأرقام تقديرية ومتغيرة وليست ضمانًا للأرباح.*',
        'request_plan_button': '📞 طلب هذه الخطة',

        'custom_plan_intro': 'استخدم الواجهة التفاعلية لتصميم خطتك الخاصة بناءً على المبلغ والمدة التي تريدها.',

        'contact_us_title': '📞 *تواصل معنا*',
        'contact_us_content': (
            "فريقنا جاهز دائمًا لمساعدتك.\n\n"
            "🔹 **للاستفسارات العامة ومتابعة الأخبار:** انضم إلى قناتنا الرسمية.\n"
            "🔹 **لطلب خطة استثمارية أو للدعم الفني:** تواصل مباشرة مع أحد خبرائنا."
        ),
        'join_channel_button': '📢 الانضمام للقناة',
        'contact_support_button': '💬 التحدث إلى الدعم',

        'faq_title': '❓ *أسئلة شائعة*',
        'faq_intro': 'اختر سؤالاً من القائمة أدناه لعرض إجابته.',

        'privacy_title': '🛡️ *الخصوصية، الشفافية، والضمانات*',
        'privacy_content': (
            "**1. الشفافية في الأرباح:** أرباحك هي ناتج التعدين الحقيقي لحصتك مطروحًا منه رسوم الكهرباء والصيانة. كل شيء واضح وبدون رسوم خفية.\n\n"
            "**2. شهادة الاستثمار:** مع كل خطة، نصدر لك شهادة إلكترونية تحتوي على تفاصيل عقدك وكود الاشتراك الخاص بك (ID)، وهي بمثابة إثبات لحقوقك معنا.\n\n"
            "**3. خصوصية بياناتك:** نحن لا نشارك بياناتك مع أي طرف ثالث. هويتك على تليجرام هي كل ما نحتاجه لربط الاستثمار بحسابك."
        ),
        
        'get_id_title': '🆔 *كود الاشتراك الخاص بك*',
        'get_id_instructions': 'هذا هو الكود الفريد الخاص بك. استخدمه عند التواصل مع الدعم لتعريف حسابك بسرعة.',
        'your_id_is': 'الكود الخاص بك هو',

        'language_select_title': '🌐 *اختر اللغة*',
        'language_updated_message': 'تم تحديث اللغة بنجاح!',
        
        'custom_plan_confirmation': '✅ تم استلام طلبك لإنشاء خطة مخصصة بالتفاصيل التالية:',
        'custom_plan_amount': '💵 مبلغ الاستثمار',
        'custom_plan_duration': '⏳ مدة الاستثمار',
        'custom_plan_hashrate_result': 'قوة تعدينية تقديرية',
        'custom_plan_contact_prompt': 'هل تريد المتابعة وطلب هذه الخطة؟ اضغط على الزر أدناه للتواصل مع فريق الدعم.',

        'image_caption_for': 'صورة لجهاز',
    },
    'en': {
        # --- General ---
        'back_button': '🔙 Back',
        'app_title': 'BTC-CloudX | Smart Investment',
        # ... All other keys would be translated here
    },
    'zh': {
        # --- General ---
        'back_button': '🔙 返回',
        'app_title': 'BTC-CloudX | 智能投资',
        # ... All other keys would be translated here
    }
}


def get_text(key: str, lang: str) -> str:
    """Fetches a text string in the user's selected language."""
    return LANGUAGES.get(lang, LANGUAGES['ar']).get(key, f"_{key}_")