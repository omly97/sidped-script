from flask import Flask, jsonify
from flask_cors import CORS

from app.efficience_blueprint import efficience_blueprint
from app.finance_blueprint import finance_blueprint
from app.humain_blueprint import humain_blueprint



# create app
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# config cors
cors = CORS(app, resources={r"/*": {"origins": "*",}})

# blueprints
app.register_blueprint(efficience_blueprint, url_prefix='/efficience')
app.register_blueprint(finance_blueprint, url_prefix='/finance')
app.register_blueprint(humain_blueprint, url_prefix='/humain')



@app.route('/')
def index():
    return "It's work"


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
