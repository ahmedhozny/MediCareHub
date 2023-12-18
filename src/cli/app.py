"""The main app."""

import cmd
import re

from src.models.doctor import Doctor
from src.models.nurse import Nurse
from src.models.patient import Patient
from src.models.room import Room
from src.models.room_type import RoomType
from src.models.ward_boy import WardBoy

import src.controllers.doctor as cdoctor
import src.controllers.nurse as cnurse
import src.controllers.patient as cpatient
import src.controllers.room as croom
import src.controllers.room_type as croom_type
import src.controllers.ward_boy as cward_boy


class App(cmd.Cmd):
    """Defines command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(MediCareHub) "

    __all_classes = {
        "Doctor",
        "Nurse",
        "Patient",
        "Room",
        "Room_type",
        "ward_boy"
    }

    def do_exit(self, args):
        """Exits the program."""
        return True

    def do_EOF(self, args):
        """Exits on EOF."""
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, args):
        """
        Usage: create <class>
        Create a new class instance and print its id.
        """
        args = args.split()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in App.__all_classes:
            print("** class doesn't exist **")
        else:
            obj = eval(args[0])(args[1:])
            eval("c{}".format(args[0]))()
