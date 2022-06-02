from flask import Blueprint, jsonify

from repositories.DataH1Repository import DataH1Repository
from repositories.DataH2ARepository import DataH2ARepository
from repositories.DataH2BRepository import DataH2BRepository
from repositories.DataH3Repository import DataH3Repository
from repositories.DataH4Repository import DataH4Repository

humain_blueprint = Blueprint('humain_blueprint', __name__)

repoE1 = DataH1Repository()
repoE2 = DataH2ARepository()
repoE3 = DataH2BRepository()
repoE5 = DataH3Repository()
repoE6 = DataH4Repository()


@humain_blueprint.route('/')
def all():
    return jsonify([
        [data.get_stats() for data in repoE1.all()],
        [data.get_stats() for data in repoE2.all()],
        [data.get_stats() for data in repoE3.all()],
        [data.get_stats() for data in repoE5.all()],
        [data.get_stats() for data in repoE6.all()],
    ])


@humain_blueprint.route('/<int:annee>')
def find(annee):
    return jsonify([
        repoE1.find(annee).get_stats(),
        repoE2.find(annee).get_stats(),
        repoE3.find(annee).get_stats(),
        repoE5.find(annee).get_stats(),
        repoE6.find(annee).get_stats(),
    ])

