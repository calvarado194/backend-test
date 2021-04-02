from random import randint

# valores precalculados para la estimación, de acuerdo a la especificación de la secuencia
day_estimation = [
    0,
    1,
    1,
    2,
    3,
    5,
    8,
    13,
    21,
    34,
    55,
    89,
    144,
    233,
    377,
    610,
    987,
    1597,
    2584,
    4181,
]


def get_estimate(d: int) -> int:
    """
    Devuelve el estimado de días para la entrega, basado en la secuencia definida en el enunciado."""
    global day_estimation

    if d <= 0:
        raise ValueError("Distance must be a positive number")
    if d >= 2000:
        return day_estimation[-1]

    return day_estimation[int(d / 100)]


def estimate(d: int) -> str:
    return "A una distancia de {} kms, su paquete llegará en {} días".format(
        d, get_estimate(d)
    )


if __name__ == "__main__":
    for i in range(10):
        print(estimate(randint(1, 2000)))

