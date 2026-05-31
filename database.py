class DataBase:
    def __init__(self):
        self.data ={}
    def set(self, key, value):
        self.data[key]=value
    def get(self,key):
        return self.data.get(key, None)
    def delete(self,key):
        if key in self.data:
            del self.data[key]
            return True
        return False
db=DataBase()
db.set("name","Yulia")
print(db.get("name"))
db.delete("name")
print(db.get("name"))
