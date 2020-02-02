a = [1, 33, 42, 3, 6, 86, 256, 0, -50, 77, 30]
b = []
def mymax(elements):
    if len(elements) == 0:
        return None
    else:
        m = elements[0]
        for element in elements[1:]:
            if element > m:
                m = element
        return(m)
print(mymax(a))
print(mymax(b))