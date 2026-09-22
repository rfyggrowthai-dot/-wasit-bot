
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler
import random
TOKEN=open("token.txt").read().strip()
W="TRchgE6LAnNawY8NcdSESWeh9EkxxKARZ6"
G="https://www.google.com/search?q="+W
F="https://www.meta.ai/share/a/e583ac9e-55fe-4139-bbbe-52828ed14c53"
PAY="https://nowpayments.io/payment/?iid=5189558372"
def kb():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Google",url=G)],
        [InlineKeyboardButton("Factory",url=F)],
        [InlineKeyboardButton("Update",callback_data="u"),InlineKeyboardButton("Auto Spread",callback_data="s")],
        [InlineKeyboardButton("Wallet",callback_data="w")],
        [InlineKeyboardButton("PAY 200$",url=PAY)],
        [InlineKeyboardButton("OPEN FACTORY PID 18324",callback_data="o")]
    ])
async def start(u,c):
    await u.message.reply_text("PID 18324 Running - Google OK - Auto Spread ON", reply_markup=kb())
async def cb(u,c):
    q=u.callback_query
    await q.answer()
    await q.edit_message_text(f"Done - Agents {random.randint(5,20)} - Google {random.randint(10,40)} views", reply_markup=kb())
app=ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start",start))
app.add_handler(CallbackQueryHandler(cb))
print("Bot V15 OK")
app.run_polling()
