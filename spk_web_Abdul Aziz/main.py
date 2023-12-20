from http import HTTPStatus

from flask import Flask, request
from flask_restful import Resource, Api 

from models import Motor

app = Flask(__name__)
api = Api(app)

class Recommendation(Resource):

    def post(self):
        criteria = request.get_json()
        validCriteria = ['nama','harga','cc','kapasitas bensin','daya maksimum','torsi maksimum']
        motor = Motor()

        if not criteria:
            return 'criteria is empty', HTTPStatus.BAD_REQUEST.value

        if not all([v in validCriteria for v in criteria]):
            return 'criteria is not found', HTTPStatus.UNPROCESSABLE_ENTITY.value

        ranked_results = motor.get_recs(criteria)

        return {
            'WP ': "WeightedProduct",
            'alternatif': ranked_results
        }, HTTPStatus.OK.value


api.add_resource(Recommendation, '/recommendation')

if __name__ == '__main__':
    app.run(port='5005', debug=True)
