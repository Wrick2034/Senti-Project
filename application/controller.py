from flask import jsonify
from flask_restful import Resource,reqparse
import application.senti as senti


# Controller for sentiment analysis 
class Senti(Resource) : 
    def get(self):
        analysisParser = reqparse.RequestParser()
        analysisParser.add_argument('review', type = str, required = True)
        args = analysisParser.parse_args()
        review = args.get("review", None)
        if review!=None:
            result = senti.AnalyzeSentiment(review)
            return jsonify(result , 200)
        return jsonify({'msg' : "No String passed"}, 406)