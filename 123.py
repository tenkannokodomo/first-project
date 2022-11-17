if __name__ == '__main__':
	words = [22, 1, 12, 36, 14]
	fruits = ["apple", "raspberry", "banana"]

	words2 = words.copy() #copiya

	words.clear() #chistit spisok

	print(words)
	print(words2)

	print(fruits.index("raspberry")) #pishet index

	fruits.pop(x) #udalil last x - index

	words.extend(fruits) #soedenyaet spiski words + fruits
	print(words2.count(33)) #schetaen elementi v spiske

	words2.insert(0, 33) #menyaet 1 element na 33

	x=5
	y=2
	print(x/y)
	print(x//y) #целочисленное деление

	arr = list() #создает пустой список

	len() #длинна массива
	
	print(fruit, end=' ') #в строчку чтобы