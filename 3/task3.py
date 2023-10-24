
f = open('text_3_var_69')
result = open('result', 'w+')
#sum = 0
#for i in f.split(','):
#    sum += i
#NA = sum / len(f.split(','))
#print(NA)

for line in f:
    tuple = line.split(',')
    temp_line = ''
    for i in range(len(tuple)):
        temp = 0
        if tuple[i] == 'NA':
            tuple[i] = str((int(tuple[i-1]) + int(tuple[i+1]))/2)
        if float(tuple[i])**(1/2) >= (50 + 69):
            temp_line += str(tuple[i]) + ', '
    if temp_line != '':
        result.write(temp_line[:-2])
        temp_line = ''



f.close()
result.close()
result = open('result', 'r')
for line in result:
    print(line)


