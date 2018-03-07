class CustomSet(object):
    def __init__(self, elements=[]):
        self.elements = elements

    def isempty(self):
        return self.elements == []

    def __contains__(self, element):
        return element in self.elements

    def issubset(self, other):
        return all(item in other for item in self.elements)

    def isdisjoint(self, other):
        return all(item not in other for item in self.elements)

    def __eq__(self, other):
        return all(a == b for a, b in zip(self.elements, other))

    def add(self, element):
        if element not in self.elements:
            self.elements.append(element)

    def intersection(self, other):
        return CustomSet(elements=[
            item for item in self.elements
            if item in other
        ])

    def difference(self, other):
        return CustomSet(elements=[
            item for item in self.elements
            if item not in other
        ] + [
            item for item in other
            if item not in self.elements
        ])

    def union(self, other):
        pass
