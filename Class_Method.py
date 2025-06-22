class person:
    name = "anonymous"

    # def change_name(obj,name):
    #     self.__class__.name = "Rahul"
    
    @classmethod
    def change_name(cls,name):
        cls.name = name

p1 = person()
p1.change_name("John Doe")
print(person.name)
print(p1.name) 