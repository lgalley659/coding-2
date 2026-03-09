

class carModel:
    def __init__(self, model, color, engine ):
        self.model = model
        self.color = color
        self.engine = engine

    def color(self):
        print('color is blue')

    def speed(self):
        print(self.model + 'goes 50 miles per hour')