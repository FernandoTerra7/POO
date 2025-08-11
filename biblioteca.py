class Livro:
    def __init__(self, titulo,  autor):
        self.titulo = titulo
        self.autor = autor

def main():
    #criar lista de livros disponíveis
    livros = [
        Livro("Dom Casmurro", "Machado de Assis"),
        Livro("Senhor dos Anéis", "J. R. R. Tolkim"),
        Livro("Harry Potter", "J. K. Rowling"),
        Livro("Café com Deus Pai", "Junior Rostirola"),
        Livro("A menina que roubava livros", "Markus Zusak"),
        Livro("Assassinato do expresso oriente", "Agatha Christie"),
        Livro("Fogo e sangue", "George RR Martin"),
        Livro("O pequeno príncipe", "Antonio de Saint-Exupéry"),
        Livro("Jogos vorazes", "Suzanne Collins"),
        Livro("Quem é você, Alaska?", "João Verde")
    ]

    #solicitar nome do usário
    nome= input("Digite o seu nome: ")

    #exibir lista de livros disponíveis
    print("\n Livros disponíveis para empréstimo: ")
    for i, livro in enumerate(livros, start=1):
        print(f" {i}. {livro.titulo} - {livro.autor}")

    #solicitar a escolha do livro pelo usuário
    while True:
        escolha = int(input("\n Digite o número do livro que deseja pegar emprestado: "))

        if 1 <= escolha <= len(livros):
            livro_selecionado = livros[escolha -1]
            break
        else:
            print(f"Por favor, digite um número entre 1 e {len(livros)}.")

    print(f"\n Empréstimo confirmado!")
    print(f"{nome} pegou emprestado o livro '{livro_selecionado.titulo}' de {livro_selecionado.autor}.")

main()  

