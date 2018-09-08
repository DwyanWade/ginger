"""
Created on 2018/6/6 0:43

"""
from flask import request, jsonify

from app.libs.redprint import RedPrint
from app.validators.forms import BookSearchForm

__Author__ = '阿强'

api = RedPrint('book')


@api.route('/search')
def search():
    form = BookSearchForm().validate_for_api()
    q = form.q.data
    return q


@api.route('/test', methods=['POST'])
def test():
    test_data = request.json
    return jsonify(test_data)
