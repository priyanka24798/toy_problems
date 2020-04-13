class lrucache:
    
    
    def __init__(self, length):

        self.length = length
        self.lru = []
        self.lrudict = {}
       

    def put(self, key):
        if (len(self.lru) < self.length):

             if key in self.lru:
                 self.lru.remove(key)
                 self.lru.append(key)
                 value = str(key)+ " is from IIIT hyderabad"
                 self.lrudict[key] = value
             else:
                self.lru.append(key)
                value = str(key)+ " is from IIIT hyderabad"
                self.lrudict[key] = value
        else:
             
             r = self.lru.pop(0)
             del self.lrudict[r]
             self.lru.append(key)
             value = str(key)+ " is from IIIT hyderabad"
             self.lrudict[key] = value


    def get(self, key, value = None):
        
        if key in self.lru:
            return self.lrudict[key]
        
        else:
            return value

    def get_cache(self):
        f = []
        for key in reversed(self.lru):
            f.append(key + " : " + self.lrudict[key])
        return f
