import unittest

from questions import questions
from app import *


class TestQuestions(unittest.TestCase):
 
  def test_ask_question(self):
    '''
    Function that finds the question from the dictionary
    '''
    self.assertEqual(ask_question(1), "What is the common name for this tree?")
    self.assertEqual(ask_question(2), "Which japanese plant has leaves like this?")
    #if question index is > len(questions), should return "finished quiz"
    self.assertEqual(ask_question(len(questions)+1), "finished quiz")
    
  def test_get_answer(self):
    '''
    Function that finds the answer from the dictionary
    '''  
    self.assertEqual(get_answer(1), "oak")
    self.assertEqual(get_answer(2), "wasabi")
    
  def test_check_answer(self):
    '''
    Function that takes user answer and compares it to the right answer
    '''
    self.assertTrue(check_answer("oak", 1))
    self.assertFalse(check_answer("pansy", 1))
    
    
class TestQuestionCounter(unittest.TestCase):
    
  def test_question_count(self):
    pass
    
    

if __name__ == '__main__':
    unittest.main()