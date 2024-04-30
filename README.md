### Documentation du Bot Discord

#### Introduction
Ce document détaille le fonctionnement et la configuration du bot Discord utilisé pour interagir de manière automatisée avec les membres d'un serveur. Le bot est programmé en Python en utilisant la bibliothèque `discord.py`.

#### Configuration et Intents
Les *intents* sont des options qui permettent au bot de recevoir et d'envoyer différents types d'événements à partir des serveurs Discord. Pour ce bot, les intents suivants sont activés :

- `messages` : Pour recevoir des messages dans des salons textuels.
- `guilds` : Pour interagir avec les informations du serveur.
- `members` : Pour interagir avec les membres du serveur.
- `message_content` : Pour accéder au contenu des messages.

La configuration initiale est réalisée comme suit :
```python
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.members = True
intents.message_content = True
```

#### Instance du Bot
Le bot est instancié avec un préfixe de commande `!` qui doit être utilisé par les membres pour invoquer les commandes.

```python
bot = commands.Bot(command_prefix="!", intents=intents)
```

#### Commandes Configurées
- `!ping` : Répond "pong 🏓" lorsque utilisée, utile pour vérifier si le bot est actif.
- `!touché` : Répond "coulé! ⚓️" pour jouer de manière ludique.
- `!members` : Liste tous les membres du serveur avec leurs rôles.
- `!joke` : Envoie une blague aléatoire à partir d'une liste prédéfinie.

#### Événements et Automatisations
- `on_ready` : Annonce dans la console que le bot s'est connecté.
- `on_message` :
  - Réagit aux salutations avec un emoji 👋.
  - Vérifie la présence de mots interdits et peut bannir un membre en conséquence.

#### Nouvelle Fonctionnalité
Une nouvelle fonctionnalité a été ajoutée pour accueillir les nouveaux membres avec une liste des commandes disponibles dès qu'ils rejoignent le serveur. Voici comment cela fonctionne :

```python
# Événement déclenché lorsqu'un nouvel utilisateur rejoint le serveur
@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name='general')  # Assurez-vous que le canal s'appelle 'general' ou modifiez selon le besoin
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
```

Cette fonction envoie un message de bienvenue personnalisé à chaque nouvel utilisateur qui rejoint le serveur dans le canal nommé "general" (vous pouvez le modifier selon vos besoins). Ce message comprend une liste des commandes disponibles pour aider les nouveaux membres à démarrer sur le serveur.