from dataclasses import dataclass, field

@dataclass(order=True)
class Person:
    sort_index: int = field(init = False, repr=False)
    name: str
    job: str
    age: str
    strength: int = 1000

    def __post_init__(self):
        self.sort_index = self.age
        self.screte = None

    def save_screte(self):
        self.screte  = 10

    def print_screte(self):
        print(self.screte)

p1 = Person("jiahao", "MLE", 25)
p2 = Person("huhu", "SDE", 30)
p3 = Person("jiahao", "MLE", 25)
print(p1)
print(p1 == p3)
print(p2 > p3)
p1.save_screte()
p1.print_screte()
p2.print_screte()