from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
import random
from threading import Thread
import schedule
import asyncio
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes
)
from datetime import time
from telegram.constants import ParseMode
Obj = {
1: "блёб",
2: "сухпаек",
3: "хлеб",
4: "инструменты",
5: "машина",
6: "оружие"
}
groups = [
        "Императору",
        "Верховному совету",
        "полиции",
        "вашей вере"
]
vilians = [
        "войны",
        "подлых диверсантов",
        "вашей слабой веры"
]
def maker(n):
    n = int(n)
    if len(str(n)) <= 3:
        return str(n)
    elif 3 < len(str(n)) <= 6:
        return str(round(n/1000, 2))+" тысяч(а)"
    elif 6 < len(str(n)) <= 9:
        return str(round(n / 1000000, 2)) + " миллион(ов)"
    elif 9 < len(str(n)) <= 12:
        return str(round(n / 1000000000, 2)) + " миллиард(ов)"
    else:
        return str(n)
CHAT_ID = 6836405294
TOKEN = "8022164051:AAGy_gYDvC_riGk66tWpCmQ11EQu8qmU8DU"
val = [50, 20, 30, 100, 500000, 1250000]
def news():
    if random.randint(1, 3) == 1:
        obj = random.randint(1, len(Obj))
        upby = round(random.uniform(0.01, 0.2), 2)
        mod = val[obj - 1] * upby
        newval = round(val[obj - 1] - mod, 2)
        val[obj - 1] = newval
        return   f"Цена на объект: {Obj[obj]} упала на {round(upby * 100, 2)}% и теперь равна {maker(newval)} кк благодаря {random.choice(groups)}."

    else:
        obj = random.randint(1, len(Obj))
        upby = round(random.uniform(0.01, 1.0), 2)
        mod = val[obj - 1] * upby
        newval = round(val[obj - 1] + mod, 2)
        val[obj - 1] = newval
        return f"Цена на объект: {Obj[obj]} поднялась на {round(upby * 100, 2)}% и теперь равна {maker(newval)} кк из-за {random.choice(vilians)}."
def q():
    return "―"*10
async def get(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"Я РАБОТАЮ"
    )



alr = []
async def regime(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global alr
    user = update.effective_chat.id
    if not user in alr:
        context.job_queue.run_daily(
            callback=at9,
            time=time(hour=6, minute=0),
            chat_id=update.effective_chat.id,
        )
        context.job_queue.run_daily(
            callback=at10,
            time=time(hour=7, minute=0),
            chat_id=update.effective_chat.id,
        )
        context.job_queue.run_daily(
            callback=at1230,
            time=time(hour=9, minute=30),
            chat_id=update.effective_chat.id,
        )
        context.job_queue.run_daily(
            callback=at13,
            time=time(hour=10, minute=0),
            chat_id=update.effective_chat.id,
        )
        context.job_queue.run_daily(
            callback=at18,
            time=time(hour=15, minute=0),
            chat_id=update.effective_chat.id,
        )
        context.job_queue.run_daily(
            callback=at19,
            time=time(hour=16, minute=0),
            chat_id=update.effective_chat.id,
        )
        context.job_queue.run_daily(
            callback=at22,
            time=time(hour=19, minute=0),
            chat_id=update.effective_chat.id,
        )
        await update.message.reply_text(
            f"Ваше устройство синхронизировано с единым Имперским временем.\n{q()}\nИ помните: Империя заботится о вас!", parse_mode=ParseMode.MARKDOWN
        )
        alr.append(user)
    else:
        await update.message.reply_text(
            f"Ваше устройство уже было синхронизировано с единым Имперским временем.\n{q()}\nИ помните: Империя заботится о вас!", parse_mode=ParseMode.MARKDOWN
        )

async def at9(context: ContextTypes.DEFAULT_TYPE):
await context.bot.send_message(
        chat_id=context.job.chat_id,
        text=f"Граждане Империи, по единому расписанию в данный промежуток времени объявляется утренний подъем. Желаем вам удовлетворительно сегодня поработать.\n{q()}\nИ помните: Империя заботится о вас!",
        parse_mode=ParseMode.MARKDOWN
    )
async def at10(context: ContextTypes.DEFAULT_TYPE):
    new = ""
    for i in range(3):
        new += news() + "\n"
    plus = ""
    out = ""
    for i in range(1, len(Obj) + 1):
        plus = Obj[i] + " - " + maker(val[i - 1]) + " кк" + "\n"
        out += plus
    await update.message.reply_text(
        f"Граждане Империи, предоставляем вам сводку новостей:\n{new}{out}{q()}\nИ помните: Империя заботится о вас!",
        parse_mode=ParseMode.MARKDOWN)
async def at1230(context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=context.job.chat_id,
        text=f"Граждане Империи, по единому расписанию в данный промежуток времени объявляется обеденный перерыв. Желаем вам удовлетворительного поглощения пищевых калорий.\n{q()}\nИ помните: Империя заботится о вас!",
        parse_mode=ParseMode.MARKDOWN
    )
async def at13(context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=context.job.chat_id,
        text=f"Граждане Империи, по единому расписанию в данный промежуток времени обеденный перерыв окончен. Желаем вам удовлетворительного продолжения рабочего дня.\n{q()}\nИ помните: Империя заботится о вас!",
        parse_mode=ParseMode.MARKDOWN
    )
async def at18(context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=context.job.chat_id,
        text=f"Граждане Империи, по единому расписанию в данный промежуток времени объявляется ужин. Желаем вам удовлетворительного поглощения пищевых калорий.\n{q()}\nИ помните: Империя заботится о вас!",
        parse_mode=ParseMode.MARKDOWN
    )
async def at19(context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=context.job.chat_id,
        text=f"Граждане Империи, по единому расписанию в данный промежуток времени объявляются свободные занятия. Всем вернутся в свои номерные комнаты и оставаться там. Желаем вам удовлетворительного времяпрепровождения.\n{q()}\nИ помните: Империя заботится о вас!",
        parse_mode=ParseMode.MARKDOWN
    )
async def at22(context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=context.job.chat_id,
        text=f"Граждане Империи, по единому расписанию в данный промежуток времени объявляется отбой. Желаем вам удовлетворительного ночного отдыха.\n{q()}\nИ помните: Империя заботится о вас!",
        parse_mode=ParseMode.MARKDOWN
    )





def main():

    application = Application.builder().token(TOKEN).build()

    # Добавляем обработчики
    application.add_handler(CommandHandler("start", regime))


    application.add_handler(CommandHandler("get", get))


    application.run_polling()






main()


# уровень 1
# камиль - 6836405294
# рамазан - 6840770961
