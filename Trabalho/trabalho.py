#Eluan de Vargas Marzola Cardoso e Victor Augusto Doim
#O programa que você desenvolverá irá receber como entrada um arquivo de texto (.txt) contendo vários conjuntos de dados e várias operações. Estas operações e dados estarão representadas em um arquivo de textos contendo apenas os dados referentes as operações que devem ser realizadas segundo a seguinte regra fixa: a primeira linha do arquivo de texto de entrada conterá o número de operações que estão descritas no arquivo, este número de operações será um inteiro; as linhas seguintes seguirão sempre o mesmo padrão de três linhas: a primeira linha apresenta o código da operação (U para união, I para interseção, D para diferença e C produto cartesiano), a segunda e terceira linhas conterão os elementos dos conjuntos separados por virgulas.
f = open('2.txt', 'r')
i = 0
conjunto1 = set()
conjunto2 = set()
conjunto3 = set()
conjunto4 = set()
conjunto5 = set()
conjunto6 = set()
conjunto7 = set()
conjunto8 = set()

for linha in f:
    if not linha or linha.startswith('#'):
        continue
    if 'U' in linha:
        conj_1 = f.readline().strip().split(',')
        conj_2 = f.readline().strip().split(',')
        conjunto1.update(conj_1)
        conjunto2.update(conj_2)
        uniao = conjunto1.union(conjunto2)
        print("União: conjunto 1 :", conjunto1, "conjunto 2 :", conjunto2, "Resultado:", uniao)
    elif 'I' in linha:
        conj_3 = f.readline().strip().split(',')
        conj_4 = f.readline().strip().split(',')
        conjunto3.update(conj_3)
        conjunto4.update(conj_4)
        intersecao = conjunto3.intersection(conjunto4)
        print("Interseção: conjunto 1 :", conjunto3, "conjunto 2 :", conjunto4, "Resultado:", intersecao)
    elif 'D' in linha:
        conj_5 = f.readline().strip().split(',')
        conj_6 = f.readline().strip().split(',')
        conjunto5.update(conj_5)
        conjunto6.update(conj_6)
        diferenca = conjunto5.difference(conjunto6)
        print("Diferença: conjunto 1 :", conjunto5, "conjunto 2 :", conjunto6, "Resultado:", diferenca)
    elif 'C' in linha:
        conj_7 = f.readline().strip().split(',')
        conj_8 = f.readline().strip().split(',')
        conjunto7.update(conj_7)
        conjunto8.update(conj_8)
        produto_cartesiano = [(x, y) for x in conjunto7 for y in conjunto8]
        print("Interseção: conjunto 1 :", conjunto7, "conjunto 2 :", conjunto8, "Resultado:", produto_cartesiano)