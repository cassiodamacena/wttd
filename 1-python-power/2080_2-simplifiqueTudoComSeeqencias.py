# Módulo: Os 20% de código que dão 80% de resultado
# Tema 2: Simplifique tudo em Sequências

nome = 'Cassio'

print("Strings também são sequências")
print("Função len() exibe o tamanho da sequênica :: " + str(len(nome)))

print()
print("Pemite acessar por índice 'nome[0]' primeiro caracter :: " + nome[0])
print("Obs.: Não é um CHAR, mas uma String de somente um elmento")

print()
print("nome[1] segundo elemento 'e' :: " + nome[1])

print()
print("nome[len(nome)-1] último elemento 'e' :: " + nome[len(nome)-1])
print("nome[-1] último elemento 'o' :: " + nome[-1])    # Último elemento de forma resumida

print()
print("nome[0:4] slice/fatia de 0 até 4 (não incluso) :: " + nome[0:4])
print("nome[1:-1] slice/fatia de 1 até -1 (não incluso) :: " + nome[1:-1])
print("nome[1:len(nome)] slice/fatia de 1 até último índice :: " + nome[0:len(nome)])
print("nome[:4] slice/fatia de 0 até 4 :: " + nome[:4])
print("nome[:] toda a sequência:: " + nome[:])

print()
print("Sequência com PASSO start/stop/step 'nome[1:6:2] :: " + nome[0:6:2])
print("Sequência com PASSO start/stop/step 'nome[::2] :: " + nome[::2])     # Forma simplificada
print("Sequência invertida start/stop/step 'nome[::2] :: " + nome[::-1])     # Forma simplificada

print()
print("Açucar sintático da String")
print("nome[0] é o mesmo que nome.__getitem__(0) :: ")
print("nome[0]             :: " + nome[0])
print("nome.__getitem__(0) :: " + nome.__getitem__(0))

print()
index = slice(1, -1, 2)
print("Objeto slice    'index = slice(1, -1, 2)' :: " + str(type(index)))
print("nome[index]             :: " + nome[index])
print("nome.__getitem__(index) :: " + nome.__getitem__(index))

print()
print("*** RESUMO Slice***")
print("Ao fazer 'nome[1, -1, 2]'                     :: " + nome[1:-1:2])
print("O python faz nome.__getitem__(slice(1, -1, 2) :: " + nome.__getitem__(slice(1, -1, 2)))
