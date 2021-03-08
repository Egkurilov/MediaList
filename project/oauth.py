
import requests
import json
from flask import Blueprint
from .models import User

oauth = Blueprint('oauth', __name__)

def auth_with_ulogin(token):
    url = "http://ulogin.ru/token.php?token={token}".format(token=token)
    try:
        r = requests.get(url)
        r.raise_for_status()
    except (HTTPError) as e:  
        print(e)
        return "404"

    return json.loads(r.text.encode('utf-8'))


def check_valiable(client):
	pass
	#user = User.query.filter(User.name == client).first()
