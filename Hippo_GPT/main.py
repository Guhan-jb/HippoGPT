import argparse
import json
import os
from flask import Flask, render_template, request
import openai
import requests
import base64
app = Flask(__name__)

# Configure OpenAI API credentials
openai.api_key = 'OPEN_API_KEY'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    search_query = request.form['search']
    if("picture" in search_query):
        process(search_query)
        return render_template('index.html', search_query=False, results=True)
    
    else:
        results = search_openai(search_query)
        return render_template('index.html', search_query=search_query, results=results)



def search_openai(query):
    response = openai.Completion.create(
        engine='text-davinci-003',  # Use the GPT-3.5 engine
        prompt=query,
        max_tokens=4000,  # Adjust the response length as needed
        temperature=0.7,  # Adjust the temperature for response randomness
        n=1,  # Generate a single response
        stop=None,  # Optional stop sequence to end the response
        timeout=10,  # Optional timeout for the API request
    )
    return response.choices[0].text.strip()
def process(prompt):
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--prompt", help="Text to image prompt:", default='an isometric view of a miniature city, tilt shift, bokeh, voxel, vray render, high detail')
    parser.add_argument("-n", "--number", help="Number of images generated", default=1)
    parser.add_argument("-s", "--size", help="Image size: 256, 512 or 1024", default=256)
    args = parser.parse_args()

    api_key ="OPEN_API_KEY"
    url = 'https://api.openai.com/v1/images/generations'
    custom_headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + api_key,
    }
    reqBody = {
        "prompt": prompt,
        "n": int(args.number),
        "size": f'{args.size}x{args.size}',
        "response_format": "b64_json"
    }
    res = requests.post(url, 
        data=json.dumps(reqBody),
        headers=custom_headers,
    )
    # print(r)
    # print(r.url)
    # print(r.status_code)
   # print(res.text)
    # print(r.content)

    res_json = json.loads(res.text)
    for i in range(0, len(res_json['data'])):
        img_file_name = 'image.jpeg'
        folder="static"
        file_path = os.path.join(folder, img_file_name)

        with open(file_path, 'wb') as f:
            f.write(base64.urlsafe_b64decode(res_json['data'][i]['b64_json']))
if __name__ == '__main__':
    app.run(debug=True)
