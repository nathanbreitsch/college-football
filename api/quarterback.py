from flask import Blueprint, Flask, render_template, request, redirect, jsonify, url_for, json
from etl.models import Athlete, Team, Game, Play, Collaboration, Action, Observation

quarterback_api = Blueprint('quarterback', __name__)

"""return quarterback stats table"""
@quarterback_api.route('/api/quarterback_stats', methods = ['GET', 'POST'])
def quarterback_stats():


@quarterback_api.route('/api/quarterback_queries', methods = ['GET'])
def quarterback_queries():
    #eventually, this should be in database.  For now, we hard code
    return jsonify({
        'queries':[
            {
                'name': 'quarters',
                'display': 'Quarters',
                'description': 'Allow for all stats to be viewed by Quarter. Allow for selection of multiple quarters (for example 3rd and 4th quarters, if users want to see stats by half.',
                'options': [
                    {
                        'name': '1st',
                        'value': '1'
                    },
                    {
                        'name': '2nd',
                        'value': '2'
                    },
                    {
                        'name': '3rd',
                        'value': '3'
                    },
                    {
                        'name': '4th',
                        'value': '4'
                    },
                    {
                        'name': 'OT',
                        'value': 'OT'
                    }
                ]
            },
            {
                'name': 'downs',
                'display': 'Downs',
                'description': 'Allow for all stats to be viewed by Down. Allow for multiple downs to be selected in a search, such as 3rd and 4th down.',
                'options': [
                    {
                        'name': '1st',
                        'value': '1'
                    },
                    {
                        'name': '2nd',
                        'value': '2'
                    },
                    {
                        'name': '3rd',
                        'value': '3'
                    },
                    {
                        'name': '4th',
                        'value': '4'
                    }
                ]
            }
        ]
    })
