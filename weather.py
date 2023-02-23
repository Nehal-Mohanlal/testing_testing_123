import requests 

def get_weather():
    city = 'London' 

    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

    api_key = '3bf83154e21f378a7dc8a50abd15ddbe'

    URL = BASE_URL + "q=" + city + "&appid=" + api_key

    print(URL)
    res =requests.get(URL)



    data = res.json() 

    temp = data['main']['temp'] 
    
    temp = temp -273.15 
    return round(temp) 




def display_weather():
    
    weather = get_weather() 
    
    #print("the weather in London is : " + str(weather) + " °C")

    print("the weather from: mock_get_weather: " + str(weather) + " °C") 
    
    return weather 

#display_weather() 

def issue_warning():
   weather =  get_weather()
   print('weather is: ' + str(weather))
      
   if weather < 30 and weather > 6:
       print("weather conditions normal") 
       print("_______________________________________")
   elif weather > 30:
       print("weather warning issued: High temperatures detected; wear some sunscreen! ") 
       print("_______________________________________")
   elif weather < 6: 
       print("Weather warning issued: Low temperatures detected; bring a jacket!") 
       print("_______________________________________")
   else:
       print("error in getting temperature")

   return weather

#issue_warning()