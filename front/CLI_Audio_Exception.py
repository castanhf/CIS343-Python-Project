#import exceptions

class CLI_Audio_Exception(Exception):
    def error(self):
        return "Audio Exception:\n"

class CLI_Audio_File_Exception(CLI_Audio_Exception):
    def error(self):
        super().error()
        return "File can't be played for some reason. Maybe it's not there?\n"

class CLI_Audio_Screen_Size_Exception(CLI_Audio_Exception):
    def error(self):
        super().error()
        return "Audio Screen Size is too small\n"


    # name of file: CLI_Audio_Exception
    # import: CLI_Audio_Exception
    # we import the class of a file because a file can have more
    # than one class
    # from CLI_Audio_Exception import CLI_Audio_Exception

    ## PRINT an object
    # example: def __str__(self):
    # basically a toString() method

    # Python does not support object assignment YET

    # override with __setitem__(self, key, value):
    # self.items[key] = value
    # python convention

    # override with __getitem__(self, index):
    # return self.items[index]

    # def __add__(self, other_scc):
    # return self.items + other_scc.items
    ## Note: other_scc will be a default list, not a SCC object
    ## Proper way to write this function:
    ## Create a new SCC of size of both added
    ## add all elements of both
    ## return new SCC
