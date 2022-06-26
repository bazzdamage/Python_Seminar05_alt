# Напишите программу, удаляющую из текста все слова содержащие "абв",
# которое регистронезависимо. Используйте знания с последней лекции.
# Выполните ее в виде функции.

example = 'абвгдеж рабав копыто фабв Абкн абрыволк аБволк'
entry_str = 'абв'


def remove_strings_with_match(text: str, entry_str: str):
    result = list(filter(lambda x: entry_str not in x.lower(), text.split()))
    return result


print(remove_strings_with_match(example, entry_str))
