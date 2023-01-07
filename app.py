from flask import Flask,request
from flask_cors import CORS
import yake

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "<h1>this is app is server</h1><p>send post request to service route</p>"


@app.route('/service', methods=['POST'])
def process_json():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        n12 = json["data"]
        #print(n12)
        s1 = n12.replace("[^a-zA-Z#]", " ")
        # removing short words
        def fun(x): return ' '.join([w for w in x.split() if len(w) > 3])
        s1 = fun(s1)
        # tokenization
        s2 = s1.split()
        all_words = ' '.join(text for text in s2)
        result = ""
        # extracting keywords
        kw_extractor = yake.KeywordExtractor()
        keywords = kw_extractor.extract_keywords(all_words)
        for kw in keywords:
            result += kw[0] + ","
        #convert string to json 
        return {"data" : result}
    else:
        return 'Content-Type not supported!'

