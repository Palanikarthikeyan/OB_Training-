
class Laptop:
    def code(self):
        print("Writing code")

class Mobile:
    def code(self):
        print("Coding on mobile")

def start_coding(device):
    device.code()

start_coding(Laptop())
start_coding(Mobile())
