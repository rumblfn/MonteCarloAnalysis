import json
import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

def view(file_name, ax, color):
    calculated_data = {}
    
    with open(f'./assets/{file_name}', 'r') as file:
        calculated_data = json.load(file)
        
    data = {
        'Количество': [],
        'Площадь': []
    }
    
    for key in calculated_data:
        data['Количество'].append(int(key))
        data['Площадь'].append(calculated_data[key])
    
    df = pd.DataFrame(data)

    ax.plot(df['Количество'], df['Площадь'], marker='o', linestyle='-', color=color, label=file_name)

def main():
    contents = os.listdir('./assets')
    
    # Создаем одну фигуру и один набор осей
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Используем разные цвета для каждого файла
    colors = plt.cm.jet(np.linspace(0, 1, len(contents)))
    
    for i, item in enumerate(contents):
        view(item, ax, colors[i])
    
    ax.set_title('Вычисление площади пересечения кругов методом Монте-Карло')
    ax.set_xlabel('Количество (псевдо)случайных точек')
    ax.set_ylabel('Значение площади')
    ax.grid(True)
    ax.legend()
    
    plt.savefig('../output/measurements-combined.png')
