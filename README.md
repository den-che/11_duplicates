# Anti-Duplicator
Описание 

Скрипт в указанной директории просматривает все файлы и папки, также подпапки и выводит информацию о файлах-дублях.

#Пример
<p><pre><code>
C:\projects\devman\11_duplicates>python duplicates.py --path C:\work_dir
Дублика ты найдены: C:\work_dir\scripts\test.txt        C:\work_dir\scripts\Assignment1_week2\tets\test.txt
Дублика ты найдены: C:\work_dir\scripts\Assignment1_week2\tets\text\32423\test1.txt        C:\work_dir\scripts\trw\tst\test1.txt
</code></pre></p>

# Описание

Для получение данных необходимо запустить скрипт
<p><pre><code>python duplicates.py --path [путь до папки]</code></pre><p>

В качестве справки по аргументам командной строки можно вызвать.
<p><pre><code>python duplicates.py --help</code></pre><p>

После выполнения скрипт выдаст все файлы которые повторяются в этой директории и её поддиректориях

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
