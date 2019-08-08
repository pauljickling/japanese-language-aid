import random

# basic sequences
vowel_seq = ["a", "i", "u", "e", "o"]
vowel_seq_hira = ["あ", "い", "う", "え", "お"]
k_seq = ["ka", "ki", "ku", "ke", "ko"]
k_seq_hira = ["か", "き", "く", "け", "こ"]
k_voiced_seq = ["ga", "gi", "gu", "ge", "go"]
k_voiced_seq_hira = ["が", "ぎ", "ぐ", "げ", "ご"]
s_seq = ["sa", "shi", "su", "se", "so"]
s_seq_hira = ["さ", "し", "す", "せ", "そ"]
s_voiced_seq = ["za", "ji", "zu", "ze", "zo"]
s_voiced_seq_hira = ["ざ", "じ", "ず", "ぜ", "ぞ"]
t_seq = ["ta", "chi", "tsu", "te", "to"]
t_seq_hira = ["た", "ち", "つ", "て", "と"]
t_voiced_seq = ["da", "ji", "zu", "de", "do"]
t_voiced_seq_hira = ["だ", "ぢ", "づ", "で", "ど"]
n_seq = ["na", "ni", "nu", "ne", "no"]
n_seq_hira = ["な", "に", "ぬ", "ね", "の"]
h_seq = ["ha", "hi", "hu", "he", "ho"]
h_seq_hira = ["は", "ひ", "ふ", "へ", "ほ"]
h_voiced_seq = ["ba", "bi", "bu", "be", "bo"]
h_voiced_seq_hira = ["ば", "び", "ぶ", "べ", "ぼ"]
h_aspirated_seq = ["pa", "pi", "pu", "pe", "po"]
h_aspirated_seq_hira = ["ぱ", "ぴ", "ぷ", "ぺ", "ぽ"]
m_seq = ["ma", "mi", "mu", "me", "mo"]
m_seq_hira = ["ま", "み", "む", "め", "も"]
y_seq = ["ya", "yu", "yo"]
y_seq_hira = ["や", "ゆ", "よ"]
r_seq = ["ra", "ri", "ru", "re", "ro"]
r_seq_hira = ["ら", "り", "る", "れ", "ろ"]
w_seq = ["wa", "(w)o"]
w_seq_hira = ["わ", "を"]
n_seq = ["n"]
n_seq_hira = ["ん"]

# combined syllables
k_combo = ["kya", "kyu", "kyo"]
k_combo_hira = ["きゃ", "きゅ", "きょ"]
k_voiced_combo = ["gya", "gyu", "gyo"]
k_voiced_combo_hira = ["ぎゃ", "ぎゅ", "ぎょ"]
s_combo = ["sha", "shu", "sho"]
s_combo_hira = ["しゃ", "しゅ", "しょ"]
s_voiced_combo = ["ja", "ju", "jo"]
s_voiced_combo_hira = ["じゃ", "じゅ", "じょ"]
c_combo = ["cha", "chu", "cho"]
c_combo_hira = ["ちゃ", "ちゅ", "ちょ"]
n_combo = ["nya", "nyu", "nyo"]
n_combo_hira = ["にゃ", "にゅ", "にょ"]
h_combo = ["hya", "hyu", "hyo"]
H_combo_hira = ["ひゃ", "ヒュ", "ひょ"]
h_voiced_combo = ["bya", "byu", "byo"]
h_voiced_combo_hira = ["びゃ", "びゅ", "びょ"]
h_aspirated_combo = ["pya", "pyu", "pyo"]
h_aspirated_combo_hira = ["ピャ", "ピュ", "ぴょ"]
m_combo = ["mya", "myu", "myo"]
m_combo_hira = ["みゃ", "みゅ", "みょ"]
r_combo = ["rya", "ryu", "ryo"]
r_combo_hira = ["りゃ", "りゅ", "りょ"]

letters = vowel_seq + k_seq + k_voiced_seq + s_seq + s_voiced_seq + t_seq + \
    t_voiced_seq + n_seq + h_seq + h_voiced_seq + h_aspirated_seq + m_seq + \
    y_seq + r_seq + w_seq + n_seq + k_combo + k_voiced_combo + s_combo + \
    s_voiced_combo + c_combo + c_voiced_combo + n_combo + h_combo + \
    h_voiced_combo + h_aspirated_combo + m_combo + r_combo

n = 10

writing_systems = ["hiragana", "katakana"]

print("Write the letter for the following characters in {}:"
      .format(random.choice(writing_systems)))

while n > 0:
    print(random.choice(letters))
    n -= 1
