#----------------------------------------------------------------------------------------------------------------
class Ordenador:

    def selecao_direta(self, lista):
        fim = len(lista)
        for i in range (fim-1):
            #inicialmente o menor elemento é o i-ésimo
            posicao_minimo = i
            #começa a verificar depois do i e vai até o fim
            for j in range (i+1, fim):
                if lista[j] < lista[posicao_minimo]:
                    posicao_minimo = j
            #Coloca o menor encontrado no início da sub-lista (i+1 até fim)
            #trocando os elementos nas posições i e posicao_minimo
            lista[i], lista[posicao_minimo] = lista[posicao_minimo], lista[i]
        if teste(lista):
            return lista
        else:
            print("A lista não foi ordenada... :(")

    def bolha (self, lista):
        fim = len(lista)
        for i in range (fim-1, 0, -1):#vai do final até o 0, decrementando de 1 em 1
            for j in range (i):
                if lista[j]>lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j] #troca de lugares
        if teste(lista):
            return lista
        else:
            print("A lista não foi ordenada... :(")

    def insercao(self, lista):
         j = 1
         while j<len(lista):
            x = lista[j]
            i = j-1
            while i>=0 and lista[i]>x: #vai procurando o lugar do x, da dir para a esq, para coloca-lo na frente do ultimo numero menor que ele
                lista[i+1] = lista[i]
                i -= 1
            lista[i+1] = x
            j += 1
         if teste(lista):
             return lista
         else:
            print("A lista não foi ordenada... :(")
#----------------------------------------------------------------------------------------------------------------
def teste(lista): #ver se a lista está em ordem crescente
    i = len(lista)-1
    while i > 0:
        if lista[i]<lista[i-1]:
            return False
        i -= 1
    return True
#----------------------------------------------------------------------------------------------------------------
import random
def lista_aleatoria(n):
        lista = [random.randrange(-200, 200) for x in range(n)]
        # cria uma lista com n elementos inteiros aleatórios de -200 a 199
        return lista      
#----------------------------------------------------------------------------------------------------------------
import time 
def main():
    quantidades = [1000, 2500, 5000]
    for i in quantidades:
        print ("\n\n#TESTE COM %d ITENS NA LISTA#\n"%i)
        lista1 = lista_aleatoria(i)
        lista2 = lista1[:] #clona a lista 1 para a lista 2. Cada uma será ordenada através de um método diferente.
        lista3 = lista1[:] 
        o = Ordenador()
        print("Lista a ser ordenada:", lista1)
        
        print ("\nMétodo de Seleção Direta:")
        antes = time.time() #começa a contar o tempo
        l1 = o.selecao_direta(lista1)
        #print("Lista ordenada:", l1) #seleção direta é método de o
        depois = time.time() #para o cronômetro
        tempo_selecao = depois-antes
        print ("Tempo de execução:%f segundos"%tempo_selecao)
        
        print ("\nMétodo Bolha:")
        antes = time.time() #começa a contar o tempo
        l2 = o.bolha(lista2)
        #print("Lista ordenada:", l2)
        depois = time.time() #para o cronômetro
        tempo_bolha = depois-antes
        print ("Tempo de execução:%f segundos"%tempo_bolha)

        print ("\nMétodo de Inserção:")
        antes = time.time() #começa a contar o tempo
        l3 = o.insercao(lista3)
        #print("Lista ordenada:", l3)
        depois = time.time() #para o cronômetro
        tempo_insercao = depois-antes
        print ("Tempo de execução:%f segundos"%tempo_insercao)

        if tempo_selecao<tempo_bolha and tempo_selecao<tempo_insercao:
            print ("O Método de Seleção Direta é o melhor método para este caso.")
        if tempo_bolha<tempo_selecao and tempo_bolha<tempo_insercao:
            print ("O Método Bolha é o melhor método para este caso.")
        if tempo_insercao<tempo_bolha and tempo_insercao<tempo_selecao:
            print ("O Método de Inserção é o melhor método para este caso.")
        
main()

