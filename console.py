#!/usr/bin/python3
"""Contains the entry point of the command interpreter"""

import cmd
import shlex
from datetime import datetime
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    class_dict = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review,
    }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """End of file command to exit the program"""
        return True

    def emptyline(self):
        """Skip empty line"""
        pass

    def do_create(self, arg):
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.class_dict:
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance attributes missing **")
            return

        args = args[1:]
        attributes = {}
        for argument in args:
            parts = argument.split('=')
            if len(parts) != 2:
                continue
            key, val = parts
            val = val.replace('_', ' ').replace('\\"', '"')
            if val[0] == '"' and val[-1] == '"':
                val = val[1:-1]
            else:
                try:
                    if '.' in val:
                        val = float(val)
                    else:
                        val = int(val)
                except ValueError:
                    continue
            attributes[key] = val

        new_instance = self.class_dict[class_name](**attributes)
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        args_list = shlex.split(arg)
        if len(args_list) == 0:
            print("** class name missing **")
        else:
            class_name = args_list[0]
            if class_name not in HBNBCommand.class_dict:
                print("** class doesn't exist **")
            elif len(args_list) < 2:
                print("** instance id missing **")
            else:
                instance_id = args_list[1]
                key = "{}.{}".format(class_name, instance_id)
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    instance = storage.all()[key]
                    print(instance)

    def do_destroy(self, arg):
        args_list = shlex.split(arg)
        if len(args_list) == 0:
            print("** class name missing **")
        else:
            class_name = args_list[0]
            if class_name not in HBNBCommand.class_dict:
                print("** class doesn't exist **")
            elif len(args_list) < 2:
                print("** instance id missing **")
            else:
                instance_id = args_list[1]
                key = "{}.{}".format(class_name, instance_id)
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, arg):
        args_list = shlex.split(arg)
        obj_list = []

        if len(args_list) == 0:
            for obj in storage.all().values():
                obj_list.append(str(obj))
            print(obj_list)
        else:
            class_name = args_list[0]
            if class_name in HBNBCommand.class_dict:
                for obj in storage.all().values():
                    if type(obj).__name__ == class_name:
                        obj_list.append(str(obj))
                print(obj_list)
            else:
                print("** class doesn't exist **")

    def do_update(self, arg):
        args_list = shlex.split(arg)
        if len(args_list) == 0:
            print("** class name missing **")
            return
        class_name = args_list[0]
        if class_name not in HBNBCommand.class_dict:
            print("** class doesn't exist **")
            return
        elif len(args_list) < 2:
            print("** instance id missing **")
            return
        instance_id = args_list[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in storage.all():
            print("** no instance found **")
            return
        instance = storage.all()[key]
        if len(args_list) < 3:
            print("** attribute name missing **")
            return
        attribute_name = args_list[2]
        if len(args_list) < 4:
            print("** value missing **")
            return
        value = args_list[3]
        try:
            value = eval(value)
        except (NameError, SyntaxError):
            pass
        setattr(instance, attribute_name, value)
        instance.updated_at = datetime.now()
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
