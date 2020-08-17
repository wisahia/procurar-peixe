def procurar_peixe(palavra):
	peixes = open("toda especie de peixe.txt", "r", encoding='utf-8')

	peixes_com_palavra = []

	palavra = palavra

	for peixe in peixes:
		if palavra.lower() in peixe.lower() or palavra == '':
			peixes_com_palavra.append(peixe.replace('\n', ''))

		else:
			continue

	print(*peixes_com_palavra, sep=', ')
	print('\n' + "Existem " + str(len(peixes_com_palavra)).strip() + " peixes com " + palavra + " no nome")


while True:
	procurar_peixe(input("Escolha uma palavra: ").lower())
	print('\n' + '---' + '\n')
