from itertools import zip_longest, islice
import sys


def to_int_keys(l):
    seen = set()
    ls = []
    for e in l:
        if not e in seen:
            ls.append(e)
            seen.add(e)
    ls.sort()
    index = {v: i for i, v in enumerate(ls)}
    return [index[v] for v in l]


def suffix_array(s):
    """dado un string s, genera el suffix array para el string.
    Un suffix array es un arreglo (en este caso, una lista) que contiene los índices para iniciar cada sufijo del string s,
    indicados de acuerdo a su orden alfabético.
    """
    n = len(s)
    k = 1
    line = to_int_keys(s)
    while max(line) < n - 1:
        line = to_int_keys(
            [
                a * (n + 1) + b + 1
                for (a, b) in zip_longest(line, islice(line, k, None), fillvalue=-1)
            ]
        )
        k <<= 1
    return line


if __name__ == "__main__":
    # tomamos input desde stdin
    stdin_fileno = sys.stdin

    for line in stdin_fileno:
        # removemos caracteres innecesarios
        line = line.strip()

        # terminamos el script si la línea es exit
        if line == "exit":
            exit(0)

        # el palindromo más largo será un sufijo que exista tanto en el string original como en el string leído al reves.
        # usaremos este conocimiento para obtener los palindromos via el suffix array de original#reverso
        full_string = line + "#" + line[::-1]
        s_a = suffix_array(full_string)

        # una vez obtenido el suffix array, creamos el array con los sufijos, ordenados alfabéticamente
        ordered_suffixes = [""] * len(full_string)
        for i in s_a:
            ordered_suffixes[s_a[i]] = full_string[i:]

        # almacenamos el largo máximo registrado, y todos los palíndromos que lo cumplen
        response_list = []
        max_lenght = -1

        for i in range(len(ordered_suffixes) - 1):
            # si ambos strings a comprarar tienen el caracter separador, o ambos no lo tienen,
            # ambos pertenecen al "mismo lado" del string, y por lo tanto no nos sirven.
            if "#" in ordered_suffixes[i] and "#" in ordered_suffixes[i + 1]:
                continue
            if "#" not in ordered_suffixes[i] and "#" not in ordered_suffixes[i + 1]:
                continue

            # obtenemos nuestro palindromo candidato
            j = 0
            candidate_palindrome = ""
            while True:
                if j >= len(ordered_suffixes[i]) or j >= len(ordered_suffixes[i + 1]):
                    break
                if ordered_suffixes[i][j] == ordered_suffixes[i + 1][j]:
                    candidate_palindrome = candidate_palindrome + ordered_suffixes[i][j]
                    j = j + 1
                else:
                    break

            # revisamos que nuestro candidato efectivamente sea un palíndromo
            # si no lo es, lo ignoramos
            if candidate_palindrome != candidate_palindrome[::-1]:
                continue

            # si el candidato es un palíndromo, revisamos que sea del mismo largo (o más) que nuestro mejor largo actual.
            # si es más largo, reiniciamos la lista de palindreomos y definimos el nuevo largo objetivo.
            # Si es igual de largo, se agrega a la lista de respuestas
            # En cualquier otro caso, se descarta.
            if j > max_lenght:
                response_list = [candidate_palindrome]
                max_lenght = j
                continue
            elif j == max_lenght:
                if candidate_palindrome not in response_list:
                    response_list.append(candidate_palindrome)

        print(response_list, max_lenght)
