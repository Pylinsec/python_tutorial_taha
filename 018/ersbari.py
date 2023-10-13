class Baba:
    def __init__(self,baba_name , maman_name):
        self.maman_name = maman_name
        self.baba_name = baba_name
        print(self.baba_name)


    def print_baba_kojast(self):
        print(f"dadash {self.baba_name} sare kar hasat")


class Maman():
    def __init__(self,baba_name , maman_name):
        self.maman_name = maman_name
        self.baba_name = baba_name
        print(self.maman_name)
    def print_maman_kojast(self):
        print(f"dadash {self.maman_name} dar khane hast")


class Baby(Baba,Maman):
    def __init__(self,baby_name,baba_name,maman_name):
        self.baby_name = baby_name
        super().__init__(baba_name,maman_name)
        print(self.baby_name)
    def print_baby_kojast(self):
        print(f"dadash {self.baby_name} dar mahd koodak hast")
a = Baby


a("oliver","jack","sara").print_baby_kojast()
a("oliver","jack","sara").print_baba_kojast()
a("oliver","jack","sara").print_maman_kojast()