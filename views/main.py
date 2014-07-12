#!/usr/bin/env python
# coding: utf-8

from flask import render_template
from flask.views import MethodView

from datetime import datetime

class MainView(MethodView):

    def get(self):
        params = {'now': datetime.now() }
        return render_template('main/index.html', params=params)
