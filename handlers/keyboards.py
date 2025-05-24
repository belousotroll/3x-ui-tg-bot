from telebot import types

def make_user_keyboard() -> types.InlineKeyboardMarkup:
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton(text="📱 Получить QR-код", callback_data="get_qr"))
    kb.add(types.InlineKeyboardButton(text="ℹ️ Информация об учётной записи", callback_data="get_info"))
    return kb

def make_approve_management_keyboard(user_id: int) -> types.InlineKeyboardMarkup:
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton(text="✅ Одобрить", callback_data=f"approve:{user_id}"))
    kb.add(types.InlineKeyboardButton(text="❌ Отклонить", callback_data=f"reject:{user_id}"))
    return kb
