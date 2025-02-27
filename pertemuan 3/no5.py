# Parent class
class Bird:
    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

# Child class
class Penguin(Bird):
    def __init__(self):
        # Memanggil constructor dari parent class
        super().__init__()
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")

# Membuat objek dari class Penguin
peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()
