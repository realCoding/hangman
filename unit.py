__author__ = 'leedongwoo'

import unittest
import Hangman

class checkCorrectAnswerTestCase(unittest.TestCase):

  def test_checkCorrectAnswer(self):
    answer=Hangman.checkCorrectAnswer('tac','cat')
    self.assertTrue(answer)

  def test_checkWrongAnswer(self):
    answer=Hangman.checkCorrectAnswer('zebrio','zebra')
    self.assertTrue(answer)

if __name__=="__main__":
  unittest.main()
