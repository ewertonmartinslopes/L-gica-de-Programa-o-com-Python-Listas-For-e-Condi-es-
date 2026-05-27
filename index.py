#Atividade 1 - Cadastro de nomes

# nome=[]

# for i in range(5):
#     nome.append(input("Digite um nome: "))
# print("Os nomes cadastrados foram: ")
# for i in range(5):    
#    print(nome[i])

#Atividade 2 - Remover e adicionar elementos em uma lista

# frutas=["maçã", "banana", "laranja", "uva", "pera"]
# frutas.remove("uva")
# frutas.append("morango")
# print(frutas)

#Atividade 3 - Soma de números

# numeros=[]
# soma=0
# for i in range(5):
#     numeros.append(int(input("Digite um número: ")))
#     soma += numeros[i]
# print(f"A soma dos números é: {soma}")


#atividade 4 - Números pares

# numeros=[]
# for i in range(10):
#     numeros.append(int(input("Digite um número: ")))
# for i in range(10):
#     if numeros[i] % 2 == 0:
#         print(f"O número {numeros[i]} é par.")

#Atividade 5 - Verificação de aluno aprovado ou reprovado

# notas=[]
# for i in range(4):
#     notas.append(float(input("Digite uma nota: ")))
# media = sum(notas) / len(notas)
# print(f"A média das notas é: {media}")
# if media >= 7:
#     print("O aluno foi aprovado.")
# else:
#     print("O aluno foi reprovado.")

#Atividade 6 - Pesquisa em lista

# alunos=["João", "Maria", "Pedro", "Ana", "Lucas"]
# nome = input("Digite o nome do aluno que deseja pesquisar: ")
# if nome in alunos:
#     print("O aluno está na lista.")
# else:
#     print("O aluno não está na lista.")

#Atividade 7 - Contagem de elementos em uma lista

# numeros=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(f"A lista contém {len(numeros)} elementos.")
# print(f"O maior número da lista é: {max(numeros)}")
# print(f"O menor número da lista é: {min(numeros)}")

#Atividade 8 - Sistema simples de tarefas

# tarefas=[]
# for i in range(3):
#     tarefa = input("Digite uma tarefa: ")
#     tarefas.append(tarefa)
# print("Tarefas cadastradas:")
# for i in range(3):
#     print(f"{i+1}. {tarefas[i]}")
# tarefa_remover = int(input("Digite o número da tarefa que deseja remover: "))
# if 1 <= tarefa_remover <= len(tarefas):
#     tarefas.pop(tarefa_remover - 1)
#     print("Tarefa removida com sucesso.")
#     print("Tarefas restantes:")
#     for i in range(len(tarefas)):
#         print(f"{i+1}. {tarefas[i]}")
# else:
#     print("Número inválido.")