sidesnumber = int(input("Number of sides on die: "))
hpleft = int(input("Enemy health left: "))
prob = 0

def probability(sides, hp):
    if hp <= sides:
        return (sides + 1 - hp) /sides
    else:
        return probability(sides,hp - sides) / sides

print(probability(sidesnumber, hpleft))
