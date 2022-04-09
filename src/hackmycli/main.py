#!/bin/python3

from fire import Fire
from requests import post
from exceptions import *
from prettytable.colortable import ColorTable, Themes
from my_pickledb import LoadPickleDB


class HackMyCLI:
    """
    HackMyVM command-line tool

    It is a tool for managing HackMyVM platform basics.
    It includes some of these utilities:
        - List all avaliable machine
        - Download machines 
        - Insert flags to machines
        - Local configuration basics
        - Submit challenges and machines
        - Get submit status

    Before using it, you must configure your username, password and API key with config command
    Try: python3 main.py config fresh <username> <password> <api_key>
         python3 main.py config key <api_key>

    Author : Adrian Toral
    Date   : 09-04-2022
    Latest : v01-beta
    """

    def __init__(self):
        """
        HackMyCLI main command manager
        """

        # Variables
        self.__database = LoadPickleDB("config.json")
        self.__api_url = "https://hackmyvm.eu/apio/"

        # Groups of commands
        self.config = self.__config(self.__database)
        self.submit = self.__submit(self.__database)

    class __config:
        def __init__(self, database: LoadPickleDB):
            """
            Basic configuration manager

            :param database: PickleDB object for handling the configuration file
            """

            self.__database = database

        def fresh(self, username: str, password: str, key: str, clean: bool = False):
            """
            Updates configuration username, password and key

            :param username: Username to be saved
            :param password: Password to be saved
            :param key: API key to be saved
            :param clean: Cleans configuration file before saving new data
            """

            if clean: self.__database.clear()

            self.username(username)
            self.password(password)
            self.key(key)

        def username(self, username: str):
            """
            Updates configuration username

            :param username: Username to be saved
            """

            self.add("username", username)

        def password(self, password: str):
            """
            Updates configuration password

            :param password: Password to be saved
            """

            self.add("password", password)

        def key(self, key: str):
            """
            Updates configuration API key

            :param key: API key to be saved
            """

            self.add("api_key", key)

        def add(self, key: str, value):
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

            if not self.__database.exists(key): raise KeywordNotFound("Keyword do not exist on config database. Check if it is spelled correctly")

            self.__database.pop(key)
            self.__database.save.as_json()


    class __submit:
        def __init__(self, database: LoadPickleDB):
            """
            Main submit command manager
            """

            self.__database = database

        def __existLevel(self, level: str):
            """
            Checks if a level is valid or not
            """

            levels = [
                    "Easy",
                    "Medium",
                    "Hard"
                    ]

            return True if level in levels else False

        def __existCategory(self, category: str):
            """
            Checks if a category is valid or not
            """

            categories = [
                    "Stego",
                    "Programming",
                    "Crypto",
                    "Web",
                    "Reversing",
                    "OSINT",
                    "Forensic",
                    "Misc"
                    ]

            return True if category in categories else False

        def challenge(self, category: str, flag: str, description: str, solution: str, url: str = None):
            """
            Submits a new challenge to hackmyvm

            Challenge categories:
                - Stego
                - Programming
                - Crypto
                - Web
                - Reversing
                - OSINT
                - Forensic
                - Misc

            :param category: Challenge category, it must be in the list above
            :param flag: Challenge flag
            :param description: Challenge level description
            :param solution: Challenge solution description
            :param url: Url where to download the challenge
            """

            # https://hackmyvm.eu/submit/registerchallenge.php
            # https://hackmyvm.eu/submit/registersubmit.php

            if not self.__existCategory(category): raise CategoryNotFound("Category do not exist on hackmyvm database. Check if it is spelled correctly")

            data = {
                    "chatype": category,
                    "challengeflag": flag,
                    "chalevel": description,
                    "chasolution": solution,
                    "challengeurl": url
                    }

            # Make post petition with data

            submited = data  # Petition

            return submited

        def machine(self, name: str, url: str, user_flag: str, root_flag: str, level: str, notes: str, writeup: str):
            """
            Submits a new machine to hackmyvm

            Machine levels:
                - Easy
                - Medium
                - Hard

            :param name: Machine name
            :param url: Url where to download the challenge
            :param user_flag: Machine user flag
            :param root_flag: Machine root flag
            :param level: Machine complexity
            :param notes: Notes about the machine. Public for everyone
            :param writeup: Summarized solution of the machine. Only avaliable for staff
            """

            if not self.__existLevel(level): raise LevelNotFound("Level do not exist on hackmyvm database. Check if it is spelled correctly")

            data = {
                    "vmname": name,
                    "url": url,
                    "flaguser": user_flag,
                    "flagroot": root_flag,
                    "level": level,
                    "notes": notes,
                    "writeup": writeup
                    }

            # Make post petition with data

            submited = data  # Petition

            return submited

        def status(self, name: str, challenge: bool = False):
            """
            Returns a machine or user challenge status

            :param name: Keyword to get the status
            :param challenge: Bool parameter to specify if you want to get a challenge status
            """

            pass

    def __catchAPIKey(self): 
        """
        Raises an exception if the API key is not set
        """

        if not self.__database.exists("api_key"): raise APIKeyNotFound("Previous configuration needed. API Key must be set.\nTry: python3 main.py config fresh <username> <password> <api_key>\n     python3 main.py config key <api_key>")

    def __catchInvalidMachine(self, machine: str):
        """
        Raises an exception if the machine is not on database
        """

        catched: bool = True

        for data in self.__list():
            if machine in data: catched = False

        if catched: raise MachineNotFound("Machine do not exist on hackmyvm database. Check if it is spelled correctly")

    def __api_post_data(self, data: dict):
        """
        Makes post request to API url wit custom data

        :param data: Petition data in dictionary format
        """

        return post(self.__api_url, data).text

    def __list(self) -> list:
        """
        Returns an array with all avaliable machines
        """

        self.__catchAPIKey()

        data = {
                "k": self.__database.get("api_key"),
                "c": "total"
                }

        return [data.split() for data in self.__api_post_data(data).splitlines()]


    def list(self, level: str = "all", pending: bool = False, finished: bool = False, limit: int = 0, descendant: bool = False):
        """
        Lists all avaliable machines based on level or status

        Level types:
            - All    : Lists all avaliable machines (Default)
            - Easy   : Lists all easy level machines
            - Medium : Lists all medium level machines
            - Hard   : Lists all hard level machines

        Pending and finished parameters can be complemented (Default)

        :param level: Level to be based when creating the list
        :param pending: Shows your pending machines
        :param finished: Shows your finished machines
        :param limit: Shows and slice of machines list from 0 to limit. Default: All machines
        :param descendant: Orders the returned table in bottom-up style (NEW-OLDER). Default: Ascendant (OLDER-NEW)
        """

        level_types = ["all", "easy", "medium", "hard"]
        level = "skip" if pending or finished else level.lower() if level.lower() in level_types else "all"

        machines_table = ColorTable(["Creation Date", "Creation time", "Machine Name", "Level", "Url"], theme=Themes.OCEAN)
        machines = self.__list() if not descendant else reversed(self.__list())

        for machine in machines:
            # Change machine[3] in pending and finished with correct value
            if level in [machine[3].lower(), "all"] or (pending and machine[3].lower() == "pending") or (finished and machine[3].lower() == "finished"):
                machines_table.add_row(machine)

        return machines_table.get_string(fields=["Creation Date", "Machine Name", "Level"], end=machines_table.rowcount if not limit else limit)

    def checkflag(self, flag: str, machine: str, no_verify: bool = False):
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

        if not no_verify and self.__catchInvalidMachine(machine): pass

        # Insert flag into machine

        return inserted

    def download(self, machine: str, no_verify: bool = False):
        """
        Downloads the machine from hackmyvm database or url

        If the 'no_verify' parameter is True, it would not check if the machine is valid or exists on database (not recommended)

        :param machine: Destination machine to download
        :param no_verify: Skips machine existence check
        """

        downloaded: bool = False

        if not no_verify and self.__catchInvalidMachine(machine): pass

        # Download the machine

        return downloaded

    def leaderboard(self, limit: int = 5):
        """
        Returns the firts users of leaderboard based on the limit

        :param limit: Integer to specify how many users to get
        """

        leaderboard = []

        return leaderboard[:limit]


if __name__ == "__main__": Fire(HackMyCLI)
