from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import telebot

iris = datasets.load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = SVC()
model.fit(X_train, y_train)
accuracy = model.score(X_test, y_test)
print("Accuracy:", accuracy)

# ======================================================================================

API_TOKEN = ''
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start', 'help'])
def start_message(message):
    start_text = '''Благодаря этому боту и встроенному в него искусственному интеллекту, вы сможете
    определить тип ириса из 0 — Setosa, 1 — Versicolor, 2 — Virginica, на основании о размерах его
    чашелистника и лепестка. Для этого нужно отправить сообщение боту в следующем формате:
    длина_чашелистника ширина_чашелистник  длина_лепестка ширина_лепестка
    данные разделяются пробелом, целая и дробная часть разделяются запятой
    Пример: 6,3 2,9 5,6 1,8'''
    test = '6,3 2,9 5,6 1,8'
    bot.send_message(message.chat.id, start_text)
    bot.send_message(message.chat.id, test)
    bot.send_message(message.chat.id, "Accuracy: " + str(accuracy))


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text: str = message.text
    # bot.reply_to(message, 'Получено сообщение: ' + message.text)
    try:
        num_iris = model.predict([text.replace(',', '.').split()])[0]
        if num_iris == 0:
            bot.reply_to(message, 'Скорее всего - это Setosa')
            img = open('0.png', 'rb')
            bot.send_photo(message.chat.id, img)
        elif num_iris == 1:
            bot.reply_to(message, 'Скорее всего - это Versicolor')
            img = open('1.png', 'rb')
            bot.send_photo(message.chat.id, img)
        elif num_iris == 2:
            bot.reply_to(message, 'Скорее всего - это Virginica')
            img = open('2.png', 'rb')
            bot.send_photo(message.chat.id, img)
        else:
            bot.reply_to(message, 'Ошибка')
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так. Проверьте формат запроса')
        print(e)


bot.polling()
