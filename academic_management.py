turmas = []
alunos = []
professores = []

def adicionar_turma(codigo, disciplina):
    dicionarioTurma = {
        "codigo" : codigo,
        "disciplina" : disciplina,
        "alunos" : [],
        "professor" : None
    }
    turmas.append(dicionarioTurma)
    pass
def adicionar_aluno(nome, matricula):
    dicionarioAluno = {
        "nome" : nome,
        "matricula" : matricula
    }
    alunos.append(dicionarioAluno)
    pass
def adicionar_professor(nome, disciplina):
    dicionarioProfessor = {
        "nome" : nome,
        "disciplina" : disciplina
    }  
    professores.append(dicionarioProfessor)
    pass
def atribuir_aluno_turma(turma, aluno):
    for dicionarioLocalTurma in turmas:
        if dicionarioLocalTurma["codigo"] == turma:
            indexTurma = turmas.index(dicionarioLocalTurma)
            listaAlunos = dicionarioLocalTurma["alunos"]
            for dicionarioLocalAluno in alunos:
                if dicionarioLocalAluno["nome"] == aluno:
                    listaAlunos.append(dicionarioLocalAluno)
                    dicionarioLocalTurma["alunos"] = listaAlunos
            turmas[indexTurma] = dicionarioLocalTurma
    pass
def atribuir_professor_turma(turma, professor):
    for dicionarioLocalTurma in turmas:
        if dicionarioLocalTurma["codigo"] == turma:
            indexTurma = turmas.index(dicionarioLocalTurma)
            for dicionarioLocalProfessor in professores:
                if dicionarioLocalProfessor["nome"] == professor:
                    dicionarioLocalTurma["professor"] = dicionarioLocalProfessor
            turmas[indexTurma] = dicionarioLocalTurma
    pass
def ler_turmas():
    print("Lista de turmas: ")
    for turma in turmas:
        print("\t{}".format(turma["codigo"]))
        print("\t\tDisciplina: {}".format(turma["disciplina"]))
        print("\t\tAlunos:")
        try:
            for aluno in turma["alunos"]:
                print("\t\t\t{} \n\t\t\t\tMatricula: {}\n".format(aluno["nome"], aluno["matricula"]))
            if len(turma["alunos"]) == 0:
                print("\t\t\tNenhum aluno encontrado")
        except:
            print("\t\t\tNenhum aluno encontrado")
        print("\t\tProfessor:")
        try:
            if turma["professor"] == None:
                print("\t\t\tNenhum professor encontrado") 
            else:
                print("\t\t\t{} \n\t\t\t\tDisciplina: {}\n".format(turma["professor"]["nome"], turma["professor"]["disciplina"]))
        except:
            print("\t\t\tNenhum professor encontrado")      
    print("\n")      
def ler_alunos():
    print("\nLista de Alunos:")
    try:
        for aluno in alunos:
            print("\t{} \n\t\tMatricula: {}\n".format(aluno["nome"], aluno["matricula"]))
    except:
        print("\t\tNenhum Aluno encontrado")
        print("\n")  
def ler_professores():
    print("\nLista de professores:")
    try:
        for professor in professores:
            print("\t{} \n\t\tDisciplina: {}\n".format(professor["nome"], professor["disciplina"]))
    except:
        print("\t\tNenhum professor encontrado")
        print("\n")  
def menu(selecao):
    match selecao:
        case "1":
            codigo = input("Insira o código da turma: ")
            disciplina = input("Insira a disciplina da turma: ")
            print("\n")
            adicionar_turma(codigo, disciplina)
        case "2":
            nome = input("Insira o nome do aluno: ")
            matricula = input("Insira a matricula do aluno: ")
            print("\n")
            adicionar_aluno(nome, matricula)
        case "3":
            nome = input("Insira o nome do professor: ")
            disciplina = input("Insira a disciplina do professor: ")
            print("\n")
            adicionar_professor(nome, disciplina)
        case "4":
            ler_turmas()
            turma = input("Insira o codigo da turma que deseja selecionar: ")
            ler_alunos()
            aluno = input("Insira o nome do aluno que deseja inserir: ")
            print("\n")
            atribuir_aluno_turma(turma, aluno)
        case "5":
            ler_turmas()
            turma = input("Insira o codigo da turma que deseja selecionar: ")
            ler_professores()
            professor = input("Insira o nome do professor que deseja inserir: ")
            print("\n")
            atribuir_professor_turma(turma, professor)
        case "6":
            print("\n")
            ler_turmas()
        case "7":
            print("\n")
            ler_alunos()
        case "8":
            print("\n")
            ler_professores()
        case "0":
            quit()
        case _:
            print("Valor informado é invalido")
def main():
    while True:
        print("\n")
        print("[1] - Inserir turma")
        print("[2] - Inserir aluno")
        print("[3] - Inserir professor")
        print("[4] - Atribuir aluno a turma")
        print("[5] - Atribuir professor a turma")
        print("[6] - Visualizar turmas")
        print("[7] - Visualizar alunos")
        print("[8] - Visualizar professores")
        print("[0] - Sair")
        
        selecao = input("Insira o valor da seleção: ")
        print("\n")
        menu(selecao)

if __name__ == '__main__':
    main()