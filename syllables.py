import random

# basic sequences
vowel_seq = ["a", "i", "u", "e", "o"]
vowel_seq_hira = ["あ", "い", "う", "え", "お"]
vowel_seq_kata = ["ア", "イ", "ウ", "エ", "オ"]

k_seq = ["ka", "ki", "ku", "ke", "ko"]
k_seq_hira = ["か", "き", "く", "け", "こ"]
k_seq_kata = ["カ", "キ", "ク", "ケ", "コ"]

k_voiced_seq = ["ga", "gi", "gu", "ge", "go"]
k_voiced_seq_hira = ["が", "ぎ", "ぐ", "げ", "ご"]
k_voiced_seq_kata = ["ガ", "ギ", "グ", "ゲ", "ゴ"]

s_seq = ["sa", "shi", "su", "se", "so"]
s_seq_hira = ["さ", "し", "す", "せ", "そ"]
s_seq_kata = ["サ", "シ", "ス", "セ", "ソ"]

s_voiced_seq = ["za", "ji", "zu", "ze", "zo"]
s_voiced_seq_hira = ["ざ", "じ", "ず", "ぜ", "ぞ"]
s_voiced_seq_kata = ["ザ", "ジ", "ズ", "ゼ", "ゾ"]

t_seq = ["ta", "chi", "tsu", "te", "to"]
t_seq_hira = ["た", "ち", "つ", "て", "と"]
t_seq_kata = ["タ", "チ", "ツ", "テ", "ト"]

t_voiced_seq = ["da", "ji", "zu", "de", "do"]
t_voiced_seq_hira = ["だ", "ぢ", "づ", "で", "ど"]
t_voiced_seq_kata = ["ダ", "ジ", "ズ", "デ", "ド"]

n_seq = ["na", "ni", "nu", "ne", "no"]
n_seq_hira = ["な", "に", "ぬ", "ね", "の"]
n_seq_kata = ["ナ", "ニ", "ヌ", "ネ", "ノ"]

h_seq = ["ha", "hi", "hu", "he", "ho"]
h_seq_hira = ["は", "ひ", "ふ", "へ", "ほ"]
h_seq_kata = ["ハ", "ヒ", "フ", "ヘ", "ホ"]

h_voiced_seq = ["ba", "bi", "bu", "be", "bo"]
h_voiced_seq_hira = ["ば", "び", "ぶ", "べ", "ぼ"]
h_voiced_seq_kata = ["バ", "ビ", "ブ", "ベ", "ボ"]

h_aspirated_seq = ["pa", "pi", "pu", "pe", "po"]
h_aspirated_seq_hira = ["ぱ", "ぴ", "ぷ", "ぺ", "ぽ"]
h_aspirated_seq_kata = ["パ", "ピ", "プ", "ペ", "ポ"]

m_seq = ["ma", "mi", "mu", "me", "mo"]
m_seq_hira = ["ま", "み", "む", "め", "も"]
m_seq_kata = ["マ", "ミ", "ム", "メ", "モ"]

y_seq = ["ya", "yu", "yo"]
y_seq_hira = ["や", "ゆ", "よ"]
y_seq_kata = ["ヤ", "ユ", "ヨ"]

r_seq = ["ra", "ri", "ru", "re", "ro"]
r_seq_hira = ["ら", "り", "る", "れ", "ろ"]
r_seq_kata = ["ラ", "リ", "ル", "レ", "ロ"]

w_seq = ["wa", "wo"]
w_seq_hira = ["わ", "を"]
w_seq_kata = ["ワ", "ヲ"]

n_consonant = ["n"]
n_consonant_hira = ["ん"]
n_consonant_kata = ["ン"]

# combined syllables
k_combo = ["kya", "kyu", "kyo"]
k_combo_hira = ["きゃ", "きゅ", "きょ"]
k_combo_kata = ["キャ", "キュ", "キョ"]

k_voiced_combo = ["gya", "gyu", "gyo"]
k_voiced_combo_hira = ["ぎゃ", "ぎゅ", "ぎょ"]
k_voiced_combo_kata = ["ギャ", "ギュ", "ギョ"]

s_combo = ["sha", "shu", "sho"]
s_combo_hira = ["しゃ", "しゅ", "しょ"]
s_combo_kata = ["シャ", "シュ", "ショ"]

s_voiced_combo = ["ja", "ju", "jo"]
s_voiced_combo_hira = ["じゃ", "じゅ", "じょ"]
s_voiced_combo_kata = ["ジャ", "ジュ", "ジョ"]

c_combo = ["cha", "chu", "cho"]
c_combo_hira = ["ちゃ", "ちゅ", "ちょ"]
c_combo_kata = ["チャ", "チュ", "チョ"]

n_combo = ["nya", "nyu", "nyo"]
n_combo_hira = ["にゃ", "にゅ", "にょ"]
n_combo_kata = ["ニャ", "ニュ", "ニョ"]

