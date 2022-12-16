from aiogram import Bot, types, executor
from aiogram.dispatcher import Dispatcher

# Токен бота для подключения к нему
TOKEN = "5625099906:AAEDIPUMjmfdwrPCY0bCeG-yOYDskpNNEHk"
# Подкюлчаем бота к токену и
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
a = 0
beep=""
alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers=["1","2","3","4","5","6","7","8","9","0"]

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет, напиши /shifr")


@dp.message_handler(commands=['/shifr'])
async def process_start_command(message: types.Message):
    await bot.send_message(msg.from_user.id, str(users[int(f"{command.args}")]))
    beep=""
    a=command1
    for i in str(a):
        for j in len(alphabet):
            if i == "z":
                beep+="a"
            elif alphabet[j] == i:
                beep+=str(alphabet[j+1])
        for j in len(numbers):
            if i == "0":
                beep+="1"
            elif numbers[j] == i:
                beep += str(numbers[j+1])
    await message.reply(beep)



if __name__ == '__main__':
    executor.start_polling(dp)