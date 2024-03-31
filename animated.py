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

# Pegar as palavras e tempos do usuário
num_words = int(input(f"{Fore.WHITE}[ {Fore.YELLOW}> {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Insira quantos status deseja adicionar: {Fore.WHITE}"))
words_and_times = []
for i in range(num_words):
    word = input(f"{Fore.WHITE}[ {Fore.YELLOW}> {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Status {i+1}: {Fore.WHITE}")
    time = float(input(f"{Fore.WHITE}[ {Fore.YELLOW}> {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Tempo para a status {i+1} (em segundos): {Fore.WHITE}"))
    words_and_times.append((word, time))

# perguntar sobre animação
print(f"\n{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Deseja usar animação nas letras? ~risco de ban~ (y/n): {Fore.WHITE}")
use_animation = input().lower() == 'y'

# emoji (opcional)
if use_animation:
    print(f"\n{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Pesquise aqui: {Fore.WHITE}www.webfx.com/tools/emoji-cheat-sheet {Fore.LIGHTBLACK_EX}(Ou deixe vazio se não quiser emoji)")
    emoji = input(f"{Fore.WHITE}[ {Fore.YELLOW}> {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Insira o nome do emoji(ex: :grinning_face:): {Fore.WHITE}")
else:
    emoji = ""  # dfine como string vazia caso o user não quiser

print(f"\n{Fore.WHITE}[ {Fore.GREEN}+ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}[O bot está sendo executado]")
sleep(1)
print(f"\n{Fore.WHITE}[ {Fore.GREEN}+ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Animando...")

while True:
    for word, time_per_word in words_and_times:
        # use a palavra e tempo atuais
        status = word

        # animação letra por letra (opcional)
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
                # ajuste o tempo de animação entre letras (opcional)
                sleep(0.1)  #  pode alterar este valor

        # atualização instantânea
        else:
            content = {
                "custom_status": {"text": status}
            }
            requests.patch("https://ptb.discordapp.com/api/v6/users/@me/settings", headers={"authorization": token}, json=content)

        # aguarda o tempo total da palavra atual
        sleep(time_per_word)
