calls = 0


def count_call():
    global calls
    calls += 1


def string_info(string):
    count_call()
    info = (len(string), string.upper(), string.lower())
    return info


def is_contains(string, lis):
    count_call()
    list_q = [i.strip() for i in lis.split(',')]
    low_list_q = [i.lower() for i in list_q]
    if string.lower() in low_list_q:
        return True
    else:
        return False


while True:
    text = str(input("""Если хотите получить информацию по строке
Введите что-нибудь (или 'выход' для завершения): """))
    if text.lower() == 'выход':
        print('Завершение работы')
        break
    else:
        print(string_info(text))
        print(calls)
while True:
    text = str(input("""Напишите значение которое хотите найти в списке
(или 'выход' для завершения): """))
    if text.lower() == 'выход':
        print('Завершение работы')
        break
    else:
        list_queak = str(input("""Напишите ваш список
Пример: ASdkm, 13332, HellO
"""))
        print(is_contains(text, list_queak))
        print(calls)
