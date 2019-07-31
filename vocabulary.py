import random

verbs = {"tanomu": "to request",
         "ikamasu": "to go",
         "mitomemasu": "to confirm",
         "kaerimasu": "to leave",
         "itadakimasu": "to receive (a meal)",
         "kaimasu": "to buy",
         "nomimasu": "to drink",
         "tabemasu": "to eat",
         "mimasu": "to watch",
         "kimasu": "to come",
         "shimasu": "to do",
         "desu": "to be", }

verbs_arr = [v for i, v in enumerate(verbs)]
random_verbs = []
n = 10
while n > 0:
    random_verb = random.choice(verbs_arr)
    if random_verb not in random_verbs:
        random_verbs.append(random_verb)
        n -= 1

print("Define the following verbs:")
for verb in random_verbs:
    print(verb)
