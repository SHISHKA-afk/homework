import random
left_hole = int(random.randint(3, 20))
half = int(left_hole / 2)
code_list = []
w = 1
for i in range(1, left_hole):
    while w < left_hole:
        if left_hole % (i + w) == 0 and w != i:
            if w < left_hole:
                code_list.extend([i, w])
                w += 1
            else:
                w += 1
                continue
        else:
            w += 1
    w = i+1
result = ''.join(str(num) for num in code_list)
print(result)
print(left_hole)



