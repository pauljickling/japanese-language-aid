import random


class Word:

    def __init__(self, romanji, english, jp, hiragana=None, katakana=None):
        self.romanji = romanji
        self.english = english
        self.jp = jp
        self.hiragana = hiragana
        self.katakana = katakana

    def __repr__(self):
        return "{} {} {}".format(self.jp, self.romanji, self.english)


verbs = [Word("tanomu", "to request", "頼む"),
         Word("taberu", "to eat", "食べる"),
         Word("ikamasu", "to go", "イカます"),
         Word("mitomemasu", "to confirm", "認めます"),
         Word("kaerimasu", "to leave", "帰ります"),
         Word("nomimasu", "to drink", "のみうます"),
         Word("tabemasu", "to eat", "食べます"),
         Word("mimasu", "to watch", "見ます"),
         Word("kimasu", "to come", "きます"),
         Word("shimasu", "to do", "します"),
         Word("okuru", "to send", "送る"),
         Word("desu", "to be", "です"), ]

nouns = {"watashi": "I",
         "musume": "girl/daughter",
         "家族": "family",
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
