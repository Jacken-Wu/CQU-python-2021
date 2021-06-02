name = input()
a = float(input())
v = float(input())
length = v * v / (2*a)
print('The acceleration of %s is %.2f M / s, the take-off speed is %.2f M / s, and the shortest '
      'take-off runway length is %.2f M.' % (name, a, v, length))

