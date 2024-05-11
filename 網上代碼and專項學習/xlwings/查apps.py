import xlwings as xw

# 獲取所有運行中的Excel應用實例
for app in xw.apps:
    print(f'Excel應用程序 ID: {app.pid}')
    for book in app.books:
        print(f' - Workbook 名稱: {book.name}')