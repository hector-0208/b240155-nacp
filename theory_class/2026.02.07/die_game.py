"""
You roll two six-sided dice, each with faces containing one, two,
three, four, five and six spots, respectively. When the dice come to
rest, the sum of the spots on the two upward faces is calculated. If
the sum is 7 or 11 on the first roll, you win. If the sum is 2, 3 or 12
on the first roll (called “craps”), you lose (i.e., the “house” wins). If
the sum is 4, 5, 6, 8, 9 or 10 on the first roll, that sum becomes
your “point.” To win, you must continue rolling the dice until you
“make your point” (i.e., roll that same point value). You lose by
rolling a 7 before making your point.
"""
import random
def roll():
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    total = die1 + die2
    print(f"Player rolled {die1} + {die2} = {total}")
    return total

print("GAME START!")
sum_of_die = roll()

if sum_of_die == 7 or sum_of_die == 11:
    print("Player Won")
elif sum_of_die == 2 or sum_of_die == 3 or sum_of_die == 12:
    print("Player Lost")
else:
    point = sum_of_die
    print(f"Point = {point}")
    end = False
    while (not end):
        new_sum = roll()
        if new_sum == point:
            print("Player Won")
            end = True
        elif new_sum == 7:
            print("Player Lost")
            end = True
