from flask import Blueprint, Flask, render_template, request, redirect, jsonify, url_for, json
from etl.models import Athlete, Team, Game, Play, Collaboration, Action, Observation

quarterback_api = Blueprint('quarterback', __name__)

"""return quarterback stats table"""
@quarterback_api.route('/api/quarterback_stats', methods = ['GET', 'POST'])
def quarterback_stats():
    return jsonify({"fuck": "yes"})


