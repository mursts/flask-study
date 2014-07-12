#!/usr/bin/env python
# coding: utf-8

from flask import Blueprint
from views.index import IndexView
from views.main import MainView
from views.forecast import ForecastView

blueprint = Blueprint('app', __name__, template_folder='templates')

blueprint.add_url_rule('/', view_func=IndexView.as_view('index'))
blueprint.add_url_rule('/main', view_func=MainView.as_view('main'))
blueprint.add_url_rule('/forecast', view_func=ForecastView.as_view('forecast'))

