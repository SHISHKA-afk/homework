def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()

#inner_function вне test_function выдаст ошибку т.к вне функции её не существует
