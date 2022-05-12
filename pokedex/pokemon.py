from flask import (
    Blueprint, redirect, render_template, url_for
)
import requests

bp = Blueprint('pokemon', __name__, url_prefix='/pokemon')

@bp.route('/')
def get_first_pokemon():
    pass

@bp.route('/<int:id>')
def get_pokemon(id):
    pass
