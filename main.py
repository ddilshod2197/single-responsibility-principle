class SOLID:
    def __init__(self):
        self.s = "Single responsibility principle"
        self.o = "Open/closed principle"
        self.l = "Liskov substitution principle"
        self.i = "Interface segregation principle"
        self.d = "Dependency inversion principle"

    def single_responsibility(self):
        return self.s

    def open_closed(self):
        return self.o

    def liskov_substitution(self):
        return self.l

    def interface_segregation(self):
        return self.i

    def dependency_inversion(self):
        return self.d

solid = SOLID()
print(solid.single_responsibility())
print(solid.open_closed())
print(solid.liskov_substitution())
print(solid.interface_segregation())
print(solid.dependency_inversion())
```

```python
class SingleResponsibility:
    def __init__(self):
        self.name = "Single responsibility principle"

    def description(self):
        return "A class should have only one reason to change."

class OpenClosed:
    def __init__(self):
        self.name = "Open/closed principle"

    def description(self):
        return "A class should be open for extension but closed for modification."

class LiskovSubstitution:
    def __init__(self):
        self.name = "Liskov substitution principle"

    def description(self):
        return "Subtypes should be substitutable for their base types."

class InterfaceSegregation:
    def __init__(self):
        self.name = "Interface segregation principle"

    def description(self):
        return "A client should not be forced to depend on interfaces it does not use."

class DependencyInversion:
    def __init__(self):
        self.name = "Dependency inversion principle"

    def description(self):
        return "High-level modules should not depend on low-level modules. Both should depend on abstractions."

solid_principles = [SingleResponsibility(), OpenClosed(), LiskovSubstitution(), InterfaceSegregation(), DependencyInversion()]
for principle in solid_principles:
    print(principle.name)
    print(principle.description())
    print()
