# main.py
# Main entry point for the Telegram bot.
# This simplified version's primary role is to launch the Web App.

import logging
import os
import json
from decimal import Decimal

from dotenv import load_dotenv
from telegram import Update, WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Import data and text strings
from data_store import MINING_HARDWARE
from localization import get_text

# --- Setup ---
load_dotenv()
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# ==============================================================================
# !! خطوة مهمة !!
# قم باستضافة ملف index.html وانسخ الرابط العام هنا.
# ==============================================================================
WEB_APP_URL = "darkcyan-manatee-795600.hostingersite.com"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a welcome message with a single button to open the Web App."""
    context.user_data.setdefault('lang', 'ar')
    
    keyboard = [[
        InlineKeyboardButton(
            get_text("open_app_button", context), # "🚀 افتح التطبيق"
            web_app=WebAppInfo(url=WEB_APP_URL)
        )
    ]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        get_text('welcome_app', context), # "أهلاً بك! اضغط على الزر أدناه..."
        reply_markup=reply_markup
    )

async def web_app_data_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Receives data ONLY from the 'Create Plan' form inside the Web App,
    calculates, and displays the results.
    """
    data = json.loads(update.effective_message.web_app_data.data)
    
    # This handler now only processes 'create_plan' submissions.
    if data.get('action') != 'create_plan':
        return

    plan_data = data['payload']
    device_type = plan_data['deviceType']
    device_id = plan_data['deviceId']
    device = next((d for d in MINING_HARDWARE[device_type] if d['id'] == device_id), None)
    
    if not device:
        await update.message.reply_text("Error: Device not found.")
        return

    quantity = int(plan_data['quantity'])
    device_price = Decimal(device['price'])
    device_profit = Decimal(device['profit'])

    # Calculations
    total_price = device_price * quantity
    monthly_profit_usd = device_profit * quantity
    annual_profit_usd = monthly_profit_usd * 12
    quarterly_profit_percent = ((monthly_profit_usd * 3) / total_price) * 100 if total_price > 0 else 0
    annual_profit_percent = (annual_profit_usd / total_price) * 100 if total_price > 0 else 0

    # Build response message
    response = f"{get_text('custom_plan_result_title', context)}\n"
    response += "-----------------------------------\n"
    response += f"*{get_text('result_price', context)}:* ${total_price:,.2f}\n"
    # ... (rest of the response text)
    
    await update.message.reply_text(text=response, parse_mode='Markdown')


def main() -> None:
    """Starts the bot."""
    BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    if not BOT_TOKEN:
        logger.error("FATAL: TELEGRAM_BOT_TOKEN not found in .env file.")
        return
    if "YOUR_WEB_APP_URL" in WEB_APP_URL:
        logger.warning("Warning: WEB_APP_URL has not been set in main.py. The bot will not work correctly.")

    application = Application.builder().token(BOT_TOKEN).build()

    # Register handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, web_app_data_handler))

    logger.info("Bot is running...")
    application.run_polling()

if __name__ == "__main__":
    main()
