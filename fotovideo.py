import telebot # importamos la libreria de telebot
bot = telebot.TeleBot('1930454566:AAFAwFRm-kiKOZwhLi0olZYKrq3Qh-iDL8s') #anadimos el token
updates = bot.get_updates()
message = updates[0].message
from_user = message.from_user
id = from_user.id
get_me = bot.get_me()
@bot.message_handler(commands=['hola', 'hi']) #definimos el comando
def hola(mensaje):
    bot.reply_to(mensaje, "Hola como estás?")
    print("Mandaron hola o hi")
@bot.message_handler(commands=['foto', 'photo'])
def conversion(mensaje):
    bot.send_chat_action(id, 'typing')
    photo = open('C:/Users/Dios es Amor/Desktop/imagen/foto.jpg', 'rb')
    bot.send_photo(id, photo)  

@bot.message_handler(commands=['video', 'mp4'])
def documento(mensaje):
    bot.send_chat_action(id, 'typing')
    video = open('videos.mp4', 'rb')
    bot.send_video(id, video)

bot.polling()