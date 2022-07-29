import unittest
from Characters import Character

class TestCharacter(unittest.TestCase):
    def setUp(self):
        self.character = Character(100, 0.0)

    def test_entity_get_health(self):
        expected = 100
        actual = self.character.get_health()

        self.assertEqual(actual, expected)

    def test_entity_take_damage(self):
        self.character.take_damage(50)
        expected = 50
        actual = self.character.get_health()

        self.assertEqual(actual, expected)

    def test_entity_take_negative_damage(self):
        self.character.take_damage(-12)
        expected = 100
        actual = self.character.get_health()

        self.assertEqual(actual, expected)

    def test_entity_heal(self):
        self.character.take_damage(50)
        self.character.take_healing(20)
        expected = 70
        actual = self.character.get_health()

        self.assertEqual(actual, expected)

    def test_entity_negative_heal(self):
        expected = False
        actual = self.character.take_healing(-50)

        self.assertEqual(actual, expected)

    def test_entity_is_alive(self):
        self.character.take_damage(100)
        expected = False
        actual = self.character.is_alive()

        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()