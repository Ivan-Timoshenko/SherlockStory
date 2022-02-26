if __name__ == '__main__':
    import telebot
    from config import API
    from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


    bot = telebot.TeleBot(API)
    chapter_controller = {}


    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.from_user.id, '''Привествую вас в виртуальной симуляции "Hartswood". Начнем игру?''')
        user_id = message.from_user.id
        chapter_controller[user_id] = 'chapter1Acquaintance'

    @bot.message_handler(content_types='voice')
    def voice_defend(message):
        bot.send_message(message.from_user.id, '''Ты точно коренной англичанин?
                                               Совершенно не могу понять, что ты говоришь.''')


    @bot.message_handler(content_types='sticker')
    def sticker_defend(message):
        bot.send_message(message.from_user.id, '''Джон, что это за идиотские картинки?''')


    @bot.message_handler(content_types='text')
    def start(message):
        user_id = message.from_user.id
        user_chapter = chapter_controller.get(user_id, 'start')

        if user_chapter == 'chapter1Acquaintance':
            play = acquaintance(message, user_id)


    def acquaintance(message, user_id):
        bot.message_handler(message.from_user.id,
                            '''Вы, как и в любое другое утро,  сидите в одиночестве в любимой кофейне, 
        пьете прекрасно сваренный капучино и читаете новости. Отвлекшись от телефона, вы замечаете странную команду
        из двух мужчин через два столика от вас, оживленно обсуждающих что-то между собой. 
        “Нет, Джон, такого точно не может быть, обшлага рукавов его пиджака были влажными,
        значит удар был нанесен со спины!” - вы невольно подслушали вскрик одного из них. 
        Вы заинтересовались и продолжаете наблюдать за ними. Какая странная пара - один с тростью, короткой прической, 
        обычными чертами лица, среднего роста, выглядит спокойным. 
        Второй высокий, с темными, слегка кудрявыми волосами, явно чем-то взволнованный.  
        -Шерлок, кажется, за нами пристально наблюдают…''')


    bot.polling()