h_combo = ["hya", "hyu", "hyo"]
h_combo_hira = ["ひゃ", "ヒュ", "ひょ"]
h_combo_kata = ["ヒャ", "ヒュ", "ヒョ"]

h_voiced_combo = ["bya", "byu", "byo"]
h_voiced_combo_hira = ["びゃ", "びゅ", "びょ"]
h_voiced_combo_kata = ["ビャ", "ビュ", "ビョ"]

h_aspirated_combo = ["pya", "pyu", "pyo"]
h_aspirated_combo_hira = ["ピャ", "ピュ", "ぴょ"]
h_aspirated_combo_kata = ["ピャ", "ピュ", "ピョ"]

m_combo = ["mya", "myu", "myo"]
m_combo_hira = ["みゃ", "みゅ", "みょ"]
m_combo_kata = ["ミャ", "ミュ", "ミョ"]

r_combo = ["rya", "ryu", "ryo"]
r_combo_hira = ["りゃ", "りゅ", "りょ"]
r_combo_kata = ["リャ", "リュ", "リョ"]

# Lists of Lists
letters = vowel_seq + k_seq + k_voiced_seq + s_seq + s_voiced_seq + t_seq + \
    t_voiced_seq + n_seq + h_seq + h_voiced_seq + h_aspirated_seq + m_seq + \
    y_seq + r_seq + w_seq + n_consonant + k_combo + k_voiced_combo + \
    s_combo + s_voiced_combo + c_combo + n_combo + h_combo + \
    h_voiced_combo + h_aspirated_combo + m_combo + r_combo

hiragana = vowel_seq_hira + k_seq_hira + k_voiced_seq_hira + s_seq_hira + \
    s_voiced_seq_hira + t_seq_hira + t_voiced_seq_hira + n_seq_hira + \
    h_seq_hira + h_voiced_seq_hira + h_aspirated_seq_hira + m_seq_hira + \
    y_seq_hira + r_seq_hira + w_seq_hira + n_consonant_hira + k_combo_hira + \
    k_voiced_combo_hira + s_combo_hira + s_voiced_combo_hira + \
    c_combo_hira + n_combo_hira + h_combo_hira + h_voiced_combo_hira + \
    h_aspirated_combo_hira + m_combo_hira + r_combo_hira

katakana = vowel_seq_kata + k_seq_kata + k_voiced_seq_kata + s_seq_kata + \
    s_voiced_seq_kata + t_seq_kata + t_voiced_seq_kata + n_seq_kata + \
    h_seq_kata + h_voiced_seq_kata + h_aspirated_seq_kata + m_seq_kata + \
    y_seq_kata + r_seq_kata + w_seq_kata + n_consonant_kata + k_combo_kata + \
    k_voiced_combo_kata + s_combo_kata + s_voiced_combo_kata + \
    c_combo_kata + n_combo_kata + h_combo_kata + h_voiced_combo_kata + \
    h_aspirated_combo_kata + m_combo_kata + r_combo_kata


# Randomly selected for the english to japanese function
writing_systems = ["hiragana", "katakana"]


def english_to_japanese(n):
    """
    Asks users to write the Japanese characters for different syllables.
    Since inputting into a keyboard wouldn't really teach anything, the idea
    here is just to write on some paper, and so this exercise is based on the
    honor system.
    """
    print("Write the letter for the following characters in {}:"
          .format(random.choice(writing_systems)))
    while n > 0:
        print(random.choice(letters))
        n -= 1


def hiragana_to_english(n, feedback=False):
    """
    n is the number of questions, and feedback is a boolean that if true
    gives feedback for wrong answers.
    """
    score = 0
    incorrect_answers = []
    print("Identify the following hiragana:")
    while n > 0:
        question = random.choice(hiragana)
        hira_index = hiragana.index(question)
        answer = input("{}\n".format(question))
        answer = answer.lower()
        if answer == letters[hira_index]:
            print("Correct!")
            score += 1
        else:
            incorrect_answers.append(question)
            if feedback is True:
                print("Incorrect. Correct answer was {}.".format(
                        letters[hira_index]))
        n -= 1
    print("You answered {} correctly!".format(score))
    print("Your answers were incorrect for the following hiragana:")
    print(incorrect_answers)


def katakana_to_english(n, feedback=False):
    """
    Same thing, but with katakana
    """
    score = 0
    incorrect_answers = []
    print("Identify the following katakana:")
    while n > 0:
        question = random.choice(katakana)
        kata_index = katakana.index(question)
        answer = input("{}\n".format(question))
        answer = answer.lower()
        if answer == letters[kata_index]:
            print("Correct!")
            score += 1
        else:
            incorrect_answers.append(question)
            if feedback is True:
                print("Incorrect. Correct answer was {}.".format(
                        lettersw[kata_index]))
        n -= 1
    print("You answered {} correctly!".format(score))
    print("Your answers were incorrect for the following katakana:")
    print(incorrect_answers)


hiragana_to_english(10, True)
