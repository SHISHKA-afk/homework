import re


def send_email(message, recipient, *, sender="university.help@gmail.com"):
    def is_valid_email(email):
        return bool(re.match(r"^[\w.-]+@[\w.-]+\.(com|ru|net)$", email))

    if not is_valid_email(sender) or not is_valid_email(recipient):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return

    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return

    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")


send_email("Привет, как дела?", "friend@example.com")
send_email("Привет, как дела?", "friend@example.com", sender="another.email@example.com")
send_email("Привет, как дела?", "friend@example.com", sender="university.help@gmail.com")
send_email("Привет, как дела?", "friend@example")
send_email("Привет, как дела?", "university.help@gmail.com", sender="university.help@gmail.com")
