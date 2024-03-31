import requests
from time import sleep
from colorama import Fore
import json
import os

with open('config.json') as f:
    config = json.load(f)

token = config.get("token")

os.system("cls")  # limpa a tela (opcional)

print(f"{Fore.WHITE}[ {Fore.CYAN}* {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Discord Animated Status adapted by {Fore.WHITE}R. G. S. Junior{Fore.LIGHTBLACK_EX} | Licensed Under {Fore.WHITE}MIT {Fore.LIGHTBLACK_EX}License")
print(f"{Fore.WHITE}[ {Fore.CYAN}* {Fore.WHITE}] {Fore.LIGHTBLACK_EX}follow me on GitHub: {Fore.WHITE}https://github.com/iamjunioru")
print(f"{Fore.WHITE}[ {Fore.CYAN}* {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Follow Pieter on GitHub: {Fore.WHITE}https://github.com/PieterSpruijt\n")

# words array
words = ["",
         "se o felizes para sempre existisse...",
         "você ainda estaria aqui?",
         "",
         "você disse que estaria lá por mim.",
         "mas onde está você agora?",
         "",
         "talvez noutra vida ou na próxima vida...",
         "seríamos finalmente eu e você.",
         "",
         "x: @iamjunioru",
         "",
         "ig: @idkjuni"
         ]

print(f"{Fore.WHITE}[ {Fore.YELLOW}> {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Coloque o intervalo de atualização (em segundos): {Fore.WHITE}")
update_interval = float(input())

print(f"\n{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Deseja usar animação nas letras ~risco de ban~ (y/n): {Fore.WHITE}")
use_animation = input().lower() == 'y'

# se o usuário quiser emoji
if use_animation:
    print(f"\n{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Pesquise aqui: {Fore.WHITE}www.webfx.com/tools/emoji-cheat-sheet {Fore.LIGHTBLACK_EX}(Ou deixe vazio se não quiser emoji)")
    emoji = input(f"{Fore.WHITE}[ {Fore.YELLOW}> {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Insira o nome do emoji(ex: :grinning_face:): {Fore.WHITE}")
else:
    emoji = ""  # vai corrigir e definir como string vazia caso o user não quiser 

current_word_index = 0

print(f"\n\n{Fore.WHITE}[ {Fore.GREEN}+ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Animando...")

while True:
    # use o index da palavra atual do array
    status = words[current_word_index]

    if use_animation:
        for text in range(0, len(status)+1):
            if emoji != "":
                content = {
                    "custom_status": {"text": status[:text], "emoji_name": emoji}
                }
            else:
                content = {
                    "custom_status": {"text": status[:text]}
                }
            requests.patch("https://ptb.discordapp.com/api/v6/users/@me/settings", headers={"authorization": token}, json=content)
            sleep(update_interval)
    else:
        # atualização instantânea
        content = {
            "custom_status": {"text": status}
        }
        requests.patch("https://ptb.discordapp.com/api/v6/users/@me/settings", headers={"authorization": token}, json=content)

    # atualize o index da palavra e faz o loop se necessário
    current_word_index += 1
    if current_word_index >= len(words):
        current_word_index = 0

    sleep(update_interval)  # aguarda o intervalo especificado antes de atualizar a palavra