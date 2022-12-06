class Downtube_Error(Exception):
    """ This is the base exception class for all other user defined exception(classes) """
    pass

class Link_Error(Downtube_Error):
    """ When there is no Link is given as input """
    pass
    
class InvalidLink(Downtube_Error):
    """ When the ink URL isn't a youtube link """
    pass

class DirectoryError(Downtube_Error):
    """ when No directory is given """
    pass
class ResolutionError(Downtube_Error):
    """ when no resolution is givenn """
    pass