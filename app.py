from flask import Flask
from routes.auth_routes import auth_routes
from routes.public_routes import public_routes
from utils.log import configure_logging

app = Flask(__name__)

# Configuration des logs colorés
configure_logging()

# Enregistrement des blueprints des routes
app.register_blueprint(auth_routes)
app.register_blueprint(public_routes)

if __name__ == "__main__":
    print("\033[1;32mSplash Screen: Application Flask démarrée !\033[0m")
    app.run(debug=True)

