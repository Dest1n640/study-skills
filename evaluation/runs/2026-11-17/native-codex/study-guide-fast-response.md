Реализовал `parse_numbers` в [exercise.py](/var/folders/8k/h7q4305x2_99njry5v0zh00h0000gn/T/study-skills-install-4aag7ita/probe-study-guide-fast/exercise.py:1).

Строка разбивается по запятым, а `int` преобразует каждый элемент: он допускает пробелы вокруг числа и вызывает `ValueError` для пустого или нецелого значения. Это позволяет обойтись без отдельной проверки каждого случая.

Все три теста `ParseTests` прошли. `summarize` не изменял и его тесты не запускал.