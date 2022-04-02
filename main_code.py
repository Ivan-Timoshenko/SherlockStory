if __name__ == '__main__':
    import telebot
    from config import API
    from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


    class Master:
        _instance = None

        def __init__(self):
            self.dictionary = {}

        @classmethod
        def get_instance(cls):
            if not cls._instance:
                cls._instance = Master()
            return cls._instance


    bot = telebot.TeleBot(API)
    chapter_controller = Master.get_instance()


    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.from_user.id,
                         '''Привествую вас в виртуальной симуляции "Hartswood". Далее я буду обращаться к вам от имени
                          Системы, а ваши реплики будут обозначены меткой игрока "И". Начнем игру.''')
        user_id = message.from_user.id
        chapter_controller.dictionary[user_id] = 'chapter1Acquaintance'


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
            play = acquaintance(message)


    def acquaintance(message):
        bot.send_message(message.from_user.id,
                         '''Вы, как и в любое другое утро,  сидите в одиночестве в любимой кофейне, 
        пьете прекрасно сваренный капучино и читаете новости. Отвлекшись от телефона, вы замечаете странную команду
        из двух мужчин через два столика от вас, оживленно обсуждающих что-то между собой. 
        “Нет, Джон, такого точно не может быть, обшлага рукавов его пиджака были влажными,
        значит удар был нанесен со спины! Думай, Джон, думай!” - вы невольно подслушали вскрик одного из них. 
        Вы заинтересовались и продолжаете наблюдать за ними. Какая странная пара - один с тростью, короткой прической, 
        обычными чертами лица, среднего роста, выглядит спокойным. 
        Второй высокий, с темными, слегка кудрявыми волосами, явно чем-то взволнованный.  
        -Шерлок, кажется, за нами наблюдают…''')
        bot.send_message(message.from_user.id,
                         '''Система: Ваши действия?
                         [1] Сделать вид что вы ничего не слышали
                         [2] Подойти и спросить''')
        user_choice = message.text
        if user_choice == '1':
            bot.send_message(message.from_user.id,
                             '''Ш: Ну и что?\n 
                             Д: Шерлок, ты слишком громкий. Прошу извинить моего друга, он всегда так говорит, когда взволнован. Надеюсь, мы вам не сильно помешали?\n
                             И: Нет, однако, со стороны звучит так, будто вы обсуждаете преступление.\n
                             Ш: Так и есть, поучавствуете? Джон совершенно не понимает очевидных вещей.\n
                             И: С удовольствием, с детства увлекаюсь криминалистикой.''')
            user_chapter = 'chapter2Assasination'
        elif user_choice == '2':
            bot.send_message(message.from_user.id,
                             '''Вы подходите к их столику и Шерлок рассказывает вам историю.''')
    bot.polling()
