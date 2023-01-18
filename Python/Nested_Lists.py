if __name__ == '__main__':
    listaNotas = []
    listaAlunosComNotas = []
    menor = 100
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        listAluno = []
        listAluno.append(name)
        listAluno.append(score)
       
        listaAlunosComNotas.append(listAluno)
        listaNotas.append(score)
        
    listaNotas = list(set(listaNotas))
    listaNotas.sort()
    segundoMenor = listaNotas[1]
    
    listaNomes = []
    for aluno in listaAlunosComNotas:
        if((aluno[1] == segundoMenor)):
            listaNomes.append(aluno[0])
        
    listaNomes.sort()
    for x in listaNomes:
        print(x)