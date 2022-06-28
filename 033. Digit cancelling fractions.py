from fractions import Fraction
result = []
for i in range(10, 100):
    for j in range(10, i):
        if j < i:
            f1 = j / i
            if str(i)[1] != "0" and str(j)[1] == str(i)[0]:
                f2 = int(str(j)[0]) / int(str(i)[1])
                if f1 == f2:
                    result.append((j, i))

(numerator, denominator) = (1, 1)
for tuple_pair in result:
    numerator *= tuple_pair[0]
    denominator *= tuple_pair[1]

print(Fraction(numerator, denominator))
