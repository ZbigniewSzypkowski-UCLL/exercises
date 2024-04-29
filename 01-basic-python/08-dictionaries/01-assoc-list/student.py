class AssocList:
    def __init__(self):
        self.__items = []

    def __setitem__(self, key, value):
        found = False
        for i in range(len(self.__items)):
            if key in self.__items[i]:
                self.__items[i] = [key, value]
                found = True
        if not found:
            self.__items.append([key, value])

    def __getitem__(self, key):
        for object in self.__items:
            if key in object:
                return object[1]
        raise KeyError()
    
    def __contains__(self, object):
        for i in self.__items:
            if object in i:
                return True

    def __len__(self):
        return len(self.__items)
    
    @property
    def keys(self):
        keys = []
        for i in self.__items:
            keys.append(i[0])
        return keys
    
    @property
    def values(self):
        values = []
        for i in self.__items:
            values.append(i[1])
        return values
    
    def items(self):
        return self.__items