#import Libraries 
import unittest 

from unittest.mock import patch 

# get component we want to test, in this case it is a function 
from weather import display_weather

#define class for testing 
class testWeather(unittest.TestCase):
    #create a mock of dependancy 
    @patch('weather.get_weather')
    
    #define test case
    def test_display_weather(self, mock_get_weather):
        # set a return value 
        mock_get_weather.return_value = 124
        #test statement 
        self.assertEqual(display_weather(), 124) 
         
if __name__ == '__main__':
    unittest.main()