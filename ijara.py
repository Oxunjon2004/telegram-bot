import aiogram
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor

TOKEN = "6184987862:AAHTY7j7uNH3jyy_cXmNDZ9hZLtO9SsCoGg"  # O'zingizning bot tokeningizni kiriting
MY_USER_ID = 5205152968  # O'zingizning user ID'niz (faqat sizdan xabar qabul qilinadi)
GROUP_CHAT_ID = -1002103861567  # Guruh chat ID'ni kiriting

# Bot va Dispatcher yaratish
bot = aiogram.Bot(token=TOKEN)
dp = aiogram.Dispatcher(bot)

# Xabar holati uchun o'zgaruvchi
awaiting_message = False

# /start buyrug'i handleri
@dp.message_handler(commands=['start'])
async def start(message: Message):
    global awaiting_message
    if message.from_user.id == MY_USER_ID:
        awaiting_message = True  # Bot sizdan xabar kutilayotganini belgilaydi
        await message.answer("Salom! Sizdan guruhga yuborish uchun xabar kutilyapti.")
    else:
        await message.answer("Sizda bu botni ishlatish uchun ruxsat yo'q.")

@dp.message_handler(commands=['habar'])
async def habar(message: Message):
    global awaiting_message
    if message.from_user.id == MY_USER_ID:
        awaiting_message = True  # Bot sizdan xabar kutilayotganini belgilaydi
        await message.answer("Salom! Sizdan guruhga yuborish uchun xabar kutilyapti.")
    else:
        await message.answer("Sizda bu botni ishlatish uchun ruxsat yo'q.")

# Foydalanuvchi yuborgan xabarlarni qayta ishlash
@dp.message_handler()
async def handle_message(message: Message):
    global awaiting_message
    if message.from_user.id == MY_USER_ID:
        if awaiting_message:
            # Guruhga yuborish
            await bot.send_message(chat_id=GROUP_CHAT_ID, text=message.text)
            awaiting_message = False  # Xabar jo'natilgandan keyin holatni tozalash
            await message.answer("Xabaringiz guruhga yuborildi.")
        else:
            await message.answer("Sizdan hozircha hech qanday xabar kutilmayapti.")
    else:
        await message.answer("Sizda bu botni ishlatish uchun ruxsat yo'q.")

# Pollingni boshlash
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

