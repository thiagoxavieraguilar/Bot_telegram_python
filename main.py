import telebot

#coloque a sua key api do telegram
key_api = ""

bot = telebot.TeleBot(key_api)

@bot.message_handler(commands=['opcao1'])
def opcao1(mensagem):
    texto = """
    O que você deseja? (clique em uma opção)
    /pizza Pizza
    /acai  Açai
    /hamburguer Hamburguer
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=['opcao2'])
def opcao2(mensagem):
    bot.send_message(mensagem.chat.id, "Para enviar uma reclamção, mande um e-mail para reclamação@gmail.com")

def verificar(mensagem):
    return True


@bot.message_handler(commands=['pizza'])
def pizza(mensagem):
    bot.send_message(mensagem.chat.id,'Pedido feito com sucesso, a sua pizza já está saindo')
    

@bot.message_handler(commands=['acai'])
def acai(mensagem):
    bot.send_message(mensagem.chat.id,'Pedido feito com sucesso, o seu acai já está saindo')


@bot.message_handler(commands=['hamburguer'])
def hamburguer(mensagem):
    bot.send_message(mensagem.chat.id,'Pedido feito com sucesso, o seu hamburguer já está saindo')
    

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Escolha uma opção para conntinuar(clique no item):
    /opcao1 Fazer um pedido
    /opcao2 Reclamar de um pedido
    
    Responder qualquer outra coisa não vai funcionar, clique em uma das opções
    """
    bot.reply_to(mensagem,texto)
#loop infinito 
bot.polling()