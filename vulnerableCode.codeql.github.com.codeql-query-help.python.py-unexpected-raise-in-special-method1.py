#Incorrect unhashable class
class MyMutableThing(object):
    
    def __init__(self):
        pass
    
    def __hash__(self):
        raise NotImplementedError("%r is unhashable" % self)