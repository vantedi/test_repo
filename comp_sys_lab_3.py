import csv
import time
import psutil
from pynput import mouse

#Функция для получения данных о CPU
def get_cpu_metrics():
    cpu_percent = psutil.cpu_percent(interval=1)  #Загрузка процессора в процентах
    return [("CPU Загрузка", cpu_percent)]

#Функция для мониторинга времени использования мыши
def on_mouse_move(x, y):
    global mouse_seconds
    mouse_seconds += 1

#Функция для записи данных в CSV файл
def write_to_csv(data):
    with open('metrics.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        for entry in data:
            timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
            metric_name, metric_value = entry
            writer.writerow([timestamp, metric_name, metric_value])

mouse_listener = mouse.Listener(on_move=on_mouse_move)
mouse_listener.start()

try:
    mouse_seconds = 0

    while True:
        cpu_metrics = get_cpu_metrics()
        mouse_metrics = [("Использование мыши (секунды)", mouse_seconds)]

        all_metrics = cpu_metrics + mouse_metrics
        write_to_csv(all_metrics)

        time.sleep(60)  #Ожидание 1 минута

except KeyboardInterrupt:
    mouse_listener.stop()