import telebot
import pyowm

owm = pyowm.OWM('7a96899518c9006f64d222b4a7b44a0e', language= "ru")
bot = telebot.TeleBot("894429828:AAHsGTISP12WtThKsifP0KIBpagEax8r1xo")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Привет! Я бот подсказывающий погоду! \nПросто напиши название города и я постараюсь что-нибудь найти!")


@bot.message_handler(content_types=['text'])
def echo_all(message):
	try:
		observation = owm.weather_at_place(message.text)
		w = observation.get_weather()
		weather = w.get_detailed_status()
		temp = w.get_temperature('celsius')["temp"]
		wet = w.get_humidity()
		wind = w.get_wind()["speed"]
		answer = message.text + ' сейчас переживает примерно следующее:\n'
		answer += "Тут " + weather + "! Средняя температура: " + str(temp) + " градусов.\n"
		answer += "Влажность: " + str(wet) + "%\n"
		answer += "Скорость ветра составляет " + str(wind) + " м\с.\n"

		bot.send_message(message.chat.id, answer)
	except:
		bot.send_message(message.chat.id, "К сожалению я понимаю не все города, но ты можешь попробовать ввести название на английском!")

bot.polling(none_stop=True)

