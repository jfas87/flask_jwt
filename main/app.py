
from api import api, app
from db import init_db
from ma import init_ma
from controller.user import ns
import logging


if __name__ == '__main__':
    logging.basicConfig(filename='app.log', level = logging.INFO)
    init_db(app)
    init_ma(app)
    api.add_namespace(ns)
    app.run()