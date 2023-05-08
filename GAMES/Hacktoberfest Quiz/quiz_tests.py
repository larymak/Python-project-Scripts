import unittest
from hacktoberfest_quiz import Quiz

class TestQuiz(unittest.TestCase):
    def test_correct_answer_to_question_one(self):
        quiz = Quiz()
        self.assertTrue(quiz.validate_question_one('python'))

    def test_correct_answer_to_question_two(self):
        quiz = Quiz()
        self.assertTrue(quiz.validate_question_two('yes'))
        
    def test_correct_answer_to_question_three(self):
        quiz = Quiz()
        self.assertTrue(quiz.validate_question_three('no'))

    def test_correct_answer_to_question_four(self):
        quiz = Quiz()
        self.assertTrue(quiz.validate_question_four('yes'))

    def test_correct_score(self):
        pass

if __name__ == "__main__":
    unittest.main()