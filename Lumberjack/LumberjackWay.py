from inputimeout import inputimeout, TimeoutOccurred

def inicio():
    print('🪓Boas vindas ao caminho do lenhador! 🪓')
    print('Seu objetivo é chegar em segurança em casa.')
    print('Mas cuidado... nem tudo é o que parece ser...')

def arvores():
    print('🌳Enquanto fazia eu trabalho como lenhador no topo da montanha, você ouve um grito...')
    print('Ele vem diretamente de sua casa onde sua filha o aguarda sozinha.💒')
    print('O que ira fazer? [1] Ignorar, pois pode ter sido sua imaginação, [2] Descer a montanha calmamente, [3] Descer a montanha em toda velocidade.')
    escolha = input("O que o lenhador irá fazer? ")

    if escolha == "1":
        print("Você continua seu trabalho normalmente, e vai para casa em seu horario padrão! Parábens, você conseguiu...")
        print("Conseguiu ser um inutil e deixar a sua unica filha ser morta brutalmente, assim como sua esposa, você realmente não consegue salvar ninguem não é mesmo?")
        return "idiota"
    if escolha == "2":
        print("Apesar de preocupado, vc vai para casa calmamente, encerra seus trabalhos de lenhador por hoje e parte em direção a sua casa.")
        print("Antes de sair você pensa em levar o machado contigo...")
        def pegar_machado():
            try:
                resposta = inputimeout(prompt="Pegar o machado? ", timeout=10).strip().lower()
            except TimeoutOccurred:
                print("Você hesitou e deixou o machado para trás.")
                return False
            if resposta.startswith("s"):
                  print("Você pegou o machado!")
                  return "Pegou1"
            else:
                print('Você deixou o machado para tras.')
                return "Deixou1"
        tem_machado = pegar_machado()

inicio()
resultado = arvores()

        
 




    