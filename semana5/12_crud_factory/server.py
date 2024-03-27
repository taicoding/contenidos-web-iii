from http.server import HTTPServer, BaseHTTPRequestHandler
import json

# Base de datos simulada de vehículos
vehicles = {}


class DeliveryVehicle:
    def __init__(self, vehicle_type, plate_number, capacity):
        self.vehicle_type = vehicle_type
        self.plate_number = plate_number
        self.capacity = capacity


class Motorcycle(DeliveryVehicle):
    def __init__(self, plate_number, capacity):
        super().__init__("motorcycle", plate_number, capacity)


class Drone(DeliveryVehicle):
    def __init__(self, plate_number, capacity):
        super().__init__("drone", plate_number, capacity)


class DeliveryFactory:
    @staticmethod
    def create_vehicle(vehicle_type, plate_number, capacity):
        if vehicle_type == "drone":
            return Drone(plate_number, capacity)
        elif vehicle_type == "motorcycle":
            return Motorcycle(plate_number, capacity)
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


class DeliveryService:
    def __init__(self):
        self.factory = DeliveryFactory()

    def add_vehicle(self, data):
        vehicle_type = data.get("vehicle_type", None)
        plate_number = data.get("plate_number", None)
        capacity = data.get("capacity", None)

        delivery_vehicle = self.factory.create_vehicle(
            vehicle_type, plate_number, capacity
        )
        vehicles[len(vehicles) + 1] = delivery_vehicle
        return delivery_vehicle

    def list_vehicles(self):
        return {index: vehicle.__dict__ for index, vehicle in vehicles.items()}

    def update_vehicle(self, vehicle_id, data):
        if vehicle_id in vehicles:
            vehicle = vehicles[vehicle_id]
            plate_number = data.get("plate_number", None)
            capacity = data.get("capacity", None)
            if plate_number:
                vehicle.plate_number = plate_number
            if capacity:
                vehicle.capacity = capacity
            return vehicle
        else:
            raise None

    def delete_vehicle(self, vehicle_id):
        if vehicle_id in vehicles:
            del vehicles[vehicle_id]
            return {"message": "Vehículo eliminado"}
        else:
            return None


class DeliveryRequestHandler(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.delivery_service = DeliveryService()
        super().__init__(*args, **kwargs)

    def do_POST(self):
        if self.path == "/deliveries":
            data = HTTPDataHandler.handle_reader(self)
            response_data = self.delivery_service.add_vehicle(data)
            HTTPDataHandler.handle_response(self, 201, response_data.__dict__)
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )

    def do_GET(self):
        if self.path == "/deliveries":
            response_data = self.delivery_service.list_vehicles()
            HTTPDataHandler.handle_response(self, 200, response_data)
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )

    def do_PUT(self):
        if self.path.startswith("/deliveries/"):
            vehicle_id = int(self.path.split("/")[-1])
            data = HTTPDataHandler.handle_reader(self)
            response_data = self.delivery_service.update_vehicle(vehicle_id, data)
            if response_data:
                HTTPDataHandler.handle_response(self, 200, response_data.__dict__)
            else:
                HTTPDataHandler.handle_response(
                    self, 404, {"message": "Vehículo no encontrado"}
                )
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )

    def do_DELETE(self):
        if self.path.startswith("/deliveries/"):
            vehicle_id = int(self.path.split("/")[-1])
            response_data = self.delivery_service.delete_vehicle(vehicle_id)
            if response_data:
                HTTPDataHandler.handle_response(self, 200, response_data)
            else:
                HTTPDataHandler.handle_response(
                    self, 404, {"message": "Vehículo no encontrado"}
                )
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
