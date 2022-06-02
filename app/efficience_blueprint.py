from flask import Blueprint, jsonify

from repositories.DataPE1Repository import DataPE1Repository
from repositories.DataPE2Repository import DataPE2Repository
from repositories.DataPE3Repository import DataPE3Repository
from repositories.DataPE5Repository import DataPE5Repository
from repositories.DataPE6Repository import DataPE6Repository

efficience_blueprint = Blueprint('efficience_blueprint', __name__)

repoE1 = DataPE1Repository()
repoE2 = DataPE2Repository()
repoE3 = DataPE3Repository()
repoE5 = DataPE5Repository()
repoE6 = DataPE6Repository()


@efficience_blueprint.route('/')
def all():
    return jsonify([
        [data.get_stats() for data in repoE1.all()],
        [data.get_stats() for data in repoE2.all()],
        [data.get_stats() for data in repoE3.all()],
        [data.get_stats() for data in repoE5.all()],
        [data.get_stats() for data in repoE6.all()],
    ])


@efficience_blueprint.route('/<int:annee>')
def find(annee):
    return jsonify([
        repoE1.find(annee).get_stats(),
        repoE2.find(annee).get_stats(),
        repoE3.find(annee).get_stats(),
        repoE5.find(annee).get_stats(),
        repoE6.find(annee).get_stats(),
    ])

