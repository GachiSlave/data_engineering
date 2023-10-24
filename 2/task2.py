f = open('text_2_var_69')
sum = []
j = 0
for line in f:
    temp = 0
    for i in line.split():
        temp+=int(i)
    sum.append(temp)
    sum.append(temp / len(line.split()))
    j+=1
f.close()

print("  Сумма","            ","СреднееАрифмитическое")
for i in range(0, len(sum), 2):
    print('{: d}'.format(sum[i]), '{: 20.1f}'.format(sum[i+1]))
