import phonenumbers
from phonenumbers import geocoder, carrier, timezone

def phoninfo(phone_number):
    phone_number = phonenumbers.parse(phone_number)

    country = geocoder.description_for_number(phone_number, "en")
    provider = carrier.name_for_number(phone_number, "en")
    time_zone = timezone.time_zones_for_number(phone_number)
    is_valid = phonenumbers.is_valid_number(phone_number)
    phone_format = phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    national_format = phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.NATIONAL)
    phone_type = phonenumbers.number_type(phone_number)
    national_code = phone_number.national_number
    region = geocoder.description_for_valid_number(phone_number, "en")
    latitude, longitude = geocoder.description_for_number(phone_number, "en").split(', ')
    possible_numbers = phonenumbers.build_phone_number_geo_lookup(phone_number)

    return {
        "country": country,
        "provider": provider,
        "time_zone": time_zone,
        "is_valid": is_valid,
        "international_format": phone_format,
        "national_format": national_format,
        "type": phone_type,
        "national_code": national_code,
        "region": region,
        "latitude": latitude,
        "longitude": longitude,
        "possible_numbers": possible_numbers
    }