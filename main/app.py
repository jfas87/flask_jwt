from api import api, app
from db import init_db
from ma import init_ma
from controller.user import ns as ns_user
from controller.auth import ns as ns_auth
import logging


if __name__ == '__main__':
    logging.basicConfig(filename='app.log', level = logging.INFO)
    init_db(app)
    init_ma(app)
    api.add_namespace(ns_auth)

    api.add_namespace(ns_user)
    app.run()