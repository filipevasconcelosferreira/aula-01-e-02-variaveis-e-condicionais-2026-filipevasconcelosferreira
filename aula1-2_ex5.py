"""
#### Exercício 3 - Identificar se a variante está no gene BRCA1 - Versão 2.

Receba 3 inputs do usuário:
1) O cromossomo de uma variante. Ele virá escrito como texto e da seguinte forma "chr1", "chr2", etc.
2) A posição dessa variante. Será um número inteiro.
3) O genoma de referência dessa variante. Considere só 2 opções possíveis, "hg19" e "hg38".

Responda:
"Sim" se ela estiver no BRCA1.
"Não" se ela não estiver.

Considere que a variante está no gene BRCA1 se estiver no cromossomo 17 (chr17), e:
1) Se a posição estiver no intevalo de 41196312 a 41277500, caso o genoma de referência seja o "hg19".
2) Se a posição estiver no intevalo de 43044295 a 43125483, caso o genoma de referência seja o "hg38".

Obs: Tirei a Location daqui: https://grch37.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000012048;r=17:41196312-41277500

Exemplos:

----------------------------------

Digite o cromossomo: chr17
Digite a posição: 41196313
Digite o genoma de referência: hg38

Resposta:
Não

----------------------------------

Digite o cromossomo: chr17
Digite a posição: 41196313
Digite o genoma de referência: hg19

Resposta:
Sim

----------------------------------

Digite o cromossomo: chr17
Digite a posição: 43044299
Digite o genoma de referência: hg38

Resposta:
Sim

----------------------------------

Digite o cromossomo: chr2
Digite a posição: 43044299
Digite o genoma de referência: hg38

Resposta:
Não

"""

prefixo = "chr"
cromossomos = ["{}{}".format(prefixo, i) for i in range(1,23)]
cromossomos.append("chrM")
cromossomos.append("chrF")

#print(cromossomos)

genomas = ["hg19", "hg38"]

cromossomo_escolhido = input(f"Digite o cromossomo ({', '.join(cromossomos)}): ")
posição_escolhida = int(input("Digite a posição: "))
genoma_escolhido = input(f"Digite o genoma de referência ({', '.join(genomas)}): ")

while cromossomo_escolhido == "chr17":
    if (posição_escolhida >= 41196312 and posição_escolhida <= 41277500) and (genoma_escolhido == "hg19"):
        print("\nResposta:\nSim")
    elif (posição_escolhida >= 43044295 and posição_escolhida <= 43125483) and (genoma_escolhido == "hg38"):
        print("\nResposta:\nSim")
    else:
        print("\nResposta:\nNão")
    break

if cromossomo_escolhido != "chr17":
    print("\nResposta:\nNão")




"""""

prefixo = "Item_"
lista_automatizada = ["{}{}".format(prefixo, i) for i in range(1, 11)]

print(lista_automatizada)


frutas = ["maçã", "banana", "laranja"]
escolha = input(f"Escolha uma fruta ({', '.join(frutas)}): ").lower()


if escolha in frutas:
    print(f"Você escolheu: {escolha}")
else:
    print("Fruta não encontrada.")
"""