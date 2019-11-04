filename = 'programming.txt'

with open(filename, 'w') as file_obj:
    file_obj.write("I love programming.\n")
    file_obj.write("I love creating new games.\n")

# 附加到文件
with open(filename, 'a') as file_obj:
    file_obj.write("I also love finding meaning in large datasets.\n")