from os import system
import sys
phrase = ' '.join(sys.argv[1:])
phrase = list(phrase)

system("clear")

for i in range(len(phrase)):
    if (i + 1) % 2 == 0:
        phrase[i] = phrase[i].capitalize()

phrase = ''.join(phrase)

print()
print()
print()
print()
print()
print()
print()
print()
print(phrase)
print()
print()
print()
print()
print()
print()
print()
print()
