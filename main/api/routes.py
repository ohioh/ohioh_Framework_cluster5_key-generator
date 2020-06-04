from ..api import api
from ..views import *

api.add_resource(StatusView, '/status')
api.add_resource(UserView, '/users')
