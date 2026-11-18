print("Bem-vindo(a)!")
print("Eu sou 4U, muito prazer 🤖🖖")
input("Pressione Enter para continuar")
while True:
    print("Qual seu nome?")
    nome = input().strip()
    
    if len(nome) == 0:
        print("Digite pelo menos uma letrinha poxa 🤖💔")
    elif len(nome) <= 15:
        print ("Olá", nome, "estava a sua espera 🤖👐")
        input("Pressione Enter para continuar")
        break
    else:
        print("Malz mas o nome deve ter no máximo 15 caracteres! 🤖⛔️")
        
print("como vc esta se sentindo hj ", nome, "? 🤖🩺")
print("1) Bem, 2) Mais ou menos, 3) to tristão")
while True:
    emocao = input().lower()
    if emocao in ["1"]:
        print("Que bom saber disso ", nome, " ! ✨🤖✨")
        input("Pressione Enter para continuar")
        break
    elif emocao in ["2"]:
        print("Entendo ", nome," posso tentar melhorar seu humor 🤖🔧")
        input("Pressione Enter para continuar")
        break
    elif emocao in ["3"]:
        print("Lamento ouvir isso ", nome, " a vida pode ser chata quando estamos desmotivados...🤖 ☔")
        input("Pressione Enter para continuar")
        break
    else:
         print("Digite o numero de uma das alternativas acima ", nome, " 🤖❗")

print("Aí...quer saber de uma coisa ", nome, "?")
print("Eu só existo por sua causa, sabia?")
input("Pressione Enter para continuar")
print("Sim ou Não")
while True:
    resp = input().lower()
    if resp in ["sim", "s"]:
        print("Ah é?...🤖🥀")
        print("Então você sabe muito! ⚡️🧠⚡️") #Inserir a imagem do meme "Eu sabo muito"
        input("Pressione Enter para continuar")
        break
    elif resp in ["não", "n", "nao"]:
        print("Bom, agora você sabe 🤖ººº{😉}")
        input("Pressione Enter para continuar")
        break
    else:
        print(nome, " responda com 'sim' ou 'não', ou apenas 's' ou 'n' 🤖⛔")

print("Mas é serio ", nome)
print("Não sou bom com palavras...🤖💧")
print("Pra deixar claro o quero dizer, veja esse video abaixo 🤖👇")
input("Pressione Enter para assitir ao video")
#inserir video aqui e apos o fim do video aparcer o botao para continuar para proxima linha

print("O que você achou? 🤖👉👈")
print("1- Fofinho 🥹 2- Esperava mais 🥱")
while True:
    opcao = input()
    if opcao == "1":
        print("Fico feliz que gostou! 🤖🫶")
        input("Pressione Enter para continuar")
        break
    elif opcao == "2":
        print("Então faz melhor! 🤖🖕")
        input("Pressione Enter para continuar")
        print("Coé pa ri, #resenha #humor 🤖🫶")
        input("Pressione Enter para continuar")
        break
    else:
        print("Digite 1 ou 2 criatura 🤖⛔")

print("Bom era isso...vlw por ter me dado motivação pra fazer tudo isso...")
print("Vou continuar me esforçando cada vez mais pra tentar te fazer feliz 🤖🫶")
input("Pressione Enter para continuar")
print("Mesmo você maltratando meu precioso 🤖👉🥚🥚")
input("Pressione Enter para continuar")
#inserir um botão para mostrar baloes subindo na tela
print("❤️❤️❤️TE AMO❤️❤️❤️")
    
        
    
