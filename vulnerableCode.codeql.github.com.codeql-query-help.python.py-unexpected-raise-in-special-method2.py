#Abstract base class, but don't declare it.
class ImplicitAbstractClass(object):
    
    def __add__(self, other):
        raise NotImplementedError()