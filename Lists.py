["Python","Javascript","Java"]
languages = ["C", "Ruby", "Swift"]
len (languages)
bool (languages)
bool ([])




//Meeting Code
attendees = ["Mark", "Roy", "Kara"]
print ("At this meeting there is", len(attendees), "currenty")

//Check Temp
temp = []
temp.append (98.6)
temp.append (99.4)

er_temps = [102.2, 109.3, 108.6]

temp.extend (er_temps)
temp


//continents example

continents = [
    'Asia',
    'South America',
    'North America',
    'Africa',
    'Europe',
    'Antarctica',
    'Australia',
]
for continent in continents:
    print ('*' , continent)

# Purposed solution for continent.py

continents = [
    'Asia',
    'South America',
    'North America',
    'Africa',
    'Europe',
    'Antarctica',
    'Australia',
]


my_list = []
char = 'A'
for item in continents:
  if item[0] in char:
    my_list.append(item)
  else:
    continue
for continent in my_list:
  print('* ' + continent)

