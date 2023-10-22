import json
import time

localtime =time.localtime()
print(f'{localtime.tm_hour}:{localtime.tm_min}')

with open('tasks1.1.txt', encoding='utf-8') as file:
    content = file.read()

tasks = content.split('|')
print(tasks)

