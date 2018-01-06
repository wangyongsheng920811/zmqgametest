#a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
a = [115,121,102,0b1000111000101000110000110111010]
b = []
for i in range(len(a)):
	if i<3:
		b.append(chr(a[i]))
	else:
		b.append(int(a[i]))

