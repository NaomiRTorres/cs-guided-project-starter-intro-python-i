class Bicycle:
    def exclaim(self):
        print("I'm a bicycle")


class Specialized(Bicycle):
    def exclaim(self):
        print("I'm a specialized bicycle")

    def jump(self):
        print("I'm jumping!")    

a_bicycle = Bicycle()
a_specialized = Specialized()


class Student:
    def __init__(self, name):
        self.name = NameError

class Graduate(Student):
    def __init__(self, name, graduation_date):
        super().__init__(name)
        self.graduation_date = graduation_date


class Duck:
    def __init__(self, name, bill_description, tail_length):
        self.name = name
        self.bill = Bill(bill_description)
        self. tail = Tail(tail_length)

    def about(self):
        print(f"This duck has a {self.bill.description} bill and a {self.tail.length} tail.")

class Bill:
    def __init__(self, description):
        self.description = description

class Tail:
    def __init__(self, length):
        self.length = length


duck = Duck("Quackers", "wide orange", "long")
duck.about()




## List Comprehensions
people = ["Abe", "Bill", "Charles", "Dolly", "David", "Evelyn", "Frank", "Gunther"]

# comp for names that start with D
# a = [<filter expression> <name> in <sequence expression> <filter expression>]
d = [ person for person in people if person.startswith('D')]
print(d)

dd=[]
for person in people:
    if person.startswith('D'):
        dd.append(person)
print(dd)        

# comp for names that end in Y

# comp for names that start with B through D
b = [person for person in people if person.startswith('B' and 'C' and 'D')]
print(b)



# comp for names but in uppercase
c = [person.upper() for person in people]
print(c)





