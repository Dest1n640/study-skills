**Ошибка в подсчёте.** `count_positive` включает ноль, потому что условие `value >= 0` допускает равенство. Для входа `[0]` ожидается `0`, а при запуске функция вернула `1`. [exercise.py, строка 2](/private/var/folders/8k/h7q4305x2_99njry5v0zh00h0000gn/T/study-review-eval.SIi8ydSC/workspaces/review-worktree/exercise.py:2)

**Подсказка.** Проверь, при каком сравнении с нулём значения `-1`, `0` и `1` дадут `False`, `False` и `True` соответственно.

Проверил текущее изменение и запустил `python3 -m unittest -v`. Два теста прошли, а `test_excludes_zero` на входе `[-2, 0, 3]` получил `2` вместо `1`. [test_exercise.py, строка 7](/private/var/folders/8k/h7q4305x2_99njry5v0zh00h0000gn/T/study-review-eval.SIi8ydSC/workspaces/review-worktree/test_exercise.py:7)