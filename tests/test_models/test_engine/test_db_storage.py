import unittest
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models import storage


class TestDBStorage(unittest.TestCase):
    def setUp(self):
        """Set up the testing environment"""
        storage.reload()

    def tearDown(self):
        """Tear down the testing environment"""
        storage.close()

    def test_all(self):
        """Test the all method"""
        storage.reload()
        new_user = User()
        new_user.save()
        all_objects = storage.all()
        self.assertIn("User.{}".format(new_user.id), all_objects)

    def test_all_with_class(self):
        """Test the all method with a specific class"""
        storage.reload()
        new_state = State()
        new_state.save()
        all_states = storage.all(State)
        self.assertIn("State.{}".format(new_state.id), all_states)
        all_users = storage.all(User)
        self.assertNotIn("User.", all_users)

    def test_new(self):
        """Test the new method"""
        storage.reload()
        new_city = City()
        storage.new(new_city)
        self.assertIn(new_city, storage._DBStorage__session.new)

    def test_save(self):
        """Test the save method"""
        storage.reload()
        new_review = Review()
        storage.new(new_review)
        storage.save()
        self.assertIn(new_review, storage._DBStorage__session)

    def test_delete(self):
        """Test the delete method"""
        storage.reload()
        new_place = Place()
        storage.new(new_place)
        storage.save()
        storage.delete(new_place)
        self.assertNotIn(new_place, storage._DBStorage__session)

    def test_reload(self):
        """Test the reload method"""
        storage.reload()
        self.assertIsNotNone(storage._DBStorage__engine)
        self.assertIsNotNone(storage._DBStorage__session)

    def test_close(self):
        """Test the close method"""
        storage.reload()
        storage.close()
        self.assertIsNone(storage._DBStorage__session)

    def test_all_multiple_classes(self):
        """Test the all method with instances of multiple classes"""
        storage.reload()

        new_user = User()
        new_user.save()

        new_state = State()
        new_state.save()

        new_place = Place()
        new_place.save()

        all_objects = storage.all()
        self.assertIn("User.{}".format(new_user.id), all_objects)
        self.assertIn("State.{}".format(new_state.id), all_objects)
        self.assertIn("Place.{}".format(new_place.id), all_objects)

    def test_new_multiple_classes(self):
        """Test the new method with instances of multiple classes"""
        storage.reload()

        new_user = User()
        storage.new(new_user)

        new_state = State()
        storage.new(new_state)

        new_place = Place()
        storage.new(new_place)

        self.assertIn(new_user, storage._DBStorage__session.new)
        self.assertIn(new_state, storage._DBStorage__session.new)
        self.assertIn(new_place, storage._DBStorage__session.new)

    def test_delete_multiple_classes(self):
        """Test the delete method with instances of multiple classes"""
        storage.reload()

        new_user = User()
        storage.new(new_user)
        new_user.save()

        new_state = State()
        storage.new(new_state)
        new_state.save()

        new_place = Place()
        storage.new(new_place)
        new_place.save()

        storage.delete(new_user)
        storage.delete(new_state)

        self.assertNotIn(new_user, storage._DBStorage__session)
        self.assertNotIn(new_state, storage._DBStorage__session)
        self.assertIn(new_place, storage._DBStorage__session)

    def test_save_with_modifications(self):
        """Test the save method with object modifications"""
        storage.reload()

        new_review = Review()
        storage.new(new_review)
        storage.save()

        # Modify the object
        new_review.text = "Updated review text"
        storage.save()

        # Reload the session and check if the modification is persisted
        storage.reload()
        updated_review = storage.all(Review)[0]
        self.assertEqual(updated_review.text, "Updated review text")
