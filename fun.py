import requests
from time import sleep
import threading
from pypresence import Presence
import time

# token do Discord
token = "YOUR_TOKEN_HERE"

# lista de estados de on
presences = [
    {"status": "online"},
    {"status": "idle"},
    {"status": "dnd"},  # dnd = "do not disturb" (ocupado)
    {"status": "offline"}
]

# estrutura de dados para as frases e seus tempos de exibição
words = [
    ("", 10),
    ("se o felizes para sempre existisse...", 5),
    ("você ainda estaria aqui?", 5),
    ("", 15),
    ("você disse que estaria lá por mim.", 7),
    ("mas onde está você agora?", 5),
    ("", 10),
    ("talvez noutra vida ou na próxima vida...", 4),
    ("seríamos finalmente eu e você. :)", 3),
    ("", 11),
    ("x: @iamjunioru", 15),
    ("", 30),
    ("ig: @idkjuni", 20)
]

# função para atualizar a presença usando pypresence
def update_presence_pypresence():
    client_id = 'client_ID_here'  # client id
    RPC = Presence(client_id)
    RPC.connect()

    while True:
        # set_details = "bla bla"
        # set_state = "blabla"
        # set_large_text = ""

        # set_large_image = "url"
        set_small_image = "https://media.discordapp.net/attachments/987834140034469920/1223212319920881744/vazio.png?ex=6619083f&is=6606933f&hm=1b4e0751e93c0f6807c17c11c2aa9a1cf6fad3146c1eed22218e8f26df2691f6&=&format=webp&quality=lossless"

        # Atualiza a presença
        RPC.update(
            # large_image=set_large_image,  # 
            small_image=set_small_image,  # 
            # large_text=set_large_text,
            # details=set_details,  # custom text/details
            # state=set_state,  # custom state
            # join="join_secret",
            # spectate="spectate_secret",
            buttons=[{"label": "𖹭", "url": "https://discord.gg/TZfKZPdA"}],      
            # party_size=[1, 69420],
            start=1704067200
        )
        # aguarda antes de atualizar novamente
        time.sleep(30)

# função para atualizar a presença
def update_presence():
    while True:
        for presence in presences:
            requests.patch("https://ptb.discordapp.com/api/v6/users/@me/settings", headers={"authorization": token}, json=presence)
            sleep(5)  # mudar o estado de presence a cada 0.5 segundos

# função para exibir frases do status
def update_status():
    while True:
        for phrase, duration in words:
            content = {
                "custom_status": {"text": phrase}
            }
            requests.patch("https://ptb.discordapp.com/api/v6/users/@me/settings", headers={"authorization": token}, json=content)
            sleep(duration)

# inicia as threads para atualizar a presença e exibir frases do status simultaneamente
thread_presence_pypresence = threading.Thread(target=update_presence_pypresence)
thread_presence = threading.Thread(target=update_presence)
thread_status = threading.Thread(target=update_status)

thread_presence_pypresence.start()
thread_presence.start()
thread_status.start()
