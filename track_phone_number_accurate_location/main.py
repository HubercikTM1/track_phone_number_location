import phonenumbers
import opencage
import folium
from phonenum import number

from phonenumbers import geocoder, carrier

pnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pnumber, 'en')
print(location)

serv_pro = phonenumbers.parse(number)
print(carrier.name_for_number(serv_pro, 'en'))

from opencage.geocoder import OpenCageGeocode

apikey = '5747306f3cd449e9b96f32f8f7056b44'

geocoder = OpenCageGeocode(apikey)
query = str(location)
results = geocoder.geocode(query)
#print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat, lng)

mymap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(mymap)

mymap.save('mylocation.html')
