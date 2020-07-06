class Vec2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'X: {} Y: {}'.format(self.x,self.y)
