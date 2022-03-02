class Parent:
    def __init__(self, ten, tuoi):
        self.ten = ten;
        self.tuoi = tuoi;

    def showDetail(self):
        print("Ten: {}\n Tuoi: {}".format(self.ten, self.tuoi))