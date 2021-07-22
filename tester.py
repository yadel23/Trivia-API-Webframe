from app import user_input, getUrl, getJson, toDict
import unittest, sys

sys.path.append('../Trivia-API-Webframe') # imports python file from parent directory
from app import app #imports flask app object

class BasicTests(unittest.TestCase):

    # executed prior to each test
    def setUp(self):
        self.app = app.test_client()

    ###############
    #### tests ####
    ###############

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
    def home(self):
        response = self.app.get('/home', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def quiz(self):
        response = self.app.get('/quiz', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def info(self):
        response = self.app.get('/info', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def next_question(self):
        response = self.app.get('/next/question', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        



if __name__ == "__main__":
    unittest.main()


    
