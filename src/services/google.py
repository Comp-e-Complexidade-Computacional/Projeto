import os, googlemaps, config

from operations import google as operations


class GoogleServices:
    def __init__(self):
        self.api_key = config.GOOGLE_API_KEY
        self.client = googlemaps.Client(key=self.api_key)

    def get_location(self, address: str):
        """
        Retorna a latitude, longitude e o endereço formatado a partir de um endereço.
        """
        return operations.get_location(self.client, address)
    

google = GoogleServices()
