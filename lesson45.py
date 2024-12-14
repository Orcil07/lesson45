import time
import threading

def write_words(word_count, file_name):
    with open(file_name, 'w') as f:
        for i in range(1, word_count + 1):
            f.write(f"какое-то слово №{i}")
            if i < word_count:  # Добавляем запятую, если это не последний элемент
                f.write(', ')
            time.sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")

# Измерение времени выполнения функций
start_time = time.time()

# Вызовы функций
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end_time = time.time()
print(f"Работа функций {end_time - start_time:.6f} секунд")

# Создание потоков
threads = []
start_time_threads = time.time()

for args in [(10, 'example5.txt'), (30, 'example6.txt'),
             (200, 'example7.txt'), (100, 'example8.txt')]:
    thread = threading.Thread(target=write_words, args=args)
    threads.append(thread)
    thread.start()

# Ожидание завершения потоков
for thread in threads:
    thread.join()

end_time_threads = time.time()
print(f"Работа потоков {end_time_threads - start_time_threads:.6f} секунд")