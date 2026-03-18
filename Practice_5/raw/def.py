from datetime import datetime, timedelta


date_str = input("Введите дату и время (формат YYYY-MM-DD HH:MM): ")
event_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M")


hours = int(input("Сколько часов добавить: "))
minutes = int(input("Сколько минут добавить: "))
seconds=int(input())

new_date = event_date + timedelta(hours=hours, minutes=minutes,seconds=seconds)

print("Исходная дата:", event_date)
print("После добавления:", new_date)