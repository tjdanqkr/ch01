f= open('multilines1.txt', 'w', encoding='utf-8')
for i in range(1,10):

    write_size = f.write("Life is too short\n")
print(write_size)
f.close()