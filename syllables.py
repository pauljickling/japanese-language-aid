import random

# basic sequences
vowel_seq = ["a", "i", "u", "e", "o"]
k_seq = ["ka", "ki", "ku", "ke"]
k_voiced_seq = ["ga", "gi", "gu", "ge", "go"]
s_seq = ["sa", "shi", "su", "se", "so"]
s_voiced_seq = ["za", "ji", "zu", "ze", "zo"]
t_seq = ["ta", "chi", "tsu", "te", "to"]
t_voiced_seq = ["da", "ji", "zu", "de", "do"]
n_seq = ["na", "ni", "nu", "ne", "no"]
h_seq = ["ha", "hi", "hu", "he", "ho"]
h_voiced_seq = ["ba", "bi", "bu", "be", "bo"]
h_aspirated_seq = ["pa", "pi", "pu", "pe", "po"]
m_seq = ["ma", "mi", "mu", "me", "mo"]
y_seq = ["ya", "yu", "yo"]
r_seq = ["ra", "ri", "ru", "re", "ro"]
w_seq = ["wa", "(w)o"]
n_seq = ["n"]

# combined syllables
k_combo = ["kya", "kyu", "kyo"]
k_voiced_combo = ["gya", "gyu", "gyo"]
s_combo = ["sha", "shu", "sho"]
s_voiced_combo = ["(s)ja", "(s)ju", "(s)jo"]
c_combo = ["cha", "chu", "cho"]
c_voiced_combo = ["(c)ja", "(c)ju", "(c)jo"]
n_combo = ["nya", "nyu", "nyo"]
h_combo = ["hya", "hyu", "hyo"]
h_voiced_combo = ["bya", "byu", "byo"]
h_aspirated_combo = ["pya", "pyu", "pyo"]
m_combo = ["mya", "myu", "myo"]
r_combo = ["rya", "ryu", "ryo"]

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
