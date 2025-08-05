# localization.py
# This file handles all text strings and supports multiple languages.

from telegram.ext import ContextTypes

LANGUAGES = {
    'ar': {
        # --- Main Menu ---
        "welcome": "أهلاً بك في *BTC-CloudX*، بوابتك الآمنة للاستثمار في التعدين السحابي.\n\nاضغط على القائمة أدناه للبدء:",
        "main_menu_expanded": "القائمة الرئيسية 🔼",
        "main_menu_collapsed": "القائمة الرئيسية 🔽",
        "custom_plan": "💡 إنشاء خطة خاصة",
        "investment_plans": "📊 الخطط الاستثمارية",
        "our_hardware": "📠 أجهزتنا الاستثمارية",
        "how_it_works": "⚙️ شرح طريقة العمل",
        "why_us": "🌟 لماذا تختارنا؟",
        "faq": "❓ أسئلة شائعة",
        "language": "🌐 اللغة",
        "contact_us": "📞 تواصل معنا",
        "back_to_main_menu": "🔙 العودة للقائمة الرئيسية",

        # --- Web App ---
        "open_plan_creator": "اضغط على الزر أدناه لفتح واجهة إنشاء الخطة التفاعلية.",
        "open_web_app_button": "🚀 افتح واجهة إنشاء الخطة",

        # --- Custom Plan Results ---
        "custom_plan_result_title": "💡 *نتائج خطتك الاستثمارية المخصصة*",
        "result_price": "💰 السعر",
        "result_devices_count": "⚙️ عدد الأجهزة",
        "result_devices_used": "🔧 الأجهزة المستخدمة",
        "result_monthly_profit_usd": "💵 الربح بالدولار (شهريًا)",
        "result_quarterly_profit_percent": "📈% الربح ربع السنوي",
        "result_annual_profit_percent": "📈% الربح السنوي",
        "result_annual_profit_usd": "💵 الربح بالدولار (سنويًا)",
        
        # --- Hardware Section ---
        "hardware_title": "📠 *أجهزتنا الاستثمارية*",
        "hardware_intro": "نحن نستخدم فقط أحدث وأقوى الأجهزة لضمان أعلى ربحية. اختر فئة لتستعرضها:",
        "show_asic": "أجهزة ASIC",
        "show_gpu": "كروت شاشة GPU",
        "profit_per_month": "الربح الشهري التقريبي",
        "price_approx": "السعر التقريبي للجهاز",
        "next_device": "التالي »",
        "prev_device": "« السابق",
        "back_to_hardware_menu": "🔙 العودة لقائمة الأجهزة",

        # --- Other sections ---
        "contact_us_title": "📞 *تواصل معنا*",
        "contact_us_content": "فريقنا جاهز للإجابة على جميع استفساراتك...",
        "join_channel_button": "🚀 الانضمام للقناة الرسمية",
        "contact_me_button": "💬 التحدث إلى خبير",
        "select_language": "اختر لغتك المفضلة:",
        "language_updated": "✅ تم تحديث اللغة بنجاح.",
        "plans_title": "📊 *الخطط الاستثمارية المتاحة*",
        "plans_intro": "اختر الفئة التي تناسب طموحك الاستثماري:",
        "monthly_plans": "🔹 الخطط الشهرية",
        "quarterly_plans": "🔸 الخطط الربع سنوية",
        "annually_plans": "🔶 الخطط السنوية",
    },
    'en': {}, # English translations can be added here
}

def get_text(key: str, context: ContextTypes.DEFAULT_TYPE) -> str:
    """Fetches a text string in the user's selected language."""
    lang = context.user_data.get('lang', 'ar')
    return LANGUAGES.get(lang, LANGUAGES['ar']).get(key, f"_{key}_")
