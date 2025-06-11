def calcular_media(notas):
    return sum(notas) / len(notas)

def main():
    # Solicitar o número de alunos
    num_alunos = int(input("Digite o número de alunos: "))
    
    # Inicializar variáveis
    total_media_turma = 0
    alunos = []

    # Loop para coletar dados dos alunos
    for _ in range(num_alunos):
        nome = input("Digite o nome do aluno: ")
        notas = []
        
        # Coletar três notas
        for i in range(1, 4):
            nota = float(input(f"Digite a nota {i} do aluno {nome}: "))
            notas.append(nota)
        
        # Calcular a média do aluno
        media = calcular_media(notas)
        total_media_turma += media
        
        # Verificar aprovação
        if media >= 7.0:
            status = "Aprovado"
        else:
            status = "Reprovado"
        
        # Armazenar informações do aluno
        alunos.append((nome, notas, media, status))
    
    # Exibir resultados
    print("\nResultados:")
    for aluno in alunos:
        nome, notas, media, status = aluno
        print(f"Nome: {nome}, Notas: {notas}, Média: {media:.2f}, Status: {status}")
    
    # Calcular e exibir a média geral da turma
    media_geral = total_media_turma / num_alunos
    print(f"\nMédia geral da turma: {media_geral:.2f}")

if __name__ == "__main__":
    main()