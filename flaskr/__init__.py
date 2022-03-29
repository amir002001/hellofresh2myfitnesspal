import os

from flask import Flask
from flask import request

from flaskr.services.meal_service import retrieveMealByMealName


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/myfitnesspal', methods=['POST'])
    def postMacrosByMealName():
        mealName = request.args.get('mealName', type=str)
        retrieveMealByMealName(mealName)
        return f'{mealName}'

    return app
