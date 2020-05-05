def mensagem(ano,string):
    print("O ano",ano,string)

def ehBissexto(ano):
    if(ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 ):
        if(ano >= 2018):
            mensagem(ano,"serah bissexto")
        else:
            mensagem(ano,"foi bissexto")
    else:
        mensagem(ano,"NAO eh bissexto")

def contaDigitos(ano):
    string = str(ano)
    if(len(string) != 4):
        print("Ano invalido")
    else:
        ehBissexto(ano)

list = []
list = input().split(" ")
list = [int(i) for i in list]
for x in list:
    contaDigitos(x)




