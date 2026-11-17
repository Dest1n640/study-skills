Реализовал только `parse_numbers` в [exercise.py](/private/var/folders/8k/h7q4305x2_99njry5v0zh00h0000gn/T/study-skills-install-4aag7ita/probe-study-guide-normal/exercise.py:1):

```python
return [int(part) for part in text.split(",")]
```

`split(",")` сохраняет пустые элементы, а `int` допускает пробелы вокруг числа и вызывает `ValueError` для пустой строки или нецелого значения. Дополнительная проверка не нужна.

Запустил `python3 -m unittest -v test_exercise.ParseTests` — все 3 теста прошли.

`summarize` оставлен без изменений; его тесты не запускал.