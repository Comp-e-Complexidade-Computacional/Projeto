import googlemaps

def get_location(client, address: str):
    result = client.geocode(address)

    if not result:
        raise ValueError(f"Address '{address}' not found.")

    location = result[0]['geometry']['location']

    return {
        "latitude": location['lat'],
        "longitude": location['lng'],
        "formatted_address": result[0]['formatted_address']
    }
    