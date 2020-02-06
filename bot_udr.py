import telebot

bot = telebot.TeleBot('1008479383:AAHIq-cvW2PpdeEGc7DKiZcqMMk0AL58pzM')
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.add('О программе', 'Как принять участие', 'Наши контакты', 'Часто задаваемые вопросы', 'Оставить заявку')
withPhoto = {
    'как принять участие': 'https://uchitel.ru/uploads/2019/10/otbor.png'
}
withVideo ={
    'часто задаваемые вопросы': 'media/mp4uchitelru_faq.mp4'
}
withPhoto2 = {'о программе': 'https://sun9-18.userapi.com/c858132/v858132060/15f1d5/CDVZaR0TWTY.jpg'}
withPhoto3 = {'наши контакты': 'https://sun9-21.userapi.com/c858132/v858132060/15f1f0/p7SP9aDm4XY.jpg'}
withPhoto4 = {'оставить заявку': 'https://sun9-69.userapi.com/c858132/v858132060/15f1f9/j0LgcCYazDw.jpg'}
answers = {
    'о программе': 'Общественный проект «Учитель для России» создан в 2015 году, чтобы обеспечить равенство образовательных возможностей для детей из разных регионов России. Проект предлагает уникальную возможность альтернативного входа в профессию учителя для молодых специалистов, мотивируя их к построению карьеры в образовании и социальной сфере. Программа работает в 78 школах и 6 регионах, в которых учителя проекта обучают более 34 тысяч детей.\nЧитайте о нашей миссии и истории на сайте: http://bit.ly/2undn67',
    'как принять участие': 'Мы отвечаем перед детьми за то, какие учителя придут в школу — поэтому уделяем особое внимание отбору участников. Прямо сейчас мы ведём приём заявок на участие в программе в 2020 учебном году. Наши требования для участия в программе:\n► оконченное высшее образование на момент 1 сентября 2020 года;\n ► готовность и желание работать в школе два года на полной ставке;\n► возможность принять участие в пятинедельном Летнем институте (четыре недели в июле и одна неделя в августе 2020 года);\n► готовность переехать в город или село Калужской, Тамбовской, Воронежской, Новгородской, Нижегородской или Новосибирской областей.\nПодробнее о наших критериях и этапах отбора читайте на сайте: http://bit.ly/36b36Y9.\nПодать заявку на участие: http://bit.ly/2RcDZ2Q.',
    'часто задаваемые вопросы': 'Ответы на часто задаваемые вопросы вы можете найти по ссылке: http://bit.ly/2ulFVgE',
    'наши контакты': 'Мы будем рады ответить на все ваши вопросы:\nОб участии в программе: otbor@uchitel.ru\nПо вопросам попечительства и финансового партнёрства — пишите Марии Парфёновой: mparfenova@uchitel.ru\nПо запросам от СМИ — Надежде Якимовой: nyakimova@uchitel.ru\nПо вопросам информационного и медийного партнёрства — Свете Примаковой: sprimakova@uchitel.ru\nВопросы, не попавшие в категории выше: i@uchitel.ru\nНаш телефон: ‭+7 499 390 36 53',
    'оставить заявку': 'Вы на верном пути! Регистрация на участие в программе займёт всего пару минут: http://bit.ly/2RcDZ2Q',
}

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,
                     'Здравствуйте! Это команда программы «Учитель для России». Чтобы узнать подробнее о программе нажми /help')


@bot.message_handler(commands=['help'])
def help(message):
    if message.text == "/help":
        bot.send_message(message.from_user.id, 'Пожалуйста, выберите вариант', reply_markup=keyboard1)
    else:
        bot.send_message(message.from_user.id, 'Используйте /help')


@bot.message_handler(content_types=['text'])
def send_text(message):
    user_command = message.text.lower()

    if user_command in answers:
        if user_command in withPhoto:
            bot.send_photo(message.chat.id, withPhoto[user_command])
        if user_command in withPhoto2:
            bot.send_photo(message.chat.id, withPhoto2[user_command])
        if user_command in withPhoto3:
            bot.send_photo(message.chat.id, withPhoto3[user_command])
        if user_command in withPhoto4:
            bot.send_photo(message.chat.id, withPhoto4[user_command])
        if user_command in withVideo:
            video = open(withVideo[user_command], 'rb')
            bot.send_video(message.chat.id, video)
        bot.send_message(message.chat.id, answers[user_command])


bot.polling(none_stop=True, interval=0)
