import json
import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

exact_value = 0.9445171858994637

def view(file_name, ax, color):
    calculated_data = {}
    
    with open(f'./assets/{file_name}', 'r') as file:
        calculated_data = json.load(file)
    
    data = {
        'Количество': [],
        'Относительное отклонение': []
    }
    
    for key in calculated_data:
        data['Количество'].append(int(key))
        data['Относительное отклонение'].append(abs(calculated_data[key] - exact_value) / exact_value)
        
    df = pd.DataFrame(data)

    ax.plot(df['Количество'], df['Относительное отклонение'], marker='o', linestyle='-', color=color, label=file_name)

def main():
    contents = os.listdir('./assets')
    
    # Создаем одну фигуру и один набор осей
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Используем разные цвета для каждого файла
    colors = plt.cm.jet(np.linspace(0, 1, len(contents)))
    
    for i, item in enumerate(contents):
        view(item, ax, colors[i])
    
    ax.set_title('Относительное отклонение от точного значения')
    ax.set_xlabel('Количество (псевдо)случайных точек')
    ax.set_ylabel('Относительное отклонение от точного значения')
    ax.grid(True)
    ax.legend()
    
    plt.savefig('../output/deviations-combined.png')
