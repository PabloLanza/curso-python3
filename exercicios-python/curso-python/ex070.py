val = []
for c in range(0, 5):
    num = int(input('Digite um número: '))
    if c == 0 or num > val[-1]:
        val.append(num)
    else:
        pos = 0
        while pos < len(val):
            if num <= val[pos]:
                val.insert(pos, num)
                break
            pos += 1
print(f'Os valores digitados em ordem foram {val}')
        

