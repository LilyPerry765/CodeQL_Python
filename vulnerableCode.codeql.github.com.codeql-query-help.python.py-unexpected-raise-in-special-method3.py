#Incorrect file-backed table
class FileBackedTable(object):
    
    def __getitem__(self, key):
        if key not in self.index:
            raise IOError("Key '%s' not in table" % key)
        else:
            #May raise an IOError
            return self.backing.get_row(key)