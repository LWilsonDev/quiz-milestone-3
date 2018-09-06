import unittest, json


from app import *


class TestQuestions(unittest.TestCase):
 
  def test_get_question_data(self):
    '''
    Function that finds the question index from the json file
    '''
    self.assertEqual(get_question_data(0), {"question": "What is the common name for this tree?", "answer": "oak", "image": "../static/images/oak.jpg"})
    self.assertEqual(get_question_data(3), {"question": "Which fruit tree is this?", "answer": "cherry", "image": "../static/images/cherry.jpg"})
    
  def test_get_answer(self): 
    '''
    Function that finds the answer from the dictionary
    '''  
    self.assertEqual(get_answer(0), "oak")
    self.assertEqual(get_answer(1), "wasabi")
    
  def test_get_image(self):
    '''
    Function that finds the images from the dictionary
    '''  
    self.assertEqual(get_image(0), "../static/images/oak.jpg")
    self.assertEqual(get_image(1), "../static/images/wasabi.JPG")  
    
  def test_check_answer(self):
    '''
    Function that takes user answer and compares it to the right answer
    '''
    self.assertTrue(check_answer("oak", 0))
    self.assertFalse(check_answer("pansy", 0))
    self.assertTrue(check_answer("wasabi", 1))
    
    

if __name__ == '__main__':
    unittest.main()