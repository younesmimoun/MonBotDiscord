import discord
from discord.ext import commands
import random

# Configuration des intents pour recevoir différents types d'événements
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.members = True
intents.message_content = True

# Création de l'instance du bot avec le préfixe de commande "!"
bot = commands.Bot(command_prefix="!", intents=intents)

# Liste des blagues pour la commande !joke
jokes = [
    "Pourquoi les plongeurs plongent-ils toujours en arrière et jamais en avant ? Parce que sinon ils tombent dans le bateau.",
    "Quel est le comble pour un électricien ? De ne pas être au courant.",
    "Que dit un oignon quand il se cogne ? Aïe !",
    "Pourquoi les canards sont toujours à l'heure ? Parce qu’ils sont dans l’étang.",
    "Qu'est-ce qui est jaune et qui attend ? Jonathan.",
    "Comment appelle-t-on un chat tout terrain ? Un chat-UV.",
    "Que fait une fraise sur un cheval ? Tagada tagada.",
    "Pourquoi les girafes n'existent-elles pas en 16 bits ? Parce qu'on ne peut pas les sauvegarder sur un GIF.",
    "Qu'est-ce qu'une tomate avec une cape ? Super-tomate. Et un concombre avec une cape ? Un concombre déguisé en super-tomate.",
    "Comment les abeilles communiquent-elles entre elles ? Par e-miel.",
    "Quel animal donne plus de lait qu'une vache ? Deux vaches.",
    "Quel est le sport le plus fruité ? La boxe, parce que quand tu reçois un coup, tu tombes dans les pommes et tu repars en fraise."
]

# Liste des mots interdits pour la fonctionnalité de bannissement
banned_words = ["NTM", "FDP"]

# Événement déclenché lorsque le bot est prêt et connecté
@bot.event
async def on_ready():
    print(f"{bot.user.name} s'est bien connecté !")

# Commande ping
@bot.command()
async def ping(ctx):
    await ctx.send("pong 🏓")

# Commande touché
@bot.command()
async def touché(ctx):
    await ctx.send("coulé! ⚓️")

# Commande members
@bot.command()
async def members(ctx):
    members = '\n'.join([member.name + ' - ' + ', '.join([role.name for role in member.roles if role.name != "@everyone"]) for member in ctx.guild.members])
    await ctx.send(members)

# Commande joke
@bot.command()
async def joke(ctx):
    await ctx.send(random.choice(jokes))

# Répondre automatiquement à certains messages
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Réaction automatique pour le mot "bonjour"
    if "bonjour" in message.content.lower():
        await message.add_reaction("👋")

    # Vérification des mots interdits pour la fonction de bannissement
    if any(word in message.content.lower() for word in banned_words):
        await message.author.ban(reason="Utilisation de mots interdits")
        await message.channel.send(f"{message.author.mention} a été banni pour utilisation de mots interdits.")

    # Ne pas oublier de traiter également les commandes !
    await bot.process_commands(message)

# Événement déclenché lorsqu'un nouvel utilisateur rejoint le serveur
@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name='general')  # Assurez-vous que le canal s'appelle 'general' ou modifiez selon le besoin
    if channel:
        await channel.send(f"Bienvenue sur le serveur, {member.mention}! 🎉")

# Événement déclenché lorsqu'un nouvel utilisateur rejoint le serveur
@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name='général')
    if channel:
        welcome_message = """
        Bienvenue sur le serveur, {0}! 🎉

        Voici quelques commandes que vous pouvez utiliser :
        - `!ping` : Vérifiez si le bot est en ligne avec une réponse rapide.
        - `!touché` : Réponse ludique avec "coulé! ⚓️".
        - `!members` : Affiche la liste des membres et leurs rôles.
        - `!joke` : Recevez une blague pour égayer votre journée.

        Pour toute aide supplémentaire, contactez l'administrateur du serveur.
        """.format(member.mention)
        await channel.send(welcome_message)



# Démarrage du bot
bot.run("MTIzNDg1NzQ3MDc4MzEzMTY3OA.Gtjszw.Qf49qVU8b98-bIuQ1FLCEnIoakpfvu-PYJnt20")
