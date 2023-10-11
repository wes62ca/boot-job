import discord
import os 
# Configura as intenções
intents = discord.Intents.default()
intents.members = True  # Habilita a intenção de membros
intents.presences = True  # Habilita a intenção de presenças
intents.message_content = True
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

        if message.content == '?regras':
            await message.channel.send(f'{message.author.name} as regras do servidor são:{os.linesep}1-Não falar palavrão{os.linesep}2- Regra importante')

client = MyClient(intents=intents)
client.run('MTE2MDMzNzI2Njk4ODgxMDMxMQ.GweHbL.fobPwMwNLDwNn9Ht3Ol877JGWGSp4vvSejCPEU')
