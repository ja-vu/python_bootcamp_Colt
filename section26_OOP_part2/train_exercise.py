class Train():
    def __init__(self, num_cars):
        self.num_cars = num_cars

    def __repr__(self):
        print("{} car train".format(self.num_cars))

    def __len__(self):
        return self.num_cars

a_train = Train(3)
print(a_train)
print(len(a_train))