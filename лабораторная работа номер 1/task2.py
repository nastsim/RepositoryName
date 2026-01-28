# Исходные данные
diskette_size_mb = 1.44  # Объем дискеты в Мб
pages_per_book = 100  # Количество страниц в книге
lines_per_page = 50  # Число строк на странице
chars_per_line = 25  # Количество символов в строке
bytes_per_char = 4  # Байт на символ

# Вычисляем количество символов в одной книге
chars_per_book = pages_per_book * lines_per_page * chars_per_line

# Вычисляем размер одной книги в байтах
book_size_bytes = chars_per_book * bytes_per_char

# Переводим размер дискеты из Мб в байты
# 1 Мб = 1024 Кб, 1 Кб = 1024 байта
diskette_size_bytes = diskette_size_mb * 1024 * 1024

# Вычисляем количество книг, которые поместятся на дискету
books_on_diskette = int(diskette_size_bytes / book_size_bytes)

print("Количество книг, помещающихся на дискету:", books_on_diskette)