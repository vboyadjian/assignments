# REading a text file
with open('victor.txt') as f:
	full_text = f.read()

print(full_text + "Victor")
#writing a text file
with open('victor.txt', 'w') as f:
    f.write('hello, my name is')
    f.write('\n')
