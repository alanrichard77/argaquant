from flask import Flask, render_template, request
from utils.get_data import get_company_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    data = get_company_data(query)
    if data:
        return render_template('company.html', data=data)
    else:
        return render_template('not_found.html', query=query)

if __name__ == '__main__':
    app.run(debug=True)