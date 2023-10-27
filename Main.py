# Estrutura Condicional -- código mais simples
from datetime import date
ano_analisado = int(input("Que ano gostaria de analisar?: "))

if ano_analisado == 0:
    ano_analisado = date.today().year  
    # Quando o usuario responde o ano como 0, o computador indica se o ano atual é bissexto ou não
if ano_analisado % 4 == 0:
    print(f"O ano {ano_analisado} é Bissexto")
elif ano_analisado % 100 != 0:
    print(f"O ano {ano_analisado} é Bissexto")
elif ano_analisado % 400 == 0:
    print(f"O ano {ano_analisado} é Bissexto")
else:
    print(f"{ano_analisado} Não é Bissexto")




