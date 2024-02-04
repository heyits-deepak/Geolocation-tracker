import phonenumbers
from phonenumbers import geocoder, timezone, carrier

phone = "+919588798189"  # Add the country code as prefix to the phone number
ph = phonenumbers.parse(phone, "CH")  # Provide the default region as "CH" (Switzerland) or any other valid country code
country = geocoder.description_for_number(ph, "en")
time_z = timezone.time_zones_for_number(ph)
carr = carrier.name_for_number(ph, "en")

print(country, time_z, carr)
