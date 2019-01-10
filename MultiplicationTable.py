X = 1
Y = 1

message = "Multiplication table from: "+str(min(range(1, 11)))+" to: "+str(max(range(1, 11)))

print("="*(len(message)+1))
print(message)
print("="*(len(message)+1))
print()
print('{:>2}'.format(' '), end= ' ')

for X in range(1, 11):
	if X == 1:
		print('{:>3}'.format(X), end=' ')
	else:
		print('{:>2}'.format(X), end=' ')

print()
print('-'*33)

#print()

for X in range(1,11):
	print('{:>2}'.format(X), end='| ')
	while Y <= 10:
		print('{:>2}'.format(X * Y), end=' ')
		Y += 1
	print()
	Y = 1
