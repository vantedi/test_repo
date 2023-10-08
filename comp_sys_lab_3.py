import csv
import time
import psutil
from pynput import mouse

#������� ��� ��������� ������ � CPU
def get_cpu_metrics():
    cpu_percent = psutil.cpu_percent(interval=1)  #�������� ���������� � ���������
    return [("CPU ��������", cpu_percent)]

#������� ��� ����������� ������� ������������� ����
def on_mouse_move(x, y):
    global mouse_seconds
    mouse_seconds += 1

#������� ��� ������ ������ � CSV ����
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
        mouse_metrics = [("������������� ���� (�������)", mouse_seconds)]

        all_metrics = cpu_metrics + mouse_metrics
        write_to_csv(all_metrics)

        time.sleep(60)  #�������� 1 ������

except KeyboardInterrupt:
    mouse_listener.stop()