#!/bin/python3

class APIKeyConfig(Exception): 
    """
    Raises an exception if the API key is not set
    """

    pass

class InvalidMachine(Exception):
    """
    Raises an exception if the machine is not on database
    """

    pass
