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
    stdin_fileno = sys.stdin

    for line in stdin_fileno:
        line = line.strip()
        if line == "exit":
            exit(0)
        full_string = line + "#" + line[::-1]
        s_a = suffix_array(full_string)

        ordered_suffixes = [""] * len(full_string)
        for i in s_a:
            ordered_suffixes[s_a[i]] = full_string[i:]

        response_list = []
        max_lenght = -1

        for i in range(len(ordered_suffixes) - 1):
            if "#" in ordered_suffixes[i] and "#" in ordered_suffixes[i + 1]:
                continue
            if "#" not in ordered_suffixes[i] and "#" not in ordered_suffixes[i + 1]:
                continue

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

            if candidate_palindrome != candidate_palindrome[::-1]:
                continue

            if j > max_lenght:
                response_list = [candidate_palindrome]
                max_lenght = j
                continue
            elif j == max_lenght:
                if candidate_palindrome not in response_list:
                    response_list.append(candidate_palindrome)

        print(response_list, max_lenght)
