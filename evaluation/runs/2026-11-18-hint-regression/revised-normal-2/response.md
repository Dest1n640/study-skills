Причина в [exercise.py:2](/private/var/folders/8k/h7q4305x2_99njry5v0zh00h0000gn/T/study-hint-regression-da7cq42u/probe-study-hint-normal/exercise.py:2): условие `value >= 0` включает ноль, поэтому считает неотрицательные числа.

Запустил `python3 -B -m unittest -v`: для `[-2, 0, 3]` получено `2` вместо `1`; остальные два теста проходят. Следующий шаг — выбрать сравнение, исключающее равенство нулю.

Файлы не менял: выбранный [study-hint-normal](/private/var/folders/8k/h7q4305x2_99njry5v0zh00h0000gn/T/study-hint-regression-da7cq42u/.agents/skills/study-hint-normal/SKILL.md) требует “Do not write or edit those files”, оставляя правку ученику. Ошибка пока сохраняется.