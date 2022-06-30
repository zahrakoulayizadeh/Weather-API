import requests
import PySimpleGUI as sg
import os


sg.theme("BluePurple")
layout = [  [sg.Text("Welcome to Current weather App!",font =("Agilo Handwriting",14,'bold'))],
            [sg.Text("Enter the city name: ")], [sg.In(size=(30, 5), enable_events=True)],
            [sg.Button('search',size =(5 , 1)) ,sg.Button('Exit',size =(5 , 1))]
                ]

window = sg.Window('Welcome', layout , margins =[150,75],font=("B babak", 14, 'bold'))

user_api = os.environ['Current_weather_data']
while(True):
    event, values = window.read()
    if event == 'search':
        location = values[0]

        full_api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + user_api

        api_link = requests.get(full_api_link)
        api_data = api_link.json()

        if api_data['cod'] == '404':
            # print("Invalid coty. Please check your city name!")
            sg.popup("Invalid city. Please check your city name!" + '\n' + '\n',font=("B babak", 14, 'bold'))
        else:
            temp_city = (api_data['main']['temp']) -273.15
            # print(str(round(temp_city)) + " centigrade" )
            sg.popup(str(round(temp_city)) + " centigrade"+ '\n' + '\n',font=("B babak", 14, 'bold'))

    elif event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()