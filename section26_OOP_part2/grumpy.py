class GrumpyDict(dict):
    def __repr__(self):
        print("NONE OF YOUR BUSINESS")
        return super().__repr__()

    def __missing__(self, key):
        print(f"YOU WANT {key}? WELL IT AIN'T HERE!")

    def __setitem__(self, key, value):
        print(f"YOU WANT TO CHANGE THE DICTIONARY?")
        print("OK FINE...")
        super().__setitem__(key, value)

    def __contains__(self, item):
        print("NO IT AINT IN HERE!")
        return False


data = GrumpyDict({"first": "Tom", "animal": "cat"})
print(data)
print("================================")
data['city'] = "Tokyo"
print(data)

"city" in data
