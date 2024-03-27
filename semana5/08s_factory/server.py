from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class DeliveryVehicle:
    def __init__(self, capacity):
        self.capacity = capacity
        self.packages_delivered = 0

    def deliver(self):
        if self.packages_delivered < self.capacity:
            self.packages_delivered += 1
            
            return f"Entrega nro: {self.packages_delivered} realizada con exito"
        else:
            return "El vehículo ha alcanzado su capacidad máxima de entregas"


class Motorcycle(DeliveryVehicle):
    def __init__(self):
        super().__init__(capacity=10)


class Drone(DeliveryVehicle):
    def __init__(self):
        super().__init__(capacity=20)


class DeliveryFactory:
    def create_delivery_vehicle(self, vehicle_type):
        if vehicle_type == "motorcycle":
            return Motorcycle()
        elif vehicle_type == "drone":
            return Drone()
        else:
            raise ValueError("Tipo de vehículo de entrega no válido")


class HTTPDataHandler:
    @staticmethod
    def handle_response(handler, status, data):
        handler.send_response(status)
        handler.send_header("Content-type", "application/json")
        handler.end_headers()
        handler.wfile.write(json.dumps(data).encode("utf-8"))

    @staticmethod
    def handle_reader(handler):
        content_length = int(handler.headers["Content-Length"])
        post_data = handler.rfile.read(content_length)
        return json.loads(post_data.decode("utf-8"))


class DeliveryRequestHandler(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.delivery_factory = DeliveryFactory()
        super().__init__(*args, **kwargs)

    def do_POST(self):
        if self.path == "/delivery":
            data = HTTPDataHandler.handle_reader(self)
            vehicle_type = data.get("vehicle_type")
            delivery_vehicle = self.delivery_factory.create_delivery_vehicle(
                vehicle_type
            )
            response_data = {"message": delivery_vehicle.deliver()}
            HTTPDataHandler.handle_response(self, 201, response_data)
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )


def main():
    try:
        server_address = ("", 8000)
        httpd = HTTPServer(server_address, DeliveryRequestHandler)
        print("Iniciando servidor HTTP en puerto 8000...")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor HTTP")
        httpd.socket.close()


if __name__ == "__main__":
    main()
