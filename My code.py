import time
import sys

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def loading_animation(duration=2):
    animation = "|/-\\"
    end_time = time.time() + duration
    while time.time() < end_time:
        for char in animation:
            sys.stdout.write(f'\rЗагружается... {char}')
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write('\r')
    sys.stdout.flush()

slow_print("Добро пожаловать в систему персонализации!")
name = input("\nКак тебя зовут? ")
age = input("Сколько тебе лет? ")
color = input("Какой твой любимый цвет? ")

slow_print(f"\nПривет, {name}! Сейчас всё настроим...")
loading_animation(2)

slow_print("\n=== ВАШ ПРОФИЛЬ ===")
slow_print(f"👤 Имя: {name}")
slow_print(f"🎂 Возраст: {age} лет")
slow_print(f"🎨 Любимый цвет: {color}")

if int(age) >= 18:
    slow_print("Статус: совершеннолетний пользователь")
else:
    slow_print("Статус: юный исследователь")

slow_print("\nНастройка завершена! Приятного дня! ✨")
L
