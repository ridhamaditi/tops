class Vector:

    def __init__(self, alist):
        self.alist = alist

    def __len__(self):
        return len(self.alist)

    def __repr__(self):
        return str(self.alist)

    def __add__(self, other):
        if(type(self.alist) != list or type(other.alist) != list):
            return "error"
        else:
            if(len(self.alist) != len(other.alist)):
                return "error"
            else:
                result = []
                for i in range(len(self.alist)):
                    temp = self.alist[i] + other.alist[i]
                    result.append(temp)
                return result

    def __sub__(self, other):
        if(type(self.alist) != list or type(other.alist) != list):
            return "error"
        else:
            if(len(self.alist) != len(other.alist)):
                return "error"
            else:
                result = []
                for i in range(len(self.alist)):
                    temp = self.alist[i] - other.alist[i]
                    result.append(temp)
                return result

    def __mul__(self, other):
        if(type(self.alist) == list and type(other) == int):
            result = []
            for i in self.alist:
                temp = i * other
                result.append(temp)
            return result

    def __rmul__(self, other):
        if(type(self.alist) == list and type(other) == int):
            result = []
            for i in self.alist:
                temp = i * other
                result.append(temp)
            return result
