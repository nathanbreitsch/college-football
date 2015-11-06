from flask import Blueprint, Flask, render_template, request, redirect, jsonify, url_for, json
from etl.models import Athlete, Team, Game, Play, Collaboration, Action, Observation
from playhouse.shortcuts import model_to_dict

quarterback_api = Blueprint('quarterback', __name__)

"""return quarterback stats table"""
@quarterback_api.route('/api/quarterback_stats', methods = ['GET', 'POST'])
def quarterback_stats():
    query = (Observation.select()
                .join(Action)
                .join(Athlete)
                .where(Action.action_type == 'QB')
                .group_by(Action.athlete)
    )
    records = [model_to_dict(record) for record in query]
    return json.dumps(records)
