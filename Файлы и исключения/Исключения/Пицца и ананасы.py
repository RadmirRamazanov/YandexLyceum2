class PizzaWithoutDoughError(ValueError):
    pass


class SauceLackError(PizzaWithoutDoughError):
    pass


class NotEnoughCheeseError(PizzaWithoutDoughError):
    pass


class AnanasError(PizzaWithoutDoughError):
    pass


class OutOfGroceriesError(ValueError):
    pass


def pizza(*args, **kwargs):
    z = ["dough"]
    cheeses = []
    if "dough" not in args:
        raise PizzaWithoutDoughError("You can't make pizza without dough.")
    if 'sauce' in kwargs and kwargs['sauce'] not in args:
        return SauceLackError("SauceLackError: Where's the sauce?")
    elif "sauce" in kwargs and kwargs["sauce"] in args:
        z.append(kwargs['sauce'])
    for i in args:
        if "cheese" in i:
            cheeses.append(i)
    if len(cheeses) < 2:
        raise NotEnoughCheeseError("You're not using enough cheese on that pizza.")
    z.append(cheeses[0])
    z.append(cheeses[-1])
    if "ananas" in args or "pineapple" in args:
        raise AnanasError("Pineapple on pizza!")
    meal = []
    if kwargs['vegan']:
        for i in args:
            if "meat" not in i and i not in z:
                meal.append(i)
    else:
        for i in args:
            if i not in z:
                meal.append(i)
    meal.sort(key=lambda i: (-len(i), i))
    if len(meal) == 0:
        raise OutOfGroceriesError("There's nothing to put in the pizza.")
    z.pop(-1)
    z = z + meal
    z.append(cheeses[-1])
    return z

