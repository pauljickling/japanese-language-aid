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
         "okuru": "to send",
         "desu": "to be", }

nouns = {"watashi": "I",
         "musume": "girl/daughter",
         "yuki": "snow",
         "kaji": "fire",
         "sensei": "teacher",
         "senpai": "upper classmate",
         "ashita": "tomorrow",
         "chokoreto": "chocolate",
         "gakko": "school",
         "haru": "spring",
         "gohan": "meal/rice",
         "neko": "cat",
         "inu": "dog", }

adjectives = {"osoi": "late",
              "samui": "cold",
              "atsui": "hot",
              "muzukashii": "difficult",
              "okii": "big",
              "chiisai": "small",
              "oishii": "delicious",
              "mazui": "unsavory",
              "toi": "far",
              "chikai": "near",
              "omoshiroi": "interesting",
              "tsumaranai": "boring",
              "ayashii": "suspicious",
              "nagai": "long",
              "mijikai": "short",
              "yasui": "cheap",
              "takai": "expensive",
              "kirei": "beautiful", }

particles = {"ne": "right?",
             "na": "right? (masculine)",
             "yo": "take note", }

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
