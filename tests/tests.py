import unittest
import sys
import os

current_script_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(current_script_path, '../src'))

from flask_backend import FlaskBackend

class TestFlaskBackend(unittest.TestCase):

    def setUp(self):
        self.backend = FlaskBackend()

    def test_get_num_messages(self):
        chat_log = ['12345', 'Hi', '12345', 'Hello', '67890', 'Hey']
        self.assertEqual(self.backend.get_num_messages('12345', chat_log), 2)

    def test_remove_messages(self):
        chat_log = ['12345', 'Hi', '12345', 'Hello', '67890', 'Hey']
        updated_chat_log = self.backend.remove_messages('12345', chat_log)
        self.assertEqual(updated_chat_log, ['67890', 'Hey'])
        updated_chat_log = self.backend.remove_messages('67890', updated_chat_log)
        self.assertEqual(updated_chat_log, [])

    def test_get_sender_chat_log(self):
        chat_log = ['12345', 'Hi', '12345', 'Hello', '67890', 'Hey']
        sender_chat_log = self.backend.get_sender_chat_log('12345', chat_log)
        self.assertEqual(sender_chat_log, ['12345', 'Hi', '12345', 'Hello'])
        sender_chat_log = self.backend.get_sender_chat_log('67890', chat_log)
        self.assertEqual(sender_chat_log, ['67890', 'Hey'])
        sender_chat_log = self.backend.get_sender_chat_log('11111', chat_log)
        self.assertEqual(sender_chat_log, [])

if __name__ == '__main__':
    unittest.main()
