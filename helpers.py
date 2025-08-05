# helpers.py
# This file contains helper functions used across the bot.

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from localization import get_text

def build_main_menu(context: ContextTypes.DEFAULT_TYPE) -> InlineKeyboardMarkup:
    """Builds the main menu with a toggleable view."""
    is_expanded = context.user_data.get('menu_expanded', True)
    
    if is_expanded:
        keyboard = [
            [InlineKeyboardButton(get_text("main_menu_expanded", context), callback_data="toggle_menu")],
            [
                InlineKeyboardButton(get_text("custom_plan", context), callback_data="custom_plan"),
                InlineKeyboardButton(get_text("investment_plans", context), callback_data="investment_plans"),
            ],
            [
                InlineKeyboardButton(get_text("our_hardware", context), callback_data="our_hardware"),
                InlineKeyboardButton(get_text("how_it_works", context), callback_data="show_how_it_works"),
            ],
            [
                InlineKeyboardButton(get_text("why_us", context), callback_data="show_why_us"),
                InlineKeyboardButton(get_text("faq", context), callback_data="show_faq"),
            ],
            [
                InlineKeyboardButton(get_text("language", context), callback_data="select_language"),
                InlineKeyboardButton(get_text("contact_us", context), callback_data="show_contact_us")
            ]
        ]
    else:
        keyboard = [
            [InlineKeyboardButton(get_text("main_menu_collapsed", context), callback_data="toggle_menu")]
        ]
        
    return InlineKeyboardMarkup(keyboard)
