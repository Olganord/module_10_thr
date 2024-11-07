import time
from multiprocessing import Pool


def read_info(name):
    all_data = []  # Локальный список для хранения данных
    with open(name, 'r') as file:
        while True:
            line = file.readline()  # Читаем строку
            if not line:  # Проверяем на пустую строку
                break
            all_data.append(line.strip())  # Добавляем строку в список


if __name__ == '__main__':

    filenames = [f'./file {number}.txt' for number in range(1, 5)]  # Список файлов

    # Линейный вызов
    start_linear = time.time()
    for filename in filenames:
        read_info(filename)  # вызываем функцию read_info для каждого файла в цикле и
        # замеряем общее время выполнения
    print(f'{time.time() - start_linear:.1f} (линейный)')

    # Многопроцессный вызов
    start_parallel = time.time()
    with Pool() as pool:  # Используем контекстный менеджер with Pool() для создания пула процессов
        results = pool.map(read_info, filenames)  # Вызываем функцию map, которая применяет функцию read_info
        # ко всем элементам списка filenames. Это позволяет выполнять чтение файлов параллельно.
    end_parallel = time.time()  # Замеряем время выполнения параллельного подхода.
    print(f'{end_parallel - start_parallel:.1f} (многопроцессный)')
