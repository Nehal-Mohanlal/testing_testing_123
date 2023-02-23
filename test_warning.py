#import Libraries 
import unittest 

from unittest.mock import Mock 

import weather
from weather import issue_warning

class test_warning(unittest.TestCase):
    weather.get_weather = Mock() 
     
    def test_levels_normal(self):
       weather.get_weather.return_value = 15    

       self.assertTrue(weather.issue_warning()) 
    
    def test_weather_high(self): 
       weather.get_weather.return_value = 42 
       self.assertTrue(weather.issue_warning()) 
    
    def test_weather_low(self): 
        weather.get_weather.return_value = 2
        self.assertTrue(weather.issue_warning()) 
    
        
        
if __name__ == '__main__':
    unittest.main()