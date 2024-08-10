import csv
import requests
from io import StringIO


csv.field_size_limit(10**7)


eng_dict = []

response = requests.get('https://raw.githubusercontent.com/benjihillard/English-Dictionary-Database/main/english%20Dictionary.csv')

if response.status_code == 200:
    reader = csv.reader(StringIO(response.text), delimiter=',')
    next(reader)

    for row in reader:
        eng_dict.append(row[0].lower())

else:
    print("Failed to fetch english word data")



inputted_list = []  
last_letter = ''

while True:
    
    input_data = str(input("Input English Word: ")).lower()
    
    if input_data == "exit!":
        break

    if last_letter and input_data[0] != last_letter: 
        print(f"The word not start with letter '{input_data[-1]}'")
        continue
    
    if input_data not in eng_dict:
        print(f"{input_data} is not an English word")
        continue

    if input_data in inputted_list:
        print(f"You have chosen '{input_data}' before")
        continue
    
    

    inputted_list.append(input_data)
    last_letter = input_data[-1]
        
print("Inputted Words:", inputted_list)



