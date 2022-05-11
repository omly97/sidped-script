from flask import Flask, jsonify
from flask_cors import CORS

from google.auth.exceptions import TransportError
from gspread.exceptions import GSpreadException
from Repositories.EfficienceRepository import EfficienceRepository

from axefinance.F1Service import F1Service
from axefinance.F2Service import F2Service
from axefinance.F4Service import F4Service

from axehumain.H2AService import H2AService
from axehumain.H2BService import H2BService
from axehumain.H2CService import H2CService
from axehumain.H3AService import H3AService
from axehumain.H3BService import H3BService
from axehumain.H3CService import H3CService
from axehumain.H4Service import H4Service


# create app
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# config cors
cors = CORS(app, resources={r"/*": {"origins": "*",}})


# instance services humain
HUMAN_SERVICES = {
    'h2a': H2AService(),
    'h2b': H2BService(),
    'h2c': H2CService(),
    'h3a': H3AService(),
    'h3b': H3BService(),
    'h3c': H3CService(),
    'h4': H4Service(),
}

# instance services finances
FINANCE_SERVICES = {
    'f1': F1Service(),
    'f2': F2Service(),
    'f4': F4Service(),
}



@app.route('/axe-humain')
def axe_humain():
    data = [{ 'key': key, 'metadata': service.get_metadata(), 'data': service.get_data_calculated() } for key,service in HUMAN_SERVICES.items()]
    try:
        return jsonify(data)

    except GSpreadException as e:
        return jsonify({ 'success': False, 'message': str(e) })

    except TransportError as e:
        return jsonify({ 'success': False, 'message': str(e) })

    except:
        return jsonify({ 'code': 500, 'success': False, 'message': "Erreur interne du serveur" })


@app.route('/axe-humain/<string:key>', methods = ['GET'])
def axe_humain_key(key):
    service = HUMAN_SERVICES[key]
    try:
        return jsonify({ 'key': key, 'metadata': service.get_metadata(), 'data': service.get_data_calculated() })

    except GSpreadException as e:
        return jsonify({ 'success': False, 'message': str(e) })

    except TransportError as e:
        return jsonify({ 'success': False, 'message': str(e) })

    except:
        return jsonify({ 'code': 500, 'success': False, 'message': "Erreur interne du serveur" })



@app.route('/axe-finance', methods = ['GET'])
def axe_finance():
    data = [{ 'key': key, 'metadata': service.get_metadata(), 'data': service.get_data_calculated() } for key,service in FINANCE_SERVICES.items()]
    try:
        return jsonify(data)

    except GSpreadException as e:
        return jsonify({ 'success': False, 'message': str(e) })

    except TransportError as e:
        return jsonify({ 'success': False, 'message': str(e) })

    except:
        return jsonify({ 'code': 500, 'success': False, 'message': "Erreur interne du serveur" })


@app.route('/axe-finance/<string:key>', methods = ['GET'])
def axe_finance_key(key):
    service = FINANCE_SERVICES[key]
    try:
        return jsonify({ 'key': key, 'metadata': service.get_metadata(), 'data': service.get_data_calculated() })

    except GSpreadException as e:
        return jsonify({ 'success': False, 'message': str(e) })

    except TransportError as e:
        return jsonify({ 'success': False, 'message': str(e) })

    except:
        return jsonify({ 'code': 500, 'success': False, 'message': "Erreur interne du serveur" })



@app.route('/efficience')
def efficience():
    repo = EfficienceRepository()
    data = repo.select_all__efficience()

    new_data = []
    for item in data:
        new_data.append({
            'annee': item[1],
            'PE1': (item[2] * 100) / (item[2] + item[3]),
            'PE2': ((item[4] + item[5]) * 100) / item[6],
            'PE3': (item[7] * item[8] * 100) / (item[9] + 10),
        })

    return jsonify(new_data)



@app.route('/')
def index():
    return "It's work"


if __name__ == "__main__":
        app.run()
