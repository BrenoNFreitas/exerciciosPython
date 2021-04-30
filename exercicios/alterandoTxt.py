arqTxt = open("testeALT.txt", "r")
lendoArq = arqTxt.read()
print(lendoArq) #mostrando o conteúdo do arquivo txt

with open('testeALT.txt', 'w') as arqTxt:
    arqTxt.write(input("insira um novo conteúdo para o arquivo: ")) #alterando
    arqTxt.close()
    
with open('testeALT.txt') as arqTxt:
    print(arqTxt.read()) #mostrando o conteúdo do arquivo txt após ser alterado