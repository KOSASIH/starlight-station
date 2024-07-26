# telescope_control.py
import time
import threading
import queue

class Telescope:
    def __init__(self, name: str, mount_type: str, connection_type: str):
        self.name = name
        self.mount_type = mount_type
        self.connection_type = connection_type
        self.connected = False
        self.image_queue = queue.Queue()

    def connect(self, ip_address: str, port: int):
        # Connect to the telescope using the provided IP address and port
        self.connected = True

    def disconnect(self):
        # Disconnect from the telescope
        self.connected = False

    def align(self, target: str):
        # Align the telescope to the specified target
        if not self.connected:
            raise Exception("Telescope is not connected")

        # Example alignment process
        time.sleep(1)
        print(f"Aligning {self.name} to {target}...")
        time.sleep(1)
        print(f"{self.name} is now aligned to {target}")

    def capture_image(self):
        # Capture an image using the telescope
        if not self.connected:
            raise Exception("Telescope is not connected")

        # Example image capture process
        time.sleep(1)
        image_data = np.random.rand(1080, 1920, 3)  # Generate random image data
        self.image_queue.put(image_data)
        print(f"Image captured by {self.name}")

    def get_image(self):
        # Get the next image from the image queue
        return self.image_queue.get()

# Example usage:
telescope = Telescope("Starlight Station", "Alt-Az GoTo", "WiFi")
telescope.connect("192.168.1.1", 4030)
telescope.align("Saturn")
telescope.capture_image()
image_data = telescope.get_image()
print(image_data.shape)
telescope.disconnect()
