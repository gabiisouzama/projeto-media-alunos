# media.py
# Programa simples para calcular a média das notas de um aluno

def calcular_media(nota1, nota2, nota3):
    # Calculando a média simples
    media = (nota1 + nota2 + nota3) / 3
    return media

# Recebendo as notas do aluno
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calculando a média
media = calcular_media(nota1, nota2, nota3)

# Exibindo o resultado
print(f"A média das notas é: {media:.2f}")
