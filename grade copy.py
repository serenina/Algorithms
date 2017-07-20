for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    stu_sco = [[n,s] for n in (name) for s in (score)]
print stu_sco

n = raw_input()
for i in range(int(n)):
    name =

for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    stu_sco.append([name, score])
print stu_sco

def second_smallest():
    m1, m2 = float('inf'), float('inf')
    for i in range (int(n)):
        for x in row in stu_sco:
            if x <= m1:
                m1, m2 = x, m1
            elif x < m2:
                m2 = x
        return m2


print stu_sco