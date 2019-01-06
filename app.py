import falcon
import json
from algorithm import WordMatching
from constants import MIN_CHARS


# global constants
app = falcon.API()
wm = WordMatching("word_search.tsv")


class FuzzyMatch:
    def on_get(self, req, res):
        word = req.params.get('word')
        word = ''.join(filter(lambda x: x.isalpha(), word))
        if not word or len(word) < MIN_CHARS:
            res.status = falcon.HTTP_400
            res.body = json.dumps({
                "message": f" enter atleast {MIN_CHARS} characters to search",
                "data": []
            })
        else:
            result = wm.top_matches(word)
            res.status = falcon.HTTP_200
            res.body = json.dumps({
                "message": "match successful.",
                "data": [data[0] for data in result]
            })
        return


# routes
app.add_route('/search', FuzzyMatch())
