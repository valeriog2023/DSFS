import enum
import random

class kid(enum.Enum):
    BOY= 0 
    GIRL = 1

def random_kid() -> kid:
    return random.choice([kid.BOY,kid.GIRL])

both_girls = 0
older_girl = 0
either_girl = 0
younger_girl = 0

random.seed(0)

for _ in range(10000):
    younger = random_kid()
    older = random_kid()
    if younger == kid.GIRL:
        younger_girl += 1
    if older == kid.GIRL:
        older_girl += 1
    if older == kid.GIRL and younger == kid.GIRL:
        both_girls += 1
    if older == kid.GIRL or younger == kid.GIRL:
        either_girl += 1

print("P(older): ", older_girl / 10000)   
print("P(younger): ", younger_girl / 10000)   
print("P(both): ", both_girls / 10000)
print("P(either): ", either_girl / 10000)
# p(A and B) == P(A|B) * P(B)
# P(A|B) = P(A and B) / P(B)
# Case 1
# A: both girls
# B: older is girl

print("P(both | older): ", both_girls / older_girl)                
# Case 2
# A: both girls
# B: either is girl
print("P(both | either): ", both_girls / either_girl)                
# Bayes conditional probability theorem
# 1) P(E|F) == P(E,F) / P(F) ==  P(F|E) * P(E) / P(F)
# 2) P(F) = P(F|E) + P(F|not E)
# => P(E|F) =  P(F|E) * P(E) / [ P(F|E) + P(F|not E) ]
#