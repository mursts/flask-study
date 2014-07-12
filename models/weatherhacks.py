#!/usr/bin/env python
# coding: utf-8

import requests

class WeatherHacks(object):
    '''Livedoor Weather Web Serviceにリクエストして
       指定の地域の天気予報をjsonで受け取る'''

    _END_POINT = 'http://weather.livedoor.com/forecast/webservice/json/v1?city={}'

    def __init__(self, city_id):
        self._city_id = city_id
        self._forecasts = []
        self._city = None

        self._request()

    def _request(self):
        url = self._END_POINT.format(self._city_id)
        r = requests.get(url).json()
        if 'forecasts' in r:
            self._forecasts =  r['forecasts']

        if 'location' in r and 'city' in r['location']:
            self._city = r['location']['city']

    @property
    def city(self):
        return self._city

    @property
    def get(self):
        return self._forecasts

    @property
    def today(self):
        return self._forecasts[0]

    @property
    def tomorrow(self):
        return self._forecasts[1]

    @property
    def day_after_tomorrow(self):
        return self._forecasts[2]

if __name__ == '__main__':
    forecast = WeatherHacks('230010')
    print(forecast.city)
    import json
    print(json.dumps(forecast.get))
    #print(forecast.tomorrow)
    #print(forecast.day_after_tomorrow)

