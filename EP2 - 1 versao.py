import random
import json
import time


def level_up(jogador, nv_ipmon, xp_atual):
    xp_prox_nv = 15 + 10 * nv_ipmon
    if xp_atual >= xp_prox_nv:
        novo = {}
        novo["nome"] = jogador["nome"]
        novo["poder"] = round(jogador["poder"] * 1.20)
        novo["vida"] = round(jogador["vida"] * 1.25)
        novo["defesa"] = round(jogador["defesa"] * 1.30)
        novo["sorte"] = round(jogador["sorte"] * 1.20) 
        novo["xp_m"] = jogador["xp_m"]
        novo["xp_atual"] = 0
        novo["level"] = jogador["level"] + 1
        return ("sim", novo)
    else:
        return "nao"

def acerto_critico(sorte):
    sorteado = random.randint(0, 99)
    if sorteado in range(0, sorte):
        return True
    else:
        return False


def fuga(sorte, n_tentativas):
    chance = sorte * n_tentativas
    if chance > 100:
        chance = 100
    sorteado = random.randint(0, 100)
    if sorteado in range(0, chance):
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
    time.sleep(2)
    while vida_jogador > 0 and vida_adversario > 0:
        escolha = input("Digite fugir ou a tecla enter para atacar:")
        n_de_fugas = 0
        if escolha == "fugir":
            n_de_fugas = n_de_fugas + 1
            resultado_fuga = fuga(jogador["sorte"], n_de_fugas)
            if resultado_fuga == True:
                print("Fuga executada com sucesso")
                break
            else:
                print("Seu inspermon nao conseguiu fugir")
        else:
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
                return "VITORIA"
        time.sleep(2)
        if acerto_critico(adversario["sorte"]) == True:
            vida_jogador = vida_jogador - (dano_adversario * 2)
            print("{0}: ATAQUE CRÍTICO! {1} de dano".format(adversario["nome"],
                                                            2 * dano_adversario))
        else:
            vida_jogador = vida_jogador - dano_adversario
            print("{0}: Ataca! {1} de dano".format(adversario["nome"],
                                                   dano_adversario))
        if vida_jogador < 0:
            vida_jogador = 0
        print("{0}: {1} restante de vida".format(jogador["nome"],
                                                 vida_jogador))
        if vida_jogador < 1:
            return "DERROTA"


with open("inspermons.json") as arquivo:
    inspermons = json.load(arquivo)

menu_inicial = input("""Digite 'load' para continuar de onde parou ou
                    'new' para comecar outra vez: """)


if menu_inicial == "load":
    with open("save_game.json") as arquivo:
        data_master = json.load(arquivo)
    insperdex = data_master["insperdex"]
    inspermon_jogador = data_master["jogador"]


elif menu_inicial == "new":
    insperdex = []
    z = 1
    for ipmon in inspermons:
        print("---- {0} ----".format(z))
        print("""Nome: {0}
                 Vida: {1}
                Poder: {2}
               Defesa: {3}
                Sorte: {4}""".format(ipmon["nome"],
                                     ipmon["vida"],
                                     ipmon["poder"],
                                     ipmon["defesa"],
                                     ipmon["sorte"]))
         
        z = z+1
    x_do_jogador = int(input("Digite o número do inspermon escolhido: ")) - 1
    inspermon_jogador = inspermons[x_do_jogador]
    insperdex.append(inspermon_jogador)
    inspermon_jogador["level"] = 1
    inspermon_jogador["xp_atual"] = 0
    print('''Seu inspermon escolhido foi: {0}
                                    Vida: {1}
                                   Poder: {2}
                                  Defesa: {3}
                                   Sorte: {4}'''.format(
                          inspermon_jogador["nome"],
                          inspermon_jogador["vida"],
                          inspermon_jogador["poder"],
                          inspermon_jogador["defesa"],
                          inspermon_jogador["sorte"])) 


while True:


    acao = input("Digite lutar, dormir, insperdex ou salvar:").lower()



    if acao == "dormir":
        break


    elif acao == "lutar":
        inspermon_adversario = random.choice(inspermons)
        if inspermon_adversario not in insperdex:
            insperdex.append(inspermon_adversario)
        time.sleep(2)
        print("""O inspermon adversário é: {0}
                                     Vida: {1}      
                                    Poder: {2}
                                   Defesa: {3}
                                    Sorte: {4}""".format(
                                    inspermon_adversario["nome"],
                                    inspermon_adversario["vida"],
                                    inspermon_adversario["poder"],
                                    inspermon_adversario["defesa"],
                                    inspermon_adversario["sorte"]))
        time.sleep(1)
        resultado_batalha = batalha(inspermon_jogador,inspermon_adversario)
        if resultado_batalha == "DERROTA":
            print("""Seu inspermon foi derrotado,
                            Fim de Jogo""")
            break


        elif resultado_batalha == "VITORIA":
            print("""Seu inspermon venceu!
                  {0} xp recebido""".format(inspermon_adversario["xp_m"]))
            inspermon_jogador["xp_atual"] += inspermon_adversario["xp_m"]
            result_lv = level_up(inspermon_jogador, inspermon_jogador["level"],
                                                 inspermon_jogador["xp_atual"])[0]


            if result_lv == "sim":
                ipmon_novo = level_up(inspermon_jogador,
                                      inspermon_jogador["level"],
                                      inspermon_jogador["xp_atual"])[1]
                inspermon_jogador = ipmon_novo
                print("LEVEL UP! Todos os atributos aprimorados")




    elif acao == "insperdex":
        xp_necessario = 15 + 10 * inspermon_jogador["level"]
        print("               ")
        print("""Seu inspermon: {0}
                          Vida: {1}
                         Poder: {2}
                        Defesa: {3}
                         Sorte: {4}
                            Xp: {5}/{6}
                         Level: {7}""".format(inspermon_jogador["nome"],
                                              inspermon_jogador["vida"],
                                              inspermon_jogador["poder"],
                                              inspermon_jogador["defesa"],
                                              inspermon_jogador["sorte"],
                                              inspermon_jogador['xp_atual'],
                                              xp_necessario,
                                              inspermon_jogador["level"]))
        print("INSPERDÉX")
        for ipmon in insperdex:
            print("-------------------------------------")
            print("""Nome: {0}
                     Vida: {1}
                    Poder: {2}
                   Defesa: {3}
                    Sorte: {4}""".format(ipmon["nome"],
                                         ipmon["vida"],
                                         ipmon["poder"],
                                         ipmon["defesa"],
                                         ipmon["sorte"]))


    elif acao == "salvar":
        save_game = {}
        save_game["jogador"] = inspermon_jogador
        save_game["insperdex"] = insperdex
        with open("save_game.json", "w") as fp:
            json.dump(save_game, fp, indent = 1)
        print("JOGO SALVO!")


    else:
        print("Comando inválido")


