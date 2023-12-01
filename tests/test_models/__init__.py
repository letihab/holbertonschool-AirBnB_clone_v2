import unittest
from unittest.mock import patch
from os import getenv
from models.engine import db_storage
from models.engine import file_storage


class TestStorageInitialization(unittest.TestCase):
    def setUp(self):
        """Set up the testing environment"""
        pass

    def tearDown(self):
        """Tear down the testing environment"""
        pass

    @patch('models.engine.file_storage.FileStorage', autospec=True)
    @patch('models.engine.db_storage.DBStorage', autospec=True)
    def test_storage_type_file(self, mock_db_storage, mock_file_storage):
        """Test storage initialization for file storage"""
        with patch('os.getenv', return_value='file'):
            from models import storage
            storage.reload()
            mock_file_storage.assert_called_once_with()
            self.assertIsInstance(storage.storage, file_storage.FileStorage)
            self.assertNotIsInstance(storage.storage, db_storage.DBStorage)

    @patch('models.engine.file_storage.FileStorage', autospec=True)
    @patch('models.engine.db_storage.DBStorage', autospec=True)
    def test_storage_type_db(self, mock_db_storage, mock_file_storage):
        """Test storage initialization for database storage"""
        with patch('os.getenv', return_value='db'):
            from models import storage
            storage.reload()
            mock_db_storage.assert_called_once_with()
            self.assertIsInstance(storage.storage, db_storage.DBStorage)
            self.assertNotIsInstance(storage.storage, file_storage.FileStorage)


if __name__ == '__main__':
    unittest.main()
