import os
from pathlib import Path

from .date_formatter import DateFormatter


class DirectoryCreator:
    __parent_directory = ''
    created_directory = ''

    def __init__(self, parent_directory: str) -> None:
        self.__parent_directory = parent_directory

    def create_as_today(self) -> str:
        today_month_and_day = DateFormatter().mmdd()
        self.__set_created_directory(today_month_and_day)

        if not self.__directory_exist():
            self.__create()
            return self.created_directory

    def __set_created_directory(self, directory_name: str):
        self.created_directory = f'{self.__parent_directory}\{directory_name}'

    def __directory_exist(self):
        return os.path.exists(self.created_directory)

    def __create(self):
        try: 
            os.makedirs(self.created_directory)
        except OSError as e:
            print(e)
