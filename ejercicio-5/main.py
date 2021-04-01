import math

if __name__ == "__main__":
    fibonacci = []
    fibonacci.append(1)
    fibonacci.append(1)

    index = 0

    def next_fibonacci():
        """
        Returns next number in the fibonacci sequence, starting from index. """
        global index
        if index < len(fibonacci):
            fib = fibonacci[index]
            index = index + 1
            return fib

        next_fib = fibonacci[index - 1] + fibonacci[index - 2]
        fibonacci.append(next_fib)

        index = index + 1

        return next_fib

    def get_divisors(n):
        p = 1
        count = 0

        while p <= math.sqrt(n):
            if n % p == 0:
                if n / p != p:
                    count = count + 2
                else:
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
