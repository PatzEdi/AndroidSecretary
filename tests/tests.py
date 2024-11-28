import unittest
import sys
import os
import json
from unittest.mock import patch

current_script_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(current_script_path, '../src'))

from flask_backend import FlaskBackend

class TestFlaskBackend(unittest.TestCase):
    def setUp(self):
        self.backend = FlaskBackend()
        self.sample_chat_log = [
            "+1234567890: Hello",
            "Assistant: Hi there!",
            "+1234567890: How are you?",
            "Assistant: I'm good!",
            "+9876543210: Test message",
            "Assistant: Hello!"
        ]

    def test_check_number_blacklist(self):
        result = self.backend.check_number(
            sender_number="+1234567890",
            sender_message="Test",
            black_listed_numbers=["+1234567890"],
            allow_list=[],
            phone_contacts=[],
            block_spam=False,
            max_messages_per_hour=5,
            chat_log=[]
        )
        self.assertFalse(result)

    def test_check_number_allowlist(self):
        result = self.backend.check_number(
            sender_number="+1234567890",
            sender_message="Test",
            black_listed_numbers=["+1234567890"],  # Even if blacklisted
            allow_list=["+1234567890"],
            phone_contacts=[],
            block_spam=False,
            max_messages_per_hour=5,
            chat_log=[]
        )
        self.assertTrue(result)

    def test_get_num_messages(self):
        count = self.backend.get_num_messages("+1234567890", self.sample_chat_log)
        self.assertEqual(count, 2)

    def test_remove_messages(self):
        chat_log = self.sample_chat_log.copy()
        updated_log = self.backend.remove_messages("+1234567890", chat_log)
        self.assertEqual(len(updated_log), 2)  # Should only have one sender-assistant pair left

    def test_get_sender_chat_log(self):
        sender_log = self.backend.get_sender_chat_log("+1234567890", self.sample_chat_log)
        self.assertEqual(len(sender_log), 4)  # Should have two sender-assistant pairs

    def test_max_messages_per_hour(self):
        chat_log = ["+1234567890: msg1", "Assistant: resp1"] * 5
        result = self.backend.check_number(
            sender_number="+1234567890",
            sender_message="Test",
            black_listed_numbers=[],
            allow_list=[],
            phone_contacts=[],
            block_spam=False,
            max_messages_per_hour=5,
            chat_log=chat_log
        )
        self.assertFalse(result)
        self.assertIn("+1234567890", self.backend.blocked_numbers)

    def test_block_spam_with_contacts(self):
        result = self.backend.check_number(
            sender_number="+1234567890",
            sender_message="Test",
            black_listed_numbers=[],
            allow_list=[],
            phone_contacts=["+9876543210"],  # Number not in contacts
            block_spam=True,
            max_messages_per_hour=5,
            chat_log=[]
        )
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
