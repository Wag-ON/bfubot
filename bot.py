import telebot
import logging
import json
from config import *

jsonString='{ "Group": "MO-2", "TimeTable":{"Day":[ {"DayName":"Вторник", "time": "15-20","Cab": "(ауд. 231)", "Lesson": "лекция Python"}, {"DayName":"Среда", "Подгруппа": [{"Номер":"(1я подгруппа)", "time":"13-40", "Cab":"(ауд. 230)", "Lesson": "лаба Python"}, {"Номер":"(2я подгруппа)", "time":"10-10", "Cab":"(ауд. 235)", "Lesson": "лаба Python"}, {"Номер":"(3я подгруппа)","time":"12-00", "Cab": "(ауд. 235)", "Lesson":"лаба Python"} ]} ]} }'

obj=json.loads(jsonString)

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')  # Ну это по классике, логи

bot = telebot.TeleBot(Config.BOT_TOKEN)  # Создает объект класса "TeleBot", то есть нашего бота

@bot.message_handler(
    content_types=['text', 'audio', 'document', 'photo', 'sticker', 'video', 'video_note', 'voice', 'location',
                   'contact', 'new_chat_members', 'left_chat_member', 'new_chat_title', 'new_chat_photo',
                   'delete_chat_photo', 'group_chat_created', 'supergroup_chat_created', 'channel_chat_created',
                   'migrate_to_chat_id', 'migrate_from_chat_id',
                   'pinned_message'])  # декоратор который заставляет пользователя реагировать на новые сообщения

@bot.message_handler(commands=['mo2'])

def sending_auto2(message):
    
    if message.text=="/mo2":
      bot.send_message(message.chat.id, "Группа "+obj["Group"]+"\n\n"+"*"+obj['TimeTable']["Day"][0]["DayName"]+"*\n"+obj['TimeTable']["Day"][0]['time']+' '+obj['TimeTable']["Day"][0]['Cab']+' '+obj['TimeTable']["Day"][0]['Lesson']+'\n\n'+'*'+obj['TimeTable']["Day"][1]["DayName"]+'*\n'+obj['TimeTable']["Day"][1]["Подгруппа"][0]["time"]+ " " +obj['TimeTable']["Day"][1]["Подгруппа"][0]["Cab"]+ " " +obj['TimeTable']["Day"][1]["Подгруппа"][0]['Lesson']+' '+obj['TimeTable']["Day"][1]["Подгруппа"][0]["Номер"]+"\n"+obj['TimeTable']["Day"][1]["Подгруппа"][1]["time"]+ " " +obj['TimeTable']["Day"][1]["Подгруппа"][1]["Cab"]+" "+obj['TimeTable']["Day"][1]["Подгруппа"][1]['Lesson']+' '+obj['TimeTable']["Day"][1]["Подгруппа"][1]["Номер"]+"\n"+obj['TimeTable']["Day"][1]["Подгруппа"][2]["time"]+" "+obj['TimeTable']["Day"][1]["Подгруппа"][2]["Cab"]+" "+obj['TimeTable']["Day"][1]["Подгруппа"][2]['Lesson']+' '+obj['TimeTable']["Day"][1]["Подгруппа"][2]["Номер"]+'\n', parse_mode="Markdown")
    
    elif message.text=="/pm4":
      bot.send_message(message.chat.id, 'Группа ПМ-4 \n \n'+'*Пятница*'+'\n'+'10-10 (ауд. 230. Вход через 230 ауд.) лаба Python (1я подгруппа)\n12-00 (ауд. 118) лекция Python\n13-40 (ауд. 214) лаба Python (2я подгруппа)\n', parse_mode="Markdown")
    
    elif message.chat.id > 0:
      bot.send_message(chat_id=message.chat.id, text=autosending_text(bot, message), parse_mode='html',disable_web_page_preview=True)  # Отправляет авто сообщение

    # NOTE
    # Не отправляем сообщения в общие чаты.
    # else:
      # bot.send_message(chat_id=message.chat.id, text='Это сообщение в чат', parse_mode='html',disable_web_page_preview=True)

if __name__ == '__main__':
    bot.polling()  # Заставляет бота получать уведомления о новых сообщениях
