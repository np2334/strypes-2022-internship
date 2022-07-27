import unittest
from Exercise_01_classes import Entity

class TestEntity(unittest.TestCase):
    def setUp(self):
        self.entity = Entity("Pesho", 100)

    def test_entity_get_health(self):
        expected = 100
        actual = self.entity.get_health()

        self.assertEqual(actual, expected)

    def test_entity_take_damage(self):
        self.entity.take_damage(50)
        expected = 50
        actual = self.entity.get_health()

        self.assertEqual(actual, expected)

    def test_entity_take_negative_damage(self):
        self.entity.take_damage(-12)
        expected = 100
        actual = self.entity.get_health()

        self.assertEqual(actual, expected)

    def test_entity_heal(self):
        self.entity.take_damage(50)
        self.entity.take_healing(20)
        expected = 70
        actual = self.entity.get_health()

        self.assertEqual(actual, expected)

    def test_entity_negative_heal(self):
        expected = False
        actual = self.entity.take_healing(-50)

        self.assertEqual(actual, expected)

    def test_entity_is_alive(self):
        self.entity.take_damage(100)
        expected = False
        actual = self.entity.is_alive()

        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()