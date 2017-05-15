f = open('file.txt', 'wt', encoding='cp1251')
print(f)
f.write('first string\n')
f.write('second string\n')
f.write('third string\n')
f.flush()
f.write('Четвертая строка\n')
f.flush()
f.close()

f = open('file.txt', 'rt')
s = f.read()
print(s)
f.close()

f = open('file.txt', 'rt')
print(f.read(5))
print(f.read(5))
print(f.read(5))
f.close()

f = open('file.txt', 'rt')
print(f.readline())
print(f.readline())
print(f.readline())
f.close()

f = open('file.txt', 'rt')
for line in f:
    print(line)
f.close()

f = open('file.txt', 'rt')
print(f.tell())
print(f.readline())
print(f.tell())
f.close()

f = open('file.txt', 'at')
print(f.tell())
f.close()

f = open('file.txt', 'r+t')
print(f.tell())
f.seek(5)
print(f.tell())
f.close()

with open('file.txt', 'rt') as f:
    for line in f:
        print(line)
print(f.closed)

# =======================================================

obj = [1, 2, 'aaa', [2, 3, 4]]
import pickle
s = pickle.dumps(obj)
print(s)
obj1 = pickle.loads(s)
print(obj1)
print(obj == obj1)

f = open('filebinary.txt', 'wb')
pickle.dump(obj, f)
f.close()
f = open('filebinary.txt', 'rb')
obj2 = pickle.load(f)
print(obj2)
