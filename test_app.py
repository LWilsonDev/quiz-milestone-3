import unittest

from questions import questions
from app import *


class TestQuestions(unittest.TestCase):
  '''
  Function that finds the question from the dictionary
  '''
  def test_ask_question(self):
    self.assertEqual(ask_question(1), "What is the common name for this tree?")
    self.assertEqual(ask_question(2), "Which japanese plant has leaves like this?")
    #if question index is > len(questions), should return "finished quiz"
    self.assertEqual(ask_question(len(questions)+1), "finished quiz")
    
  def test_get_answer(self):
    self.assertEqual(get_answer(1), "oak")
    

if __name__ == '__main__':
    unittest.main()