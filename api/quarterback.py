from flask import Blueprint, Flask, render_template, request, redirect, jsonify, url_for, json
from etl.models import Athlete, Team, Game, Play, Collaboration, Action, Observation

quarterback_api = Blueprint('quarterback', __name__)

"""return quarterback stats table"""
@quarterback_api.route('/api/quarterback_stats', methods = ['GET', 'POST'])
def quarterback_stats():
    return jsonify({
        # 'quarterbacks': {
        #     'id1': {
        #         'name': 'name',
        #         'position': 'quarterback',
        #         'team': 'Bearcats',
        #         'attempts': 'decimal',
        #         'completion': 'decimal 0-1',
        #         'direction': {
        #             'left': 'decimal 0-1',
        #             'right': 'decimal 0-1',
        #             'mid': 'decimal 0-1'
        #         }
        #         'airYards': 'decimal',
        #         'totalYards': '+/- decimal',
        #         'pressure': 'decimal 0-1',
        #         'pocket': 'decimal 0-1',
        #         'scramble': 'decimal 0-1',
        #         'accuracy': {
        #             'overthrown': 'decimal 0-1',
        #             'underthrown': 'decimal 0-1'
        #         },
        #         'interception': 'decimal 0-1',
        #         'touchdown': 'decimal 0-1',
        #         'throwAway': 'decimal 0-1',
        #         'batteredPass': '???',
        #         'fumble': 'decimal 0-1',
        #         'sack': 'decimal 0-1',
        #         'hit': 'decimal 0-1',
        #         'hurry': 'decimal 0-1'
        #     }
        # }
        # 'id2': {
        #     'name': 'name2',
        #     '...': '...',
        #     'hurry': 'decimal 0-1'
        # }
    })


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
