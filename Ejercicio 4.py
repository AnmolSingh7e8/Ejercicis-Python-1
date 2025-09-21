elements = int(input("Introdueix els numero d'elements qeu vols consultar: "))

#La formula es F(n) = F(n-1) + F(n-2)
def fibonacci(elements):
    if elements < 2:
        return elements
    else:
        return fibonacci(elements - 1) + fibonacci(elements - 2)

print("Els elements de la sèrie Fibonacci són:")
for i in range(elements):
    print(fibonacci(i))