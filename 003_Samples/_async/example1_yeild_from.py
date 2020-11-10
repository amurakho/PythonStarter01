def count(n):
    res = []
    while n != 0:
        res.append(n)
        n -= 1
    return res


def test_yield(n):
    while n != 0:
        yield n - 1
        n -=1



def concat_sequence_v1(s1, s2):
    for elem in s1:
        yield elem
    for elem in s2:
        yield elem

def concat_sequence_v2(s1, s2):
    yield from s1
    yield from s2


seq1 = range(10)
seq2 = range(10, 20)
result = concat_sequence_v1(seq1, seq2)

print('Seq 1')
for i in result:
    print(i)

seq1 = range(10)
seq2 = range(10, 20)
result = concat_sequence_v2(seq1, seq2)

print('Seq 2')
for i in result:
    print(i)
