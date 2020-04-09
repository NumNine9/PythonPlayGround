
countries = ['Zimbabwe','South Africa','Namibia','Tanzania','Botswana','Malawi','Eygpt']
capitals = ['Harare','Pretoria','Windhoek','Dodoma','Gaborone','Lilongwe','Cairo']
#i want a dict {'country':'capital'} for each country,capital in zip(country,capital)
my_dict = {}
for countries,capitals in zip(countries,capitals):
    my_dict[countries]=capitals #countries are the keys in the dictionary
#print(my_dict)

my_dict2 = {countries: capitals for countries, capitals in zip (countries,capitals)}
print(my_dict2)