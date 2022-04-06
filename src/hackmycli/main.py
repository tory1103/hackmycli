#!/bin/python3

import fire
from my_pickledb import LoadPickleDB


class HackMyCLI:
    """
    HackMyVM command-line tool

    It is a tool for managing HackMyVM platform basics.
    It includes some of this utilities:
        - List all avaliable machine
        - Download machines 
        - Insert flags to machines
        - Local configuration basics

    Before using it, you must configure your username and password with config command
    Try: python3 main.py config fresh <username> <password>

    Author : Adrian Toral
    Date   : 06-04-2022
    Latest : v0-beta
    """

    def __init__(self):
        """
        HackMyCLI main command manager
        """

        self.__database = LoadPickleDB("config.json")
        self.config = self.__config(self.__database)

    class __config:
        def __init__(self, database: LoadPickleDB):
            """
            Basic configuration manager

            :param database: PickleDB object for handling the configuration file
            """

            self.__database = database

        def fresh(self, username:str, password:str, clean:bool=False):
            """
            Updates configuration username and password

            :param username: Username to be saved
            :param password: Password to be saved
            :param clean: Cleans configuration file before saving new data
            """

            if clean: self.__database.clear()

            self.username(username)
            self.password(password)

        def username(self, username: str):
            """
            Updates configuration username

            :param username: Username to be saved
            """
            
            self.add("username", username)            

        def password(self, password:str):
            """
            Updates configuration password

            :param password: Password to be saved
            """

            self.add("password", password)

        def add(self, key:str, value):
            """
            Inserts custom key and value into configuration file

            :param key: Keyword to be saved
            :param value: Value of the keyword to be saved
            """

            self.__database.set(key, value)
            self.__database.save.as_json()

        def remove(self, key):
            """
            Removes custom key from configuration file

            :param key: Keyword to be removed
            """

            if self.__database.exists(key): 
                self.__database.pop(key)
                self.__database.save.as_json()

            else: raise Exception("Invalid keyword. It do not exists on configuration file")

    def list(self, level:str="all"):
        """
        Lists all avaliable machines based on level

        Level types:
            - All    : Lists all avaliable machines (Default)
            - Easy   : Lists all easy level machines
            - Medium : Lists all medium level machines
            - Hard   : Lists all hard level machines

        :param level: Level type to list
        """

        level_types = ["all", "easy", "medium", "hard"]
        level  = level if level.lower() in level_types else "all"

        machines = []

        # List all machines

        return machines

    def checkflag(self, flag:str, machine:str, no_verify:bool=False):
        """
        Inserts the flag into the machine if valid

        Machine must exist on hackmyvm database
        If the tag is not valid, it would not insert it

        If the 'no_verify' parameter is True, it would not check if the machine is valid or exists on database (not recommended)

        :param flag: Flag to insert into machine
        :param machine: Destination machine to insert the flag
        :param no_verify: Skips machine existence check
        """

        inserted: bool = False

        if not no_verify:
            if machine not in self.list():
                raise Exception("Invalid machine. It do not exist on hackmyvm database")

        # Insert flag into machine

        return inserted

    def download(self, machine:str, no_verify:bool=False):
        """
        Downloads the machine from hackmyvm database

        If the 'no_verify' parameter is True, it would not check if the machine is valid or exists on database (not recommended)

        :param machine: Destination machine to download
        :param no_verify: Skips machine existence check
        """

        downloaded: bool = False
        
        if not no_verify:
            if machine not in self.list():
                raise Exception("Invalid machine. It do not exist on hackmyvm database")

        # Download the machine
        
        return downloaded

if __name__ == "__main__": fire.Fire(HackMyCLI)

