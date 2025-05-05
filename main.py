from flask import Flask, Response
import json
import random

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_phrase():
    # Read the JSON file
    with open('data.json', 'r') as file:
        data = json.load(file)
    
    phrases = data.get('phrases', [])
    
    # Check if the list is not empty
    if phrases:
        selected_phrase = random.choice(phrases)
    else:
        selected_phrase = "No phrases available"
    
    response_data = {"ตอบ": selected_phrase}
    return Response(json.dumps(response_data, ensure_ascii=False), content_type="application/json; charset=utf-8")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001 , debug=True)
