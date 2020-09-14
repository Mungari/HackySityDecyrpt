def chunk(seq, size):
    return [seq[pos:pos + size] for pos in range(0, len(seq), size)]

ascii_sum = []
text=""
f=open("cypher.txt", "r")
cont=f.read().split('.')
for x in chunk(cont, 3):
    ascii_sum.append(sum([int(x[i]) for i in range(3)]))
for a in ascii_sum:
    #print(a, ascii_sum.count(a))
    text = text+(chr(a-762))

print(text)