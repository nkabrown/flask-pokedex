from flask import (
    Blueprint, redirect, render_template, url_for
)
import requests

POKE_API = 'https://pokeapi.co/api/v2'

bp = Blueprint('pokemon', __name__, url_prefix='/pokemon')

@bp.route('/<int:id>')
def get_pokemon(id):
    resp = requests.get(f'{POKE_API}/pokemon/{id}/')
    data = resp.json()
    return render_template('pokemon/index.html', pokemon=data)
