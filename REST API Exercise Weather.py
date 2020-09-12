import requests

try:
    City= str(input('Enter city name: ')) #Masukkan nama kota
    key = 'ef4e6a5e1d236a0bdbc9236faa3ff995' #Token API
    url = f'http://api.openweathermap.org/data/2.5/weather?q={City}&appid={key}' #URL API

    weatherdata = (requests.get(url)).json() #Get data in json format
            
    Lon=(weatherdata['coord']['lon']) #Set LONGITUDE VARIABLE
    Lat=(weatherdata['coord']['lat']) #Set lATITUDE VARIABLE
            
    '''Converting all temperatures in unit Celcius'''    
    Temp_C=round(((weatherdata['main']['temp'])-273.15),2) #actual Temperature
    Feels_like_C=round(((weatherdata['main']['feels_like'])-273.15),2) #feels like Temperature
    Temp_Min_C=round(((weatherdata['main']['temp_min'])-273.15),2) #minimum temperature
    Temp_Max_C=round(((weatherdata['main']['temp_max'])-273.15),2)#maximal temperature

    Windspeed= weatherdata['wind']['speed'] #Get windspeed data 

    print(f'\n\nGood Day !!! Welcome in {City} !!! \n\n{City} is located on {Lon} degrees lon and {Lat} degrees lat\n\nThe temperature in {City} is {Temp_C} degrees Celcius \nHowever, it feels like {Feels_like_C} degrees.\nOn the other hand, we have {Temp_Max_C} degrees as our maximum temperature and {Temp_Min_C} degrees as our minimum.\n')
    print((City),'has Humidity level at ',(weatherdata['main']['temp_min']))
    for i in (weatherdata['weather']):
        print ('\nWeather in ',(City),'today:', (i['description']))
    print(f'Windspeed: {Windspeed} m/s') 
    print('\n\nHave a pleasant Day, my friend !')
    
except:
    print (f'Nothing we found a city named {City}. Please try another one !')