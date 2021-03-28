# read animals.txt
animal_file = open('animals.txt', 'r', encoding='utf-8')
# and write animals_new.txt
animal_new = open('animals_new.txt', 'w', encoding='utf-8')
for line in animal_file:
    animal_new.write(str.rstrip(line) + " ")

animal_file.close()
animal_new.close()
