import random
import json
def batalha(jogador,adversario):
    vida_jogador = jogador["vida"]
    vida_adversario = adversario["vida"]
    while vida_jogador > 0 and vida_adversario > 0:
        vida_adversario = vida_adversario - (jogador["poder"] - adversario["defesa"])
        if vida_adversario < 1:
            return "VITÓRIA!"                               
        vida_jogador = vida_jogador - (adversario["poder"] - jogador["defesa"])
        if vida_jogador < 1:
            return "DERROTA!"   
        
                                             
data = open("inspermons.json").read()
inspermons = json.loads(data)
z = 0
for imon in inspermons:
    print(imon)
    print("Número do inspermon: {0}".format(z + 1)) 
    z = z+1
x_do_jogador = int(input("Digite o número do inspermon escolhido: ")) - 1
inspermon_jogador = inspermons[x_do_jogador]
print('''Seu inspermon escolhido foi: {0}
vida: {1}
poder: {2}
defesa: {3}'''.format(inspermon_jogador["nome"],inspermon_jogador["vida"],inspermon_jogador["poder"],inspermon_jogador["defesa"]))   
while True:
    acao = input("Digite lutar ou dormir: ")
    inspermon_adversario = random.choice(inspermons)
    print('''O inspermon adversário é: {0}
vida: {1}
poder: {2}
defesa: {3}'''.format(inspermon_adversario["nome"],inspermon_adversario["vida"],inspermon_adversario["poder"],inspermon_adversario["defesa"])) 
    if acao == "dormir":
        break
    elif acao == "lutar":
        print(batalha(inspermon_jogador,inspermon_adversario))
