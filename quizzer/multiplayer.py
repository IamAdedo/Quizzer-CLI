import socket
import threading
from typing import List

class QuizServer:
    def __init__(self, host: str = '0.0.0.0', port: int = 5000):
        self.clients: List[socket.socket] = []
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))

    def broadcast(self, message: str):
        """Send message to all clients."""
        for client in self.clients:
            client.send(message.encode())

    def handle_client(self, client: socket.socket):
        """Manage a single client connection."""
        self.clients.append(client)
        self.broadcast("New player joined!")

    def start(self):
        """Start the multiplayer server."""
        self.server.listen()
        print(f"🚀 Server running on port {self.server.getsockname()[1]}")
        while True:
            client, _ = self.server.accept()
            threading.Thread(target=self.handle_client, args=(client,)).start()
