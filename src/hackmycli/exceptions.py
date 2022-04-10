#!/bin/python3

class APIKeyNotFound(Exception): 
    """
    Raises an exception if the API key is not set
    """

    pass

class MachineNotFound(Exception):
    """
    Raises an exception if the machine is not on database
    """

    pass

class KeywordNotFound(Exception):
    """
    Raises an exception if the key do not exist on config database
    """

    pass

class CategoryNotFound(Exception):
    """
    Raises an exception if the category do not exist on database
    """

    pass

class LevelNotFound(Exception):
    """
    Raises an exception if the level do not exist on database
    """

    pass

class DownloadParamsInconsistency(Exception):
    """
    Raises an exception if the download parameters are bad configured
    """

    pass
