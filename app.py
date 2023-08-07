from flask_jwt_extended import JWTManager
from flask_openapi3 import Info, OpenAPI

from routers import api


def create_app():
    info = Info(title='Empresa API', version='1.0.0')
    app = OpenAPI(__name__, info=info)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'xs1LB9anHiVqTgzHxsVk0mNLUEsD1UtO'
    
    app.register_api(api)
    jwt = JWTManager(app)
    return app


if __name__ == "__main__":
    create_app().run(debug=True)
