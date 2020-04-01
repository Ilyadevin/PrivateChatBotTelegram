from directories.bot_meeting_app.meeting_bot import *


@bot.message_handler(commands=['help'])
def help_user(message):
    try:
        time.sleep(2)
        bot.send_message(message.chat.id, 'Я - бот который поможет вам найти пару для приятного общения.\n'
                                          'Я использую данные из vk,\n'
                                          'Команды - "Настройки, Meet"\n',
                         reply_markup=keyboard_settings_meeting())
    except Exception as error_in_command:
        print(error_in_command)


@bot.message_handler(content_types=['text'])
def setting_user(message):
    try:
        if message.text.lower() == 'настройки' or \
                message.text.lower == '/настройки' or \
                message.text.lower('/meet') or \
                message.text.lower('meet'):
            bot.send_message(message.from_user.id, 'Введите логин и пароль в формате "password login"')
            list_of_log_data.append(message.from_user.id.split(' '))
            password = list_of_log_data[0]
            login = list_of_log_data[1]

    except Exception as error_log:
        print(error_log)