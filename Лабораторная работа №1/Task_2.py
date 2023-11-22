size_, count_page, count_lines, count_symbols = (1.44 * 1024 * 1024), 100, 50, 25

size_book = 4 * count_symbols * count_lines * count_page

print(f"Количество книг, которое можно поместить на дискету = {round(size_ // size_book)}")