with open('pi_digits.txt') as file_obj:
    contents = file_obj.read()
    print(contents)

with open('pi_digits.txt') as file_obj:
    for line in file_obj:
        print(line.rstrip())

file_name = 'pi_digits.txt'

with open(file_name) as file_obj:
    lines = file_obj.readlines()

for line in lines:
    print(line.rstrip())