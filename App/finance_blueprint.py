from flask import Blueprint, jsonify

from Repositories.DataF1Repository import DataF1Repository
from Repositories.DataF2Repository import DataF2Repository
from Repositories.DataF3Repository import DataF3Repository

finance_blueprint = Blueprint('finance_blueprint', __name__)

repoF1 = DataF1Repository()
repoF2 = DataF2Repository()
repoF3 = DataF3Repository()


@finance_blueprint.route('/')
def all():
    return jsonify([
        [data.get_stats() for data in repoF1.all()],
        [data.get_stats() for data in repoF2.all()],
        [data.get_stats() for data in repoF3.all()],
    ])


@finance_blueprint.route('/<int:annee>')
def find(annee):
    return jsonify([
        repoF1.find(annee).get_stats(),
        repoF2.find(annee).get_stats(),
        repoF3.find(annee).get_stats(),
    ])

