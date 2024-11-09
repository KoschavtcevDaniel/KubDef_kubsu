from typing import Optional


def gcdex(a: int, b: int):
    """
    Следующая рекурсивная функция реализует расширенный алгоритм Евклида.
    Она может быть использована для поиска обратного элемента.
    """
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = gcdex(b, a % b)
    return d, y, x - y * (a // b)


def obr(a: int, b: int) -> int:
    """
    Функция нахождения обратного элемента к a по модулю b.
    Находит а^(-1) mod b, то есть такое с, что ac=1(mod b).
    """
    g = gcdex(a, b)

    return g[1] % b if g[0] == 1 else 0


def BSGS(a: int, b: int, p: int) -> Optional[int]:
    m = int(p ** 0.5) + 1

    baby_steps = {pow(a, l, p): l for l in range(m)}

    c = obr(pow(a, m, p), p)
    current = b

    for k in range(m):
        if current in baby_steps:
            l = baby_steps[current]

            return m * k + l

        current = (current * c) % p

    return None


p = 263
a = 7
b = 233
print(f'{a}^x = {b} mod({p})')
result = BSGS(a, b, p)

print(f"x = {result}" if result else "Решение не найдено")

