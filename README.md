# <p style="text-align: center;"><span style="color:blue">*AirBnB clone - The console*</span></p>

### TABLE OF CONTENTS
- [DESCRIPTION](#description)
- [WHERE IS THE AIRBNB CLONE ?](#Where-is-the-Airbnb-clone)
- [REQUIREMENTS](#requirements)
- [COMPILATION CMD](#compilation-cmd)
- [EXAMPLES](#examples)
- [AUTHORS](#authors)


### DESCRIPTION

The Airbnb "The Console" project consists of creating a Python program that serves as a command-line interface for managing various entities related to Airbnb.

The command line interface is entirely created to manage and query entities related to Airbnb, including users, states, cities, facilities, locations and reviews.

Created on week : Monday 30 october to Friday 3 November 2023.

### WHERE IS THE AIRBNB CLONE ?

<a href="https://zupimages.net/viewer.php?id=23/44/duly.jpg"><img src="https://zupimages.net/up/23/44/duly.jpg" alt="" /></a>

### REQUIREMENTS

Python Scripts
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the pycodestyle (version 2.7.*)
All your files must be executable
The length of your files will be tested using wc
All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

### COMPILATION CMD

tests/test_models/test_base_model.py (for code)
or
python3 -m unittest tests/test_models/test_base_model.py (for unittest)

### EXAMPLES

_Interactive :_

./console.py (for console)
or
python3 -m unittest tests/test_models/test_base_model.py (for unittest)

_Non-interactive :_

echo "help" | ./console.py (for console)
or
echo "python3 -m unittest discover tests" | bash (for unittest)

_Unittest :_

class TestBaseModel(unittest.TestCase):
    def test_instance_creation(self):
        model = BaseModel()
        self.assertTrue(isinstance(model, BaseModel))
        self.assertTrue(hasattr(model, 'id'))
        self.assertTrue(hasattr(model, 'created_at'))
        self.assertTrue(hasattr(model, 'updated_at'))

    def test_instance_with_args(self):
        data = {
            'id': 'test_id',
            'created_at': '2023-11-01T12:00:00',
            'updated_at': '2023-11-01T12:30:00'
        }
        model = BaseModel(**data)
        self.assertEqual(model.id, 'test_id')
        self.assertEqual(model.created_at, datetime.fromisoformat
                         ('2023-11-01T12:00:00'))
        self.assertEqual(model.updated_at, datetime.fromisoformat
                         ('2023-11-01T12:30:00'))

    def test_str_representation(self):
        model = BaseModel()
        self.assertIn('BaseModel', str(model))
        self.assertIn(model.id, str(model))

...

### AUTHORS
Solomon William
&
Nadège Tettelin
