#!/bin/python3

import fire
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
        self.submit = self.__submit(self.__database)

    class __config:
        def __init__(self, database: LoadPickleDB):
            """
            Basic configuration manager

            :param database: PickleDB object for handling the configuration file
            """

            self.__database = database

        def fresh(self, username: str, password: str, clean: bool = False):
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

        def password(self, password: str):
            """
            Updates configuration password

            :param password: Password to be saved
            """

            self.add("password", password)

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

            if self.__database.exists(key):
                self.__database.pop(key)
                self.__database.save.as_json()

            else: raise Exception("Invalid keyword. It do not exists on configuration file")

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

            if not self.__existCategory(category): raise Exception("Invalid challenge category. It do not exist on categories list")

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

            if not self.__existLevel(level): raise Exception("Invalid machine level. It do not exist on levels list")

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

    def list(self, level: str = "all"):
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
        level = level if level.lower() in level_types else "all"

        machines = []

        # List all machines

        return machines

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

        if not no_verify and machine not in self.list():
            raise Exception("Invalid machine. It do not exist on hackmyvm database")

        # Insert flag into machine

        return inserted

    def download(self, machine: str, no_verify: bool = False):
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

    def leaderboard(self, limit: int = 5):
        """
        Returns the firts users of leaderboard based on the limit

        :param limit: Integer to specify how many users to get
        """

        leaderboard = []

        return leaderboard[:limit]


if __name__ == "__main__": fire.Fire(HackMyCLI)
