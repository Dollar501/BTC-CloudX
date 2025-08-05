# main.py
import logging
import os
import json
import random
import string
from telegram import Update, WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler

# Import data and text strings
from data_store import MINING_HARDWARE, ANNUAL_PLANS, FAQ_DATA, BTC_PRICE_USD, BTC_PER_TH_PER_DAY
from localization import get_text

# --- Configuration ---
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

# IMPORTANT: Replace with your actual Web App URL
WEB_APP_URL = "https://darkcyan-manatee-795600.hostingersite.com/" 
# IMPORTANT: Replace with your actual Telegram Channel and Support links
TELEGRAM_CHANNEL_LINK = "https://t.me/BTCCloudX"
TELEGRAM_SUPPORT_LINK = "https://t.me/BTC_CloudX"


# --- Helper Functions ---
def get_user_lang(context: ContextTypes.DEFAULT_TYPE) -> str:
    """Gets user's language, defaults to Arabic."""
    return context.user_data.get('lang', 'ar')


# --- Main Menu Builder ---
def build_main_menu(lang: str) -> InlineKeyboardMarkup:
    """Builds the main menu with the new structure."""
    keyboard = [
        [InlineKeyboardButton(get_text('our_mission_button', lang), callback_data='show_our_mission')],
        [InlineKeyboardButton(get_text('featured_plans_button', lang), callback_data='show_featured_plans')],
        [InlineKeyboardButton(get_text('custom_plan_button', lang), web_app=WebAppInfo(url=WEB_APP_URL + "?page=create-plan-page"))],
        [
            InlineKeyboardButton(get_text('contact_us_button', lang), callback_data='show_contact_us'),
            InlineKeyboardButton(get_text('faq_button', lang), callback_data='show_faq')
        ],
        [
            InlineKeyboardButton(get_text('privacy_button', lang), callback_data='show_privacy'),
            InlineKeyboardButton(get_text('get_id_button', lang), callback_data='get_user_id')
        ],
        [
            InlineKeyboardButton(get_text('language_button', lang), callback_data='select_language'),
            InlineKeyboardButton(get_text('open_app_button', lang), web_app=WebAppInfo(url=WEB_APP_URL))
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

# --- Command Handlers (START) ---
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handles the /start command and displays the main menu."""
    context.user_data.setdefault('lang', 'ar')
    lang = get_user_lang(context)
    
    welcome_message = get_text('welcome_message', lang)
    reply_markup = build_main_menu(lang)
    
    if update.callback_query:
        await update.callback_query.answer()
        await update.callback_query.edit_message_text(
            text=welcome_message,
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )
    else:
        await update.message.reply_markdown(
            welcome_message,
            reply_markup=reply_markup
        )

# --- Callback Query Handlers (Bot Buttons) ---
async def show_our_mission(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    lang = get_user_lang(context)
    text = f"{get_text('our_mission_title', lang)}\n\n{get_text('our_mission_content', lang)}"
    keyboard = [[InlineKeyboardButton(get_text('back_button', lang), callback_data='main_menu')]]
    await query.edit_message_text(text=text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')

async def show_featured_plans(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    lang = get_user_lang(context)
    
    # Calculate estimated profits for display
    response_text = f"{get_text('featured_plans_title', lang)}\n\n{get_text('featured_plans_intro', lang)}\n"
    response_text += "-----------------------------------\n\n"

    for plan in ANNUAL_PLANS:
        daily_gross_profit = plan['hashrate'] * BTC_PER_TH_PER_DAY * BTC_PRICE_USD
        daily_net_profit = daily_gross_profit - plan['daily_fee_usd']
        annual_net_profit = daily_net_profit * 365

        response_text += f"*{plan['name']}*\n"
        response_text += f"*{get_text('plan_price', lang)}:* ${plan['price']}\n"
        response_text += f"*{get_text('plan_hashrate', lang)}:* {plan['hashrate']} TH/s\n"
        response_text += f"*{get_text('plan_annual_profit', lang)}:* ~${annual_net_profit:,.2f}\n"
        response_text += "-----------------------------------\n"
    
    response_text += get_text('profit_warning', lang)
    
    keyboard = [[InlineKeyboardButton(get_text('back_button', lang), callback_data='main_menu')]]
    await query.edit_message_text(text=response_text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')

async def show_contact_us(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    lang = get_user_lang(context)
    text = f"{get_text('contact_us_title', lang)}\n\n{get_text('contact_us_content', lang)}"
    keyboard = [
        [InlineKeyboardButton(get_text('join_channel_button', lang), url=TELEGRAM_CHANNEL_LINK)],
        [InlineKeyboardButton(get_text('contact_support_button', lang), url=TELEGRAM_SUPPORT_LINK)],
        [InlineKeyboardButton(get_text('back_button', lang), callback_data='main_menu')]
    ]
    await query.edit_message_text(text=text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')

async def show_faq(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    lang = get_user_lang(context)
    keyboard = [
        [InlineKeyboardButton(FAQ_DATA[key]['q'], callback_data=f"faq_{key}")] for key in FAQ_DATA
    ]
    keyboard.append([InlineKeyboardButton(get_text('back_button', lang), callback_data='main_menu')])
    await query.edit_message_text(
        text=f"{get_text('faq_title', lang)}\n\n{get_text('faq_intro', lang)}",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode='Markdown'
    )
    
async def show_faq_answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    faq_key = query.data.split('faq_')[1]
    lang = get_user_lang(context)
    
    question = FAQ_DATA[faq_key]['q']
    answer = FAQ_DATA[faq_key]['a']
    
    text = f"❓ *{question}*\n\n{answer}"
    keyboard = [[InlineKeyboardButton(get_text('back_button', lang), callback_data='show_faq')]]
    
    await query.edit_message_text(text=text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')

async def show_privacy(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    lang = get_user_lang(context)
    text = f"{get_text('privacy_title', lang)}\n\n{get_text('privacy_content', lang)}"
    keyboard = [[InlineKeyboardButton(get_text('back_button', lang), callback_data='main_menu')]]
    await query.edit_message_text(text=text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')

async def get_user_id(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    user = query.from_user
    lang = get_user_lang(context)

    # Check if user already has an ID
    if 'user_btc_id' in context.user_data:
        user_id_code = context.user_data['user_btc_id']
    else:
        # Generate a new persistent ID
        random_part = ''.join(random.choices(string.digits, k=7))
        user_id_code = f"BTC-77{random_part}"
        context.user_data['user_btc_id'] = user_id_code

    text = f"{get_text('get_id_title', lang)}\n\n{get_text('get_id_instructions', lang)}\n\n`{user_id_code}`"
    keyboard = [[InlineKeyboardButton(get_text('back_button', lang), callback_data='main_menu')]]
    await query.edit_message_text(text=text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')
    
async def select_language(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    lang = get_user_lang(context)
    keyboard = [
        [InlineKeyboardButton("🇸🇦 العربية", callback_data="set_lang_ar")],
        [InlineKeyboardButton("🇬🇧 English", callback_data="set_lang_en")],
        [InlineKeyboardButton("🇨🇳 中文", callback_data="set_lang_zh")],
        [InlineKeyboardButton(get_text('back_button', lang), callback_data='main_menu')]
    ]
    await query.edit_message_text(text=get_text('language_select_title', lang), reply_markup=InlineKeyboardMarkup(keyboard))
    
async def set_language(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    lang_code = query.data.split('set_lang_')[1]
    context.user_data['lang'] = lang_code
    await query.answer(get_text('language_updated_message', lang_code))
    await start_command(update, context)


# --- Web App Data Handler ---
async def web_app_data_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Receives and processes data from the Web App."""
    try:
        data = json.loads(update.effective_message.web_app_data.data)
        action = data.get('action')
        payload = data.get('payload')
        lang = get_user_lang(context)

        if action == 'show_device_image':
            device_id = payload['device_id']
            device = next((d for d in MINING_HARDWARE if d['id'] == device_id), None)
            if device:
                caption = f"*{get_text('image_caption_for', lang)}: {device['name']}*\n\n{device['description']}"
                await update.message.reply_photo(photo=device['image'], caption=caption, parse_mode='Markdown')

        elif action == 'show_faq_answer':
            faq_id = payload['faq_id']
            faq_item = FAQ_DATA.get(faq_id)
            if faq_item:
                text = f"❓ *{faq_item['q']}*\n\n{faq_item['a']}"
                await update.message.reply_markdown(text)
        
        elif action == 'confirm_custom_plan':
            text = (
                f"{get_text('custom_plan_confirmation', lang)}\n"
                "-----------------------------------\n"
                f"*{get_text('custom_plan_amount', lang)}:* ${float(payload['amount']):,.2f}\n"
                f"*{get_text('custom_plan_duration', lang)}:* {payload['duration']} سنة/سنوات\n"
                f"*{get_text('custom_plan_hashrate_result', lang)}:* {payload['hashrate']} TH/s\n"
                "-----------------------------------\n"
                f"*{get_text('plan_annual_profit', lang)}:* ~${float(payload['total_profit']):,.2f} (لكامل المدة)\n\n"
                f"{get_text('custom_plan_contact_prompt', lang)}"
            )
            keyboard = [[InlineKeyboardButton(get_text('contact_support_button', lang), url=TELEGRAM_SUPPORT_LINK)]]
            await update.message.reply_markdown(text, reply_markup=InlineKeyboardMarkup(keyboard))

    except (json.JSONDecodeError, KeyError) as e:
        logger.error(f"Error processing Web App data: {e}")
        await update.message.reply_text(get_text('error_message', get_user_lang(context)))


def main() -> None:
    """Starts the bot."""
    BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    if not BOT_TOKEN:
        logger.error("FATAL: TELEGRAM_BOT_TOKEN not found in .env or environment variables.")
        return
    if "your-actual-web-app-url" in WEB_APP_URL:
        logger.warning("Warning: WEB_APP_URL has not been set in main.py. The Web App will not work correctly.")

    application = Application.builder().token(BOT_TOKEN).build()

    # --- Register handlers ---
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CallbackQueryHandler(start_command, pattern='^main_menu$'))
    
    # Bot menu buttons
    application.add_handler(CallbackQueryHandler(show_our_mission, pattern='^show_our_mission$'))
    application.add_handler(CallbackQueryHandler(show_featured_plans, pattern='^show_featured_plans$'))
    application.add_handler(CallbackQueryHandler(show_contact_us, pattern='^show_contact_us$'))
    application.add_handler(CallbackQueryHandler(show_faq, pattern='^show_faq$'))
    application.add_handler(CallbackQueryHandler(show_privacy, pattern='^show_privacy$'))
    application.add_handler(CallbackQueryHandler(get_user_id, pattern='^get_user_id$'))
    
    # FAQ answer handler
    application.add_handler(CallbackQueryHandler(show_faq_answer, pattern='^faq_'))

    # Language handlers
    application.add_handler(CallbackQueryHandler(select_language, pattern='^select_language$'))
    application.add_handler(CallbackQueryHandler(set_language, pattern='^set_lang_'))

    # Web App data handler
    application.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, web_app_data_handler))

    logger.info("Bot is running...")
    application.run_polling()

if __name__ == "__main__":
    main()