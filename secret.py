class Message:

    def __init__(self, image: str):
        self.image = image

    def write(self, message):
        message_as_byte = bytes(message, "utf-8")
        with open(self.image, "ab") as hider:
            hider.write(message_as_byte)

    def read(self):
        with open(self.image, "rb") as hider:
            image_content = hider.read()
            end_bytes = bytes.fromhex("FF D9")
            end = image_content.find(end_bytes)
            if end == -1:
                raise ValueError("End marker not found in JPG.")
            
            print(image_content[end+2:])

    def ReSeT(self):
        with open(self.image, "rb") as hider:
            image_content = hider.read()
            end = image_content.find(bytes.fromhex("FF D9"))
            if end == -1:
                raise ValueError("End marker not found in JPG.")
            
        with open(self.image, "wb") as hider:
            hider.write(image_content[:end+ len(bytes.fromhex("FFD9"))])