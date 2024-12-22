def send_email (message, recipient, *, sender="university.help@gmail.com"):
    if not (recipient.count('@') > 0 and sender.count('@') > 0 and (recipient.endswith((".com", ".ru", ".net")))
            and (sender.endswith((".com", ".ru", ".net")))):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return
    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return
    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")
        return
    print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")


send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
