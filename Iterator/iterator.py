


sehirler = [ "Mardin", "Ankara", "İstanbul", "Burdur"]


iteratorum = iter(sehirler)

print(next(iteratorum))
print(next(iteratorum))
print(next(iteratorum))
print(next(iteratorum))

# yukarıda tanımlanan iterator aşağıda yazılan for ile bire bir aynıdır.
# kendi iteratorlarımızı yazabilmemiz için verilmiş bir örnek

for i in sehirler:
    print(i)

