class DictHash:
    def __init__(self,size=0):
        self.size = size
        self.hd = {}

    def __str__(self):
        return f"{self.size}"

    def __contains__(self, nyckel):
        return nyckel in self.hd

    def store(self,nyckel,data):
        self.hd[nyckel] = data
        self.size += 1

    def search(self,nyckel):
        try:
            if nyckel in self.hd:
                print(f"{nyckel} finns med i listan av k-drama!")
                print(f"Datan för {nyckel} är: {self.hd[nyckel]}")
            else:
                raise KeyError
        except KeyError:
            print(f"{nyckel} finns inte med i listan!")







