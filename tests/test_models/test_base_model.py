#!/usr/bin/python3
"""
This would test my base_model
"""
import unittest
from models.base_model import BaseModel


class testBaseModel(unittest.TestCase):
    def test_init(self):
        my_model = BaseModel()

        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.updated_at)
        self.assertIsNotNone(my_model.created_at)

    def test_save(self):
        my_model = BaseModel()

        first_update = my_model.updated_at
        new_update = my_model.save

        self.assertNotEqual(first_update, new_update)

    def test_to_dict(self):
        my_model = BaseModel()

        my_model_dic = my_model.to_dict()

        self.assertIsInstance(my_model_dic, dict)
        self.assertEqual(my_model_dic["__class__"], 'BaseModel')
        self.assertEqual(my_model_dic['id'], my_model.id)
        self.assertEqual(my_model_dic['updated_at'], my_model.updated_at.isoformat())
        self.assertEqual(my_model_dic['created_at'], my_model.created_at.isoformat())

    def test_str(self):
        my_model = BaseModel()

        self.assertTrue(str(my_model).startswith('[BaseModel]'))
        self.assertIn(my_model.id, str(my_model))
        self.assertIn(str(my_model.__dict__), str(my_model))

if __name__ =="__main__":
    unittest.main()


