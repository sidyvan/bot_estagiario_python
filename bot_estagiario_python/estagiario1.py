# -*- coding: utf-8 -*-
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

#bot = ChatBot('Test')
bot = ChatBot(
	'Estagiário',
	read_only=False,
	storage_adapter='chatterbot.storage.SQLStorageAdapter',
	database='./database.sqlite3'
)
saudacao = ['Olá como vai a sua relação com computador?',
			'Estou com problemas',
			'Como posso ajudar?'
			]
impressora = [
	'A minha impressora não imprime', 
	'Por favor, reinicie o computador',
	'A impressora esta sem tinta',
	'Entendi, peça ao pessoal do TI para trocar para você.'

	]

computador_nao_liga = [
				'O computador não liga',
				'O computador está ligado na tomada',
				'A luzinha do display está ligada',
				'O computador está fazendo algum barulho'
					]


bot.set_trainer(ListTrainer)
bot.train(saudacao)
bot.train(impressora)
bot.train(computador_nao_liga)

while True:
	quest = input('Voce: ')
	resposta = bot.get_response(quest)
	print('Suporte: ', resposta)

