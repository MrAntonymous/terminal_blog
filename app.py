from database import Database
from menu import Menu

__author__ = 'antonymous'


Database.initialize()

menu = Menu()
menu.run_menu()
