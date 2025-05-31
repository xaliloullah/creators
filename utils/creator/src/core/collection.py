class Collection:
    
    def __init__(self, *data):   
        data = list(data) 
        if len(data) == 1: 
            self.data = data[0]
        else: 
            self.data = data
            
    def get(self, keys:str=None, default=None):
        data = self.data
        if keys:
            try:
                for key in keys.split("."):
                    if isinstance(data, (list, tuple)):
                        index = data.index(key)
                        data = data[index]
                    else: 
                        data = data[key]
            except:
                return default
        return data  
    
    def set(self, keys: str, value):
        keys = keys.split(".")
        data = self.data 

        for key in keys[:-1]: 
            if key not in data or not isinstance(data[key], dict):
                data[key] = {}
            data = data[key]
        data[keys[-1]] = value 

    def create(self, data):
        return Collection(*data)
    
    def all(self):
        return self

    def add(self, item):
        self.data.append(item)
        
    def update(self, old, new):
        if old in self.data:
            index = self.data.index(old)
            self.data[index] = new
        else: 
            self.data.append(new)
    
    def remove(self, item):   
        if item in self.data:
            index = self.data.index(item)
            self.data.pop(index)
        
    def find(self, **kwargs): 
        for item in self.data:
            if isinstance(item, dict):
                if all(item.get(key) == value for key, value in kwargs.items()): 
                    return item
            else:
                if all(item == value for key, value in kwargs.items()):
                    return item
        return None
    
    def where(self, **kwargs):
        for item in self.data:
            if isinstance(item, dict):
                if all(item.get(key) == value for key, value in kwargs.items()):
                    self.data = item 
                else:
                    if all(item == value for key, value in kwargs.items()): 
                        self.data = item 
                    else:
                        self.data = None 
        return self
    
    def first(self, func=None): 
        if func:
            for item in self.data:
                if func(item):
                    return item
        return self.data[0] if self.data else None  
    
    def last(self, func=None):
        if func:
            for item in reversed(self.data):
                if func(item):
                    return item
        return self.data[-1] if self.data else None 

    def sort(self, key=None, reverse=False):
        return Collection(sorted(self.data, key=key, reverse=reverse)) 
    
    def new(self, data):
        return Collection(*data)
    
    def filter(self, func):
        return Collection(filter(func, self.data))

    def map(self, func):
        return Collection(map(func, self.data))

    def reduce(self, func, initial=None):
        from functools import reduce
        return reduce(func, self.data, initial)

    def chunk(self, size):
        return Collection([self.data[i:i + size] for i in range(0, len(self.data), size)]) 
    
    def pluck(self, key):
        return Collection(item.get(key) for item in self.data if isinstance(item, dict)) 
    
    def merge(self, other) -> 'Collection': 
        self.data.extend(other)
        return self
    
    def count(self) -> int: 
        return len(self.data)

    def sum(self, key= None): 
        if key:
            return sum(key(item) for item in self.data)
        return sum(self.data)

    def avg(self, key= None): 
        if not self.data:
            return None
        return self.sum(key) / self.count()

    def max(self, key= None): 
        if not self.data:
            return None
        return max(self.data, key=key) if key else max(self.data)

    def min(self, key= None): 
        if not self.data:
            return None
        return min(self.data, key=key) if key else min(self.data)
    
    def json(self):
        import json
        return json.dumps(self.data) 
    
    def dict_to_list(self):
        return list(self.data.items())
    
    def __getitem__(self, index):
        return self.data[index]
    
    def __setitem__(self, index, value):
        self.data[index] = value

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        return iter(self.data)

    def __str__(self):
        return f"{self.data}"
    
    def __delitem__(self, index):
        del self.data[index]

    def __call__(self, index):
        return self.data[index] if index < len(self.data) else None
    
    def __repr__(self):
        return f"Collection({self.data})"
    
    def __add__(self, other):
        if isinstance(other, Collection):
            return Collection(self.data + other.data)
        raise TypeError("Unsupported type for addition")



# Usage:
# collection = Collection([1, 2, 3, 4, 5])
# print(collection)
# print(collection.all())
# print(collection.count())
# print(collection.sum())
# print(collection.avg())
# print(collection.max())
# print(collection.min())
# print(collection.first())
# print(collection.last())
# print(collection.where(2))
# print(collection.sort())
# print(collection.chunk(2))
# print(collection.pluck('name'))
# print(collection.merge([6, 7, 8, 9, 10]))
# print(collection.filter(lambda x: x % 2 == 0))
# print(collection.map(lambda x: x * 2))
# print(collection.reduce(lambda x, y: x + y))
# print(collection.get(2))
# print(collection.set(2, 10))
# print(collection.new([1, 2, 3, 4, 5]))
# print(collection.add(6))
# print(collection.remove(2))
# print(collection.find(2))
# print(collection[2])
# collection[2] = 10
# for item in collection:
#     print(item)
# print(collection)
# print(collection.data)
# print(collection.__repr__())
# print(collection.__str__())
# print(collection.__len__())
# print(collection.__iter__())
# print(collection.__getitem__(2))
# print(collection.__setitem__(2, 10) 