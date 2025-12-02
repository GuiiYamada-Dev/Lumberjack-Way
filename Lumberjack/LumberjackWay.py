from inputimeout import inputimeout, TimeoutOccurred

def inicio():
    print('🪓 Boas vindas ao caminho do lenhador! 🪓')
    print('Seu objetivo é chegar em segurança em casa.')
    print('Mas cuidado... nem tudo é o que parece ser...\n')

def pegar_machado():
    try:
        resposta = inputimeout(prompt="Pegar o machado? (s/n) ", timeout=10).strip().lower()
    except TimeoutOccurred:
        print("Você hesitou e deixou o machado para trás.")
        return False

    if resposta.startswith("s"):
        print("Você pegou o machado!")
        return True
    else:
        print("Você deixou o machado para trás.")
        return False

def arvores():
    print('🌳 Enquanto trabalhava como lenhador no topo da montanha, você ouve um grito...')
    print('Ele vem da sua casa, onde sua filha o aguarda sozinha. 💒\n')
    print('[1] Ignorar (pode ter sido sua imaginação)')
    print('[2] Descer calmamente a montanha')
    print('[3] Descer em toda velocidade\n')

    escolha = input("O que o lenhador irá fazer? ")

    if escolha == "1":
        print("\nVocê ignorou o grito e seguiu seu dia normalmente...")
        print("Ao chegar em casa... tarde demais.")
        print("Sua filha teve o mesmo destino trágico que sua esposa.")
        return "perdeu"

    elif escolha == "2":
        print("\nPreocupado, mas tentando manter a calma, você decide descer.")
        print("Antes de partir, pensa em levar o machado...\n")
        tem_machado = pegar_machado()
        return "machado" if tem_machado else "sem_machado"

    elif escolha == "3":
        print("\nVocê desce a montanha correndo, tomado pelo desespero!")
        return "correu"

    else:
        print("Escolha inválida.")
        return arvores()  # chama de novo até o jogador digitar certo




    