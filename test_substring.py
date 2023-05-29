from substring import *

text = "Don't let the noise of others' opinions drown out your own inner voice"
pattern1 = "opinions"
pattern2 = "phrase"

print("– Бойера-Мура")
boyer = boyer_moore(text, pattern1)
if boyer == -1:
    print("Подстрока не найдена")
else:
    print(f"Подстрока найдена в позиции {boyer}")
boyer = boyer_moore(text, pattern2)
if boyer == -1:
    print("Подстрока не найдена")
else:
    print(f"Подстрока найдена в позиции {boyer}")

print("\n– Рабина-Карпа")
rabin = rabin_karp(text, pattern1)
if rabin == -1:
    print("Подстрока не найдена")
else:
    print(f"Подстрока найдена в позиции {rabin}")
rabin = rabin_karp(text, pattern2)
if rabin == -1:
    print("Подстрока не найдена")
else:
    print(f"Подстрока найдена в позиции {rabin}")

print("\n- Кнута-Морриса-Пратта")
kmp = kmp_search(pattern1, text)
if kmp == -1:
    print("Подстрока не найдена")
else:
    print(f"Подстрока найдена в позиции {kmp}")
kmp = kmp_search(pattern2, text)
if kmp == -1:
    print("Подстрока не найдена")
else:
    print(f"Подстрока найдена в позиции {kmp}")

print("\n– с помощью конечного автомата")
auto = finite_automaton_matcher(text, pattern1)
if auto == -1:
    print("Подстрока не найдена")
else:
    print(f"Подстрока найдена в позиции {auto}")
auto = finite_automaton_matcher(text, pattern2)
if auto == -1:
    print("Подстрока не найдена")
else:
    print(f"Подстрока найдена в позиции {auto}")