"""Main file to fetch blueprints"""
from flask import Blueprint
main = Blueprint('main', __name__)
from . import views