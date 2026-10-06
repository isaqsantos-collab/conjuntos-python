# conjuntos_exemplos.py
# Exemplos de conjuntos (set) em Python

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Conjunto A:", A)
print("Conjunto B:", B)

# União
print("União:", A | B)

# Interseção
print("Interseção:", A & B)

# Diferença
print("A - B:", A - B)
print("B - A:", B - A)

# Diferença simétrica
print("Diferença simétrica:", A ^ B)

# Adicionando elemento
A.add(10)
print("A após adicionar 10:", A)

# Removendo elemento
A.remove(10)
print("A após remover 10:", A)

# Verificando se um elemento pertence ao conjunto
print("3 pertence a A?", 3 in A)
print("10 pertence a A?", 10 in A)

# Subconjunto
C = {1, 2}

print("C é subconjunto de A?", C.issubset(A))
print("A é superconjunto de C?", A.issuperset(C))

# Exemplo com nomes
turma_a = {"Ana", "Bruno", "Carlos", "Diana"}
turma_b = {"Carlos", "Diana", "Eduardo", "Fernanda"}

print("\n--- Exemplo com alunos ---")

print("Turma A:", turma_a)
print("Turma B:", turma_b)

print("Alunos das duas turmas:", turma_a & turma_b)
print("Todos os alunos:", turma_a | turma_b)
print("Somente da turma A:", turma_a - turma_b)
print("Somente de uma das turmas:", turma_a ^ turma_b)
