#!/usr/bin/env python
# coding: utf-8

from flask import render_template
from flask.views import MethodView

from models.weatherhacks import WeatherHacks

class ForecastView(MethodView):

    def get(self):
        wh = WeatherHacks('230010')
        params = {'forecasts': wh.get,
                  'city': wh.city}

        return render_template('forecast/index.html', params=params)
