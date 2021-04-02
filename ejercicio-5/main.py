import math

if __name__ == "__main__":
    fibonacci = []
    fibonacci.append(1)
    fibonacci.append(1)

    index = 0

    def next_fibonacci() -> int:
        """
        Retorna el siguiente número de fibonacci empezando desde 1.
        Utilizamos programación dinámica para acelerar el proceso."""
        global index
        if index < len(fibonacci):
            # si ya sabemos el resultado, avanzar index y retornar
            fib = fibonacci[index]
            index = index + 1
            return fib

        # si es un index nuevo, calcular usando los anteriores
        next_fib = fibonacci[index - 1] + fibonacci[index - 2]

        fibonacci.append(next_fib)
        index = index + 1

        return next_fib

    def get_divisors(n) -> int:
        """
        Retorna la cantidad de divisores de un número.
        Usamos un algoritmo simple, para minimizar la carga en memoria.
        """
        p = 1
        count = 0

        # llegamos hasta sqrt(n) porque si p > sqrt(n) y p divide a n, entonces n/p < sqrt(n) será encontrado primero.
        while p <= math.sqrt(n):
            if n % p == 0:
                if n / p != p:
                    count = count + 2
                else:
                    # si n es un cuadrado perfecto
                    count = count + 1
            p = p + 1

        return count

    p = 0
    while True:
        p = next_fibonacci()
        count = get_divisors(p)

        print(p, count)

        if count >= 1000:
            break
