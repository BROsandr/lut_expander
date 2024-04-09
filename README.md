# lut_expander

В некоторой степени автоматизирует создание lut (look-up table).

Примеры использования можно найти в [`tests`](./project/tests/).

Основным классом является [`Lut`](./project/lut.py#45). Основные аргументы его конструктора:
-   `lut_row_func` &mdash; функцию, которая создает значение для ячейки lut. Например, функция `lut_row_func_and` позволяет сформировать таблицу для булевой функции конкатенации двух аргументов:

    ```python
    def lut_row_func_and(a: bool, b: bool)->bool:
      return a & b
    ```

    Значение аргументов получаются из номера строки (ячейки) в `Lut`. Размер `Lut` будет автоматически вычислен на основе количества аргументов `lut_row_func` (в примере `Lut` будет на 4 строки).

-   `Lut_row_format_factory` &mdash; генерирует форматы `Lut_row_format`. Форматы определяют, как будет выглядеть строка `Lut` при преобразовании ее в `str`. Например, можно преобразовывать номер строки в литерал верилога, добавлять символ `:`, преобразовывать результат `lut_row_func` в `str` и добавлять `;`. Такой формат упрощает создание элементов `switch`/`case`.

`Lut` является итератором, который создает `Lut_row`. Над `Lut_row` можно производить различные операции. Например, можно перемешивать их стандартными средствами *python*.

Возможный строковой вид создаваемой лут при использовании `lut_row_func_and` из примера с `Lut`:

```
2'b00: False;
2'b01: False;
2'b10: False;
2'b11: True;
```
