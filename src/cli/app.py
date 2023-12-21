"""The main app."""

import cmd
import re

from src.models.bill import Bill
from src.models.doctor import Doctor
from src.models.medical_record import MedicalRecord
from src.models.nurse import Nurse
from src.models.patient import Patient
from src.models.room import Room
from src.models.room_type import RoomType
from src.models.ward_boy import WardBoy

from src.controllers.controller import *


class App(cmd.Cmd):
    """Defines command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(MediCareHub) "

    __all_classes = {
        "Bill",
        "Doctor",
        "MedicalRecord",
        "Nurse",
        "Patient",
        "Room",
        "RoomType",
        "WardBoy"
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
        elif args[0] not in self.__all_classes:
            print("** class doesn't exist **")
        else:
            attributes = eval(args[0]).relation_attribute_name()
            del attributes["ID"]
            data = [None]
            if len(attributes) != 0:
                print(f"Please input attributes: ")
                for attribute in attributes:
                    data.append(input(attribute + ": "))
            obj = eval(args[0])(*data)
            try:
                res = new(obj)
                print(f"{args[0]} (ID: {res}) has been created.")
            except Exception as e:
                print("An error occurred while inserting data into the database.")
                print(e)

    def do_delete(self, args):
        """
        Usage: delete <class>
        Deletes an instance based on the class name and id.
        """
        args = args.split()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in self.__all_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif get_by_id(eval(args[0]), args[1]) is None:
            print(f"{args[0]} with Id ({args[1]}) was not found. Please recheck the ID")
        else:
            model = get_by_id(eval(args[0]), args[1])
            try:
                delete(model)
                print("Deleted successfully")
            except Exception as e:
                print("An error occurred while deleting")
                print(e)

    def do_update(self, args):
        """
        Usage: update <class> <id> <attributes_dict>
        Updates an instance based on the class name and id
        by adding or updating attribute.
        """
        args = args.split()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in self.__all_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** id missing **")
        elif get_by_id(eval(args[0]), args[1]) is None:
            print(f"{args[0]} with Id ({args[1]}) was not found. Please recheck the ID")
        else:
            model = get_by_id(eval(args[0]), args[1])
            kwargs = {}
            for key, val in model.relation_attribute_name().items():
                res = input(f"{key}[{getattr(model, val)}]: ")
                if len(res) != 0:
                    kwargs[key] = res
            model.update(**kwargs)
            try:
                update(model)
                print("Updated successfully")
            except Exception as e:
                print("An error occurred while updating")
                print(e)

    def do_list(self, args):
        """
        Usage: list <classname>
        Lists models according to the given arguments
        """
        args = args.split()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in self.__all_classes:
            print("** class doesn't exist **")
        else:
            instances = list_model(eval(args[0]))
            for instance in instances:
                print(instance)

    def do_record(self, args):
        """
        Usage: update <class> <id> <attributes_dict>
        Updates an instance based on the class name and id
        by adding or updating attribute.
        """
        RecordInterface().cmdloop()


class RecordInterface(cmd.Cmd):
    """Defines record interface.

    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "Record > "

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
        Usage: create <patient_id>
        Creates a new record for a patient
        """
        args = args.split()
        if len(args) < 1:
            print("** patient id missing **")
            return False
        patient = get_by_id(Patient, args[0])
        if patient is None:
            print("** patient id doesn't exist **")
        else:
            attributes = MedicalRecord.relation_attribute_name()
            del attributes["ID"]
            data = [None, patient.id]
            print(f"Please input attributes: ")
            keys = list(attributes.keys())[1:]
            for i in range(3):
                data.append(input(keys[i] + ": "))
            obj = MedicalRecord(*data)
            try:
                res = new(obj)
                print(f"Record (ID: {res}) for patient({args[0]}) has been created.")
            except Exception as e:
                print("An error occurred while updating")
                print(e)

    def do_disease(self, args):
        """
        Usage: disease <patient_id> <record_id: optional>
        Sets a disease for selected record of a patient
        """
        args = args.split()
        if len(args) < 1:
            print("** patient id missing **")
        elif len(args) < 2:
            print("** record id missing **")
        elif not get_by_id(Patient, args[0]):
            print("** patient doesn't exist **")
        else:
            record = get_medical_record(args[0], args[1])
            if record is None:
                print("** record doesn't exist **")
                return False
            print(f"Please input attributes: ")
            keys = ["DiseaseDescription", "Priority"]
            data = []
            for key in keys:
                data.append(input(key + f"[{record.__dict__()[key]}]: "))
            record.set_disease(*data)
            try:
                update_medical_record(record)
                print("Updated successfully")
            except Exception as e:
                print("An error occurred while updating")
                print(e)

    def do_treatment(self, args):
        """
        Usage: treatment <patient_id> <record_id: optional>
        Sets a treatment for selected record of a patient
        """
        args = args.split()
        if len(args) < 1:
            print("** patient id missing **")
        elif len(args) < 2:
            print("** record id missing **")
        elif not get_by_id(Patient, args[0]):
            print("** patient doesn't exist **")
        else:
            record = get_medical_record(args[0], args[1])
            if record is None:
                print("** record doesn't exist **")
                return False
            print(f"Please input attributes: ")
            keys = ["TreatmentDescription", "TreatmentCost"]
            data = []
            for key in keys:
                data.append(input(key + f"[{record.__dict__()[key]}]: "))
            record.set_treatment(*data)
            try:
                update_medical_record(record)
                print("Updated successfully")
            except Exception as e:
                print("An error occurred while updating")
                print(e)

    def do_discharge(self, args):
        """
        Usage: discharge <patient_id> <record_id: optional>
        Sets the discharge date for selected record of a patient
        """
        args = args.split()
        if len(args) < 1:
            print("** patient id missing **")
        elif len(args) < 2:
            print("** record id missing **")
        elif not get_by_id(Patient, args[0]):
            print("** patient doesn't exist **")
        else:
            record = get_medical_record(args[0], args[1])
            if record is None:
                print("** record doesn't exist **")
                return False
            print(f"Please input attributes: ")
            key = "DischargeDate"
            data = input(key + f"[{record.__dict__()[key]}]: ")
            record.set_discharge(*data)
            try:
                update_medical_record(record)
                print("Updated successfully")
            except Exception as e:
                print("An error occurred while updating")
                print(e)


if __name__ == "__main__":
    App().cmdloop()
