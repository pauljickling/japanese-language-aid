import random

vowel_seq = ["a", "i", "u", "e", "o"]
k_seq = ["ka", "ki", "ku", "ke"]
s_seq = ["sa", "shi", "su", "se", "so"]
t_seq = ["ta", "chi", "tsu", "te", "to"]
n_seq = ["na", "ni", "nu", "ne", "no"]
h_seq = ["ha", "hi", "hu", "he", "ho"]
m_seq = ["ma", "mi", "mu", "me", "mo"]
y_seq = ["ya", "yu", "yo"]
r_seq = ["ra", "ri", "ru", "re", "ro"]
w_seq = ["wa", "(w)o"]
n_seq = ["n"]

letters = vowel_seq + k_seq + s_seq + t_seq + n_seq + h_seq + m_seq + \
    y_seq + r_seq + w_seq + n_seq

n = 10

writing_systems = ["hiragana", "katakana"]

print("Write the letter for the following characters in {}:"
      .format(random.choice(writing_systems)))

while n > 0:
    print(random.choice(letters))
    n -= 1
