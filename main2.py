import random
A = input('Введите текст для кодировки: ')

B = ['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ь','ы','ъ','э','ю','я',' ',',']

C = [x for x in range(len(A)*10)]
print(C)
for x in C:
    H = random.randint(0,32)                     ## данный цикл дает каждому значению списка С случайную букву, из указанного списка.
    C[x] = B[H]
print(C)
V = set()

for x in [x for x in range(len(A))]:         ## данный цикл создает множество с требуемым кол-вом значений(равному длине кодируемого объекта
    R = random.randint(1,len(A)*5)
    V.add(R)

U = len(A) - len(V)

while not len(V) == len(A):
    R = random.randint(1, len(A) * 5)       ## данный цикл смотрит, равно ли кол-во значений множества и символов в кодируемой строке,
    V.add(R)                                 ## если во множестве были повторения, он добавляет требуемое кол-во символов, но только один раз
                                           ## вероятно, с большим кол-вом символов, потребуется еще несколько подобных итераций(костылей).
print(V)
print(len(V))
print(len(A))
V = list(V)

for x in [x for x in range(len(A))]:
    C[V[x]] = A[x]

D = ''.join(C)
print(D)
kodi = open('egor.txt','w')
kodi.write(D)
kodi.close()
kodi = open('egor.txt')
D = kodi.readline()
K = list(D)

G = []
for x in [x for x in range(len(A))]:
    G.append(K[V[x]])

G = ''.join(G)
print(G)














