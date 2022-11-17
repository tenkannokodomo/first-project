if __name__ == '__main__':
	words = list()
	x = ''
	while x != "СТОП":
		x = input('Введите новое слово:')
		if x != "СТОП":
			words.append(x)
		else:
			print(words)