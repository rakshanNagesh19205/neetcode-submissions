def discount_applies(age: int) -> bool:
    result = False
    if age < 18 or age >= 65:
        result = True
    return result




# don't modify this code below this line
print(discount_applies(17))
print(discount_applies(18))
print(discount_applies(40))
print(discount_applies(65))
print(discount_applies(70))
