# Módulo: Os 20% de código que dão 80% de resultado
# Tema 1: Mais do Que Strings

# Strings
print('Hello world.')               # String com aspas simples
print("This is Alice'sgreeting.")   # String com aspas duplas (não tem diferença)
print('This is Bob\'s greeting')    # String com aspas simples com aspas de texto tendo que fazer o scape

print('')

print("Strings são ojetos dos tipo String")
nome = 'cAsSio'     # Strings são objetos
print(type(nome))   # Imprimi o tipo do objeto, neste caso (class 'str')

sobrenome = str('Damacena')      # Instanciando a classe string
print(sobrenome)

print(nome.encode())        # Em python todas as strings são unicode (b de byte)
print(type(nome.encode()))  # Tipo de objeto bytes

print("String unicode com cárectes especiais")
print("Cássio".encode())        # Em python todas as strings são unicode (b de byte)
print("Káçio".encode())        # Strings são objetos com todas as complexidades do unicode

print()

print("Métodos Strings")
print(dir(nome))
print(dir(str))


nome = 'cAsSio damacena'     # Strings atualizada
print()
print("Observação: strings são imutáveis, logo, cada operado com String gera uma nova string")
print("String original: " + nome + "  | Função Upper => " + nome.upper() + " <= Passa tudo para maiúsculo")
print("String original: " + nome + "  | Função title => " + nome.capitalize() + " <= Primeira letra para maiúsculo")
print("String original: " + nome + "  | Função title => " + nome.title() + " <= Primeira letra de cada palavra maiúsculo")
print("String original: " + nome + "  | Função replace => " + nome.replace('a', 'A') + " <= Troca os caracteres")
print("String original: " + nome + "  | Função len => " + str(len(nome)) + " <= Exibe o tamanho da string")
print("String original: " + nome + "  | Função lower => " + nome.lower() + " <= Passa tudo para minúsculo")
print("String original: " + nome + "  | Função count => " + str(nome.count('a')) + " <= Conta quantas ocorrências do valor passado por parâmetro")


print("String original: " + nome + "  | Função split <= Desmembra uma string numa lista de Strings com delimitador padrão como espaço")
print(nome.split())
print("String original: " + nome + "  | Função split <= trocar delimitados po A")
print(nome.split('a'))

print()
print("Concatenação com '+' é inviável em grande quantidade. Utiizar join()")
# Join é eficiente porque ele verifica o tamanho de cada string já com delimitador
# O python já aloca um espaço de memória para uma passagem só
nome = "Cassio"
nome_do_meio = "Pereira"
ultmo_nome = "Damacena"
print(' '.join([nome, nome_do_meio, ultmo_nome]) + " => String concatenada com Join e linha única separa com espaço")
print('\n'.join([nome, nome_do_meio, ultmo_nome]) + " \n=> String concatenada com Join e em quebra de linha ")
