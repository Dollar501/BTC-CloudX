# localization.py
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes

# Add all bot text here for easy translation
LANGUAGES = {
    'ar': {
        # General
        "welcome": "أهلاً بك {user_mention} في *BTC-CloudX*!\n\nاستخدم الأزرار أدناه للبدء.",
        "open_app_button": "🚀 فتح التطبيق الكامل",
        "bot_menu_button": "⚙️ استخدام البوت مباشرة",
        "main_menu_title": "القائمة الرئيسية للبوت. اختر أحد الخيارات:",
        "back_to_main_menu": "🔙 العودة للقائمة الرئيسية",
        "price": "السعر",
        "hashrate": "القوة التعدينية",
        "annual_profit": "الربح السنوي الصافي",
        "device_source": "الجهاز المستخدم",
        "daily_profit": "الربح اليومي",
        "semi_annual_bonus": "مكافأة نصف سنوية ",




        

        
        # Main Menu Buttons
        "featured_plans": "📊 الخطط المميزة",
        "how_it_works": "⚙️ طبيعة عملنا",
        "faq": "❓ أسئلة شائعة",
        "privacy_policy": "📄 الخصوصية وسياسة العمل",
        "get_subscription_code": "💳 الحصول على كود اشتراك",
        "contact_us": "📞 تواصل معنا",
        "language": "🌐 اللغة",

        # Sections Content
        "featured_plans_title": "الخطط الاستثمارية المميزة",
        "how_it_works_text": "...", # Text is now in data_store.py
        "privacy_policy_text": "...", # Text is now in data_store.py
        "faq_title": "اختر سؤالاً لعرض إجابته:",
        "back_to_faq_menu": "🔙 العودة لقائمة الأسئلة",

        # Subscription Code
        "subscription_code_text": "✅ تم إنشاء كود الاشتراك الخاص بك بنجاح!\n\nالكود الخاص بك هو:\n`{user_code}`\n\nاحتفظ بهذا الكود، فهو معرّفك الدائم معنا.",

        # Contact Us
        "contact_us_content": "فريقنا جاهز للإجابة على جميع استفساراتك. يمكنك التواصل معنا عبر:",
        "join_channel_button": "📢 قناتنا على تليجرام",
        "contact_support_button": "💬 التحدث إلى الدعم الفني",

        # Language
        "select_language": "اختر لغتك المفضلة:",
        "language_updated": "✅ تم تحديث اللغة إلى العربية.",

        # Web App Data Handler
        "custom_plan_result_title": "✅ تم استلام تفاصيل خطتك المخصصة",
        "investment_amount": "مبلغ الاستثمار",
        "contract_duration": "مدة العقد",
        "calculated_hashrate": "القوة التعدينية المحسوبة",
        "total_profit_estimate": "إجمالي الربح الصافي التقديري",
        "plan_request_prompt": "لطلب هذه الخطة أو لمناقشة التفاصيل، يرجى التواصل مع الدعم الفني.",
        "close_message_button": "✖️ إغلاق",
    },
    'en': {
        # English translations would go here
        "welcome": "Welcome {user_mention} to *BTC-CloudX*!\n\nUse the buttons below to get started.",
        "open_app_button": "🚀 Open Full App",
        "bot_menu_button": "⚙️ Use Bot Directly",
        "language_updated": "✅ Language updated to English.",
        # ... etc
    },
    'zh': {
        # Chinese translations would go here
        "welcome": "欢迎 {user_mention}来到 *BTC-CloudX*！\n\n请使用下面的按钮开始。",
        "open_app_button": "🚀 打开完整应用",
        "bot_menu_button": "⚙️ 直接使用机器人",
        "language_updated": "✅ 语言已更新为中文。",
        # ... etc
    }
}

def get_text(key: str, context: ContextTypes.DEFAULT_TYPE) -> str:
    """Fetches a text string in the user's selected language."""
    lang = context.user_data.get('lang', 'ar')
    # Fallback to English if key not in selected language, then to key name
    return LANGUAGES.get(lang, {}).get(key, LANGUAGES.get('en', {}).get(key, f"_{key}_"))

def build_language_menu(context: ContextTypes.DEFAULT_TYPE) -> InlineKeyboardMarkup:
    """Builds the language selection menu."""
    keyboard = [
        [
            InlineKeyboardButton("🇸🇦 العربية", callback_data="set_lang_ar"),
            InlineKeyboardButton("🇬🇧 English", callback_data="set_lang_en"),
            InlineKeyboardButton("🇨🇳 中文", callback_data="set_lang_zh"),
        ],
        [InlineKeyboardButton(get_text("back_to_main_menu", context), callback_data="main_menu")]
    ]
    return InlineKeyboardMarkup(keyboard)

async def set_language_and_reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sets the user's language and shows a confirmation."""
    query = update.callback_query
    lang_code = query.data.split('set_lang_')[1]
    context.user_data['lang'] = lang_code
    
    # Use a direct lookup to ensure the confirmation is in the newly selected language
    confirmation_text = LANGUAGES.get(lang_code, {}).get("language_updated", "Language updated.")
    await query.answer(text=confirmation_text, show_alert=True)
    
    # Redisplay the main menu with the new language
    from helpers import build_main_menu # Avoid circular import
    await query.edit_message_text(
        text=get_text('main_menu_title', context),
        reply_markup=build_main_menu(context)
    )
