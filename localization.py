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
        "device_source": "الجهاز المصدر",
        "daily_profit": "الربح اليومي الصافي",
        "semi_annual_bonus": "عائد نصف سنوي",

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
        # General
        "welcome": "Welcome {user_mention} to *BTC-CloudX*!\n\nUse the buttons below to get started.",
        "open_app_button": "🚀 Open Full App",
        "bot_menu_button": "⚙️ Use Bot Directly",
        "main_menu_title": "Bot Main Menu. Choose an option:",
        "back_to_main_menu": "🔙 Back to Main Menu",
        "price": "Price",
        "hashrate": "Hashrate",
        "annual_profit": "Net Annual Profit",
        "device_source": "Source Device",
        "daily_profit": "Net Daily Profit",
        "semi_annual_bonus": "Semi-Annual Bonus",

        # Main Menu Buttons
        "featured_plans": "📊 Featured Plans",
        "how_it_works": "⚙️ How It Works",
        "faq": "❓ FAQ",
        "privacy_policy": "📄 Privacy & Policy",
        "get_subscription_code": "💳 Get Subscription Code",
        "contact_us": "📞 Contact Us",
        "language": "🌐 Language",

        # Sections Content
        "featured_plans_title": "Featured Investment Plans",
        "faq_title": "Select a question to see its answer:",
        "back_to_faq_menu": "🔙 Back to FAQ List",

        # Subscription Code
        "subscription_code_text": "✅ Your subscription code has been successfully created!\n\nYour code is:\n`{user_code}`\n\nKeep this code, it is your permanent identifier with us.",

        # Contact Us
        "contact_us_content": "Our team is ready to answer all your inquiries. You can contact us via:",
        "join_channel_button": "📢 Our Telegram Channel",
        "contact_support_button": "💬 Chat with Technical Support",

        # Language
        "select_language": "Select your preferred language:",
        "language_updated": "✅ Language updated to English.",

        # Web App Data Handler
        "custom_plan_result_title": "✅ Your custom plan details have been received",
        "investment_amount": "Investment Amount",
        "contract_duration": "Contract Duration",
        "calculated_hashrate": "Calculated Hashrate",
        "total_profit_estimate": "Estimated Total Net Profit",
        "plan_request_prompt": "To request this plan or discuss details, please contact technical support.",
        "close_message_button": "✖️ Close",
    },
    'zh': {
        # General
        "welcome": "欢迎 {user_mention} 来到 *BTC-CloudX*！\n\n请使用下面的按钮开始。",
        "open_app_button": "🚀 打开完整应用",
        "bot_menu_button": "⚙️ 直接使用机器人",
        "main_menu_title": "机器人主菜单。请选择一个选项：",
        "back_to_main_menu": "🔙 返回主菜单",
        "price": "价格",
        "hashrate": "算力",
        "annual_profit": "年净利润",
        "device_source": "源设备",
        "daily_profit": "日净利润",
        "semi_annual_bonus": "半年奖金",

        # Main Menu Buttons
        "featured_plans": "📊 特色计划",
        "how_it_works": "⚙️ 工作原理",
        "faq": "❓ 常见问题",
        "privacy_policy": "📄 隐私与政策",
        "get_subscription_code": "💳 获取订阅代码",
        "contact_us": "📞 联系我们",
        "language": "🌐 语言",

        # Sections Content
        "featured_plans_title": "特色投资计划",
        "faq_title": "选择一个问题以查看答案：",
        "back_to_faq_menu": "🔙 返回常见问题列表",

        # Subscription Code
        "subscription_code_text": "✅ 您的订阅代码已成功创建！\n\n您的代码是：\n`{user_code}`\n\n请保留此代码，它是您在我们这里的永久标识符。",

        # Contact Us
        "contact_us_content": "我们的团队随时准备回答您的所有问题。您可以通过以下方式联系我们：",
        "join_channel_button": "📢 我们的 Telegram 频道",
        "contact_support_button": "💬 与技术支持聊天",

        # Language
        "select_language": "请选择您的首选语言：",
        "language_updated": "✅ 语言已更新为中文。",

        # Web App Data Handler
        "custom_plan_result_title": "✅ 已收到您的自定义计划详情",
        "investment_amount": "投资金额",
        "contract_duration": "合同期限",
        "calculated_hashrate": "计算算力",
        "total_profit_estimate": "预计总净利润",
        "plan_request_prompt": "如需申请此计划或讨论详情，请联系技术支持。",
        "close_message_button": "✖️ 关闭",
    }
}

def get_text(key: str, context: ContextTypes.DEFAULT_TYPE) -> str:
    """Fetches a text string in the user's selected language."""
    lang = context.user_data.get('lang', 'ar')
    # Fallback to English if key not in selected language, then to the key name itself as a last resort.
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
    await query.answer() # Acknowledge the button press first
    
    lang_code = query.data.split('set_lang_')[1]
    context.user_data['lang'] = lang_code
    
    # Use a direct lookup to ensure the confirmation is in the newly selected language
    confirmation_text = LANGUAGES.get(lang_code, {}).get("language_updated", "Language updated.")
    await query.answer(text=confirmation_text, show_alert=True)
    
    # Redisplay the main menu with the new language
    from helpers import build_main_menu # Avoid circular import
    await query.edit_message_text(
        text=get_text('main_menu_title', context),
        reply_markup=build_main_menu(context),
        parse_mode='Markdown'
    )
