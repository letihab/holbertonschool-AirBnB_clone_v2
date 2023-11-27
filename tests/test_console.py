import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.state import State
from unittest.mock import patch
import sys


class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.cmd = HBNBCommand()
        self.patcher = patch('sys.stdout', new_callable=StringIO)
        self.mock_stdout = self.patcher.start()
        self.console = HBNBCommand()
        self.obj = BaseModel()
        self.obj.save()

    def tearDown(self):
        self.patcher.stop()

    def test_do_create_with_valid_class(self):
        class_name = "BaseModel"
        cmd_input = f"create {class_name}\n"
        expected_output = f"{self.cmd.models['BaseModel'].id}\n"
        with patch('builtins.input', side_effect=cmd_input):
            self.cmd.onecmd("create BaseModel")
        self.assertEqual(self.mock_stdout.getvalue(), expected_output)
        self.assertEqual(self.mock_stdout.getvalue(), expected_output)
        self.assertEqual(self.mock_stdout.getvalue(), expected_output)

    def test_do_create_with_valid_class(self):
        class_name = "BaseModel"
        cmd_input = f"create {class_name}\n"
        with patch('builtins.input', side_effect=cmd_input):
            self.cmd.onecmd("create BaseModel")
        actual_output = self.mock_stdout.getvalue().strip()
        self.assertIsNotNone(actual_output)
        self.assertRegex(actual_output, r'^[0-9a-f-]+$')

    def test_do_create_with_no_class_name(self):
        cmd_input = "create\n"
        expected_output = "** class name missing **\n"

        with patch('builtins.input', side_effect=cmd_input):
            self.cmd.onecmd("create")

        self.assertEqual(self.mock_stdout.getvalue(), expected_output)

    def test_show_with_valid_instance(self):
        base_model = BaseModel()
        instance_id = base_model.id
        class_name = "BaseModel"
        cmd_input = f"show {class_name} {instance_id}\n"
        with patch('builtins.input', side_effect=cmd_input):
            self.cmd.onecmd(f"show {class_name} {instance_id}")
        expected_output = str(base_model) + "\n"
        self.assertEqual(self.mock_stdout.getvalue(), expected_output)

    def test_show_with_nonexistent_instance(self):
        cmd_input = "show BaseModel 12345\n"
        with patch('builtins.input', side_effect=cmd_input):
            self.cmd.onecmd("show BaseModel 12345")
        expected_output = "** no instance found **\n"
        self.assertEqual(self.mock_stdout.getvalue(), expected_output)

    def test_destroy_with_valid_instance(self):
        base_model = BaseModel()
        instance_id = base_model.id
        class_name = "BaseModel"
        cmd_input = f"destroy {class_name} {instance_id}\n"
        with patch('builtins.input', side_effect=cmd_input):
            self.cmd.onecmd(f"destroy {class_name} {instance_id}")
        self.assertIsNone(storage.all().get(f"{class_name}.{instance_id}"))

    def test_do_destroy_with_nonexistent_instance(self):
        cmd_input = "destroy BaseModel 12345\n"
        with patch('builtins.input', side_effect=cmd_input):
            self.cmd.onecmd("destroy BaseModel 12345")
        expected_output = "** no instance found **\n"
        self.assertEqual(self.mock_stdout.getvalue(), expected_output)

    def test_all_with_class_argument(self):
        base_model_1 = BaseModel()
        cmd_input = "all BaseModel\n"
        with patch('builtins.input', side_effect=cmd_input):
            self.cmd.onecmd("all BaseModel")
        actual_output = self.mock_stdout.getvalue()
        self.assertIn(str(base_model_1), actual_output)

    def test_all_with_empty_argument(self):
        base_model_1 = BaseModel()
        cmd_input = "all\n"
        with patch('builtins.input', side_effect=cmd_input):
            self.cmd.onecmd("all")
        actual_output = self.mock_stdout.getvalue()
        self.assertIn(str(base_model_1), actual_output)

    def test_do_update_with_nonexistent_instance(self):
        cmd_input = "update BaseModel 12345 name \"UpdatedName\"\n"
        with patch('builtins.input', side_effect=cmd_input):
            self.cmd.onecmd("update BaseModel 12345 name \"UpdatedName\"")
        expected_output = "** no instance found **\n"
        self.assertEqual(self.mock_stdout.getvalue(), expected_output)


class CaptureOutput:
    def __enter__(self):
        self.old_stdout = sys.stdout
        sys.stdout = self.mock_stdout = StringIO()
        return self.mock_stdout

    def __exit__(self, *args):
        sys.stdout = self.old_stdout

    def test_help_command(self):
        cmd_input = "help\n"
        expected_output = "Quitter la commande pour quitter le programme\n"

        with patch('builtins.input',
                   side_effect=cmd_input), CaptureOutput() as mock_stdout:
            self.cmd.onecmd("help")

        self.assertEqual(expected_output, mock_stdout.getvalue())

    def test_create_with_different_model_classes(self):
        class_name = "User"
        cmd_input = f"create {class_name}\n"
        with patch('builtins.input', side_effect=cmd_input):
            self.cmd.onecmd(f"create {class_name}")

    def test_create_with_invalid_model_class(self):
        cmd_input = "create InvalidModel\n"
        expected_output = "** class doesn't exist **\n"
        with patch('builtins.input', side_effect=cmd_input):
            self.cmd.onecmd("create InvalidModel")
        self.assertEqual(self.mock_stdout.getvalue(), expected_output)

    def test_show_with_invalid_instance_id(self):
        class_name = "BaseModel"
        cmd_input = f"show {class_name} InvalidID\n"
        expected_output = "** no instance found **\n"
        with patch('builtins.input', side_effect=cmd_input):
            self.cmd.onecmd(f"show {class_name} InvalidID")
        self.assertEqual(self.mock_stdout.getvalue(), expected_output)

    def test_destroy_with_invalid_instance_id(self):
        class_name = "BaseModel"
        cmd_input = f"destroy {class_name} InvalidID\n"
        expected_output = "** no instance found **\n"
        with patch('builtins.input', side_effect=cmd_input):
            self.cmd.onecmd(f"destroy {class_name} InvalidID")
        self.assertEqual(self.mock_stdout.getvalue(), expected_output)

    def test_update_with_invalid_attribute(self):
        instance_id = self.obj.id
        with patch(
            'builtins.input', side_effect=['update BaseModel', instance_id,
                                           'non_existent_attribute', 'John']):
            self.cmd.onecmd("update BaseModel {} non_existent_attribute 'John'"
                            .format(instance_id))
        expected_output = "** Invalid value for the attribute **\n"
        self.assertEqual(self.mock_stdout.getvalue(), expected_output)

    def test_update_with_valid_date_attribute(self):
        class_name = "BaseModel"
        instance_id = self.obj.id
        cmd_input = (f"update {class_name} {instance_id} "
                     "updated_at '2023-11-03T12:00:00'\n")
        # Ensure that the date update was performed correctly

    def test_update_with_invalid_model_class(self):
        class_name = "InvalidModel"
        instance_id = self.obj.id
        cmd_input = f"update {class_name} {instance_id} attribute 'NewValue'\n"
        expected_output = "** class doesn't exist **\n"
        with patch('builtins.input', side_effect=cmd_input):
            self.cmd.onecmd
            (f"update {class_name} {instance_id} attribute 'NewValue'")
        self.assertEqual(self.mock_stdout.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()
