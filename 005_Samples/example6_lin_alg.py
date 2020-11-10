import numpy


a = numpy.array(
    [
        [1, 2],
        [5, 4]
    ],
    dtype=numpy.uint8
)

print('Min', a.min())
print('Min (0)', a.min(axis=0))
print('Min (1)', a.min(axis=1))

print(a.max())
print(a.max(axis=0))
print(a.max(axis=1))

