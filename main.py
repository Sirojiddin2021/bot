import telebot
from datetime import datetime
import calendar



API_KEY = "1960500338:AAGHjBiwp3qJPLAfuuc567MznM73fgFvP3c"

bot = telebot.TeleBot(API_KEY)

week_days=["Dushanba","Seshanba","Chorshanba","Payshanba","Juma","Shanba","Yakshanba"]

osh_str =["osh", "palov", "ош", "палов"]
answer1 =["yes", "ha", "ха"]
answer2 = ["no", "yo'q", "yoq"]
question = "Oshga qaysi kuni boramiz?"



i = 0;

def handle_messages(messages):
    now = datetime.now()
    weekday= calendar.weekday(now.year, now.month, now.day)
    try:
        for message in messages:
            if osh_str[0] in (message.json["text"]).lower() or osh_str[1] in (message.json["text"]).lower() or osh_str[2] in (message.json["text"]).lower() or osh_str[3] in (message.json["text"]).lower():

                bot.reply_to(message, 'Assalom alaykum okakhon '+message.from_user.first_name+',\nborakansizu!')
                bot.send_message(message.chat.id, 'Qachon osh? Bugun '+week_days[weekday]+',\nPayshanbagacha '+(str)(abs(weekday-3))+" kun borakan\nTashkillashtirib qo'yaymi")
                global i
                i = 1
            elif i == 1 and (answer1[0] == message.json['text'].lower() or answer1[1] == message.json['text'].lower() or answer1[2] == message.json['text'].lower()):
                # delete user last answer
                bot.delete_message(message.chat.id, message.message_id)

                bot.send_poll(message.chat.id, question, week_days, is_anonymous=False, type='regular', allows_multiple_answers=False, correct_option_id=None, is_closed=None,
                reply_to_message_id=None, reply_markup=None, timeout=None, explanation=None, explanation_parse_mode=None, open_period=None, close_date=None, allow_sending_without_reply=None, explanation_entities=None)
                bot.pin_chat_message(message.chat.id,message.message_id + 1)

                i = 0
            elif i == 1 and (answer2[0] == message.json['text'].lower() or answer2[1] == message.json['text'].lower() or answer2[2] == message.json['text'].lower()):

                # delete user last answer
                bot.delete_message(message.chat.id, message.message_id)
                # delete user answer -1
                bot.delete_message(message.chat.id, message.message_id -1)
                # delete user answer -2
                bot.delete_message(message.chat.id, message.message_id -2)

                i = 0
            print(i)


    except Exception as e:
        print(e)



def main() -> None:
    """Run bot."""
    # Create the Updater and pass it your bot's token.
    bot.set_update_listener(handle_messages)
    bot.polling()



if __name__ == '__main__':
    main()

