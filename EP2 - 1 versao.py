import random
import json
import time
def acerto_critico(sorte):
	sorteado = random.randint(0,100)
	if sorteado in range(0, sorte):
		return True
	else:
		return False




def batalha(jogador, adversario):
    vida_jogador = jogador["vida"]
    vida_adversario = adversario["vida"]
    dano_jogador = jogador["poder"] - adversario["defesa"]
    dano_adversario = adversario["poder"] - jogador["defesa"]
    if dano_jogador < 0:
        dano_jogador = 0
    if dano_adversario < 0:
        dano_adversario = 0
    print("""Combate inicia!
        {0} vs {1}""".format(jogador["nome"], adversario["nome"]))
    time.sleep(4)
    while vida_jogador > 0 and vida_adversario > 0:
        time.sleep(2)
        if acerto_critico(jogador["sorte"]) == True:
            vida_adversario = vida_adversario - (2 * dano_jogador)
            print("{0}: ATAQUE CRÍTICO! {1} de dano".format(jogador["nome"],
                                                            2 * dano_jogador)) 
        else:    
            vida_adversario = vida_adversario - dano_jogador
            print("{0}: Ataca! {1} de dano".format(jogador["nome"],
                                                   dano_jogador))
        if vida_adversario < 0:
            vida_adversario = 0
        print("{0}: {1} restante de vida".format(adversario["nome"],
                                                 vida_adversario))
        if vida_adversario < 1:
            return "VITÓRIA!"
        time.sleep(2)
        if acerto_critico(adversario["sorte"]) == True:
            vida_jogador = vida_jogador - (dano_adversario * 2)
            print("{0}: ATAQUE CRÍTICO! {1} de dano".format(adversario["nome"],
                                                            vida_jogador))
        else:
            vida_jogador = vida_jogador - dano_adversario
            print("{0}: Ataca! {1} de dano".format(adversario["nome"],
                                                   dano_adversario))
        if vida_jogador < 0:
            vida_jogador = 0
        print("{0}: {1} restante de vida".format(jogador["nome"],
                                                 vida_jogador))
        if vida_jogador < 1:
            return "DERROTA!"




with open("inspermons.json") as arquivo:
    inspermons = json.load(arquivo)

    


z = 0
for ipmon in inspermons:
    print(ipmon)
    print("Número do inspermon: {0}".format(z + 1)) 
    z = z+1
x_do_jogador = int(input("Digite o número do inspermon escolhido: ")) - 1
inspermon_jogador = inspermons[x_do_jogador]
print('''Seu inspermon escolhido foi: {0}
                                vida: {1}
                               poder: {2}
                              defesa: {3}
                               sorte: {4}'''.format(
                      inspermon_jogador["nome"],
                      inspermon_jogador["vida"],
                      inspermon_jogador["poder"],
                      inspermon_jogador["defesa"],
                      inspermon_jogador["sorte"])) 
while True:
    acao = input("Digite lutar ou dormir: ")
    if acao == "dormir":
        break
    elif acao == "lutar":
        inspermon_adversario = random.choice(inspermons)
        print('''O inspermon adversário é: {0}
                                     vida: {1}      
                                    poder: {2}
                                   defesa: {3}
                                    sorte: {4}'''.format(
                                    inspermon_adversario["nome"],
                                    inspermon_adversario["vida"],
                                    inspermon_adversario["poder"],
                                    inspermon_adversario["defesa"],
                                    inspermon_adversario["sorte"]))
        resultado = batalha(inspermon_jogador,inspermon_adversario)
