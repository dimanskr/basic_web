from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):

    """
        Специальный класс, который отвечает за
        обработку входящих запросов от клиентов
    """
    filename = 'index.html'

    def _get_content_data(self):
        with open(self.filename, "r", encoding="utf-8") as f:
            context = f.read()
        return context

    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(self._get_content_data(), "utf-8"))


if __name__ == "__main__":
    # Инициализация веб-сервера
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        # Cтарт веб-сервера в бесконечном цикле прослушивания входящих запросов
        webServer.serve_forever()
    except KeyboardInterrupt:
        # Корректный способ остановить сервер в консоли через сочетание клавиш Ctrl + C
        pass

    # Корректная остановка веб-сервера, чтобы он освободил адрес и порт в сети, которые занимал
    webServer.server_close()
    print("Server stopped.")
