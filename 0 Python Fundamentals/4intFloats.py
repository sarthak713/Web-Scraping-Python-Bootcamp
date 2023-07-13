# Ints 
    # whole complete numbers, with no fractional value
    # useful for counting

n=4
print(type(n))


# Floats
    # dividing an int by another gives float, floating point number
    # floats represent real numbers with fractional value

m=5.01
print(type(m))
print(4/2, 5/2)
print(type(2.), type(2.0))

# Ints & Floats
    # operations between ints & floats always produce floats
    # we can convert floats to ints, vice versa
    # floats take more space in memory than ints

print(type(1.0+1))
print(type(10*10.0))

print(type(3.0))
print(type(int(3.0)))
print(type(float(3)))

print(int(3.1))
print(int(3.999999)) # fractional part is ignored

# Floats are Approximations
    # computers store floats as binary (base 2) fractions
    # this may produce unexpected results with certain real numbers that dont have a precise binary representation

print(0.1+0.2)  # side effect