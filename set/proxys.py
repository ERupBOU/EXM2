def getproxy():
    proxy_host = input("Введите хост прокси-сервера: ")
    proxy_port = input("Введите порт прокси-сервера: ")

    with open("proxy.py", "w") as f:
        f.write(f"PROXY_HOST = '{proxy_host}'\n")
        f.write(f"PROXY_PORT = {proxy_port}\n")

    print("Настройки прокси-сервера сохранены в файл proxy.py.")