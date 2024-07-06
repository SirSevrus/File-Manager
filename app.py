from flask import Flask, render_template, redirect, url_for, jsonify, request
from libs.fileUtils import get_files_data

app = Flask(__name__)
appName = "Test"
rootDir = "C:\\"

@app.route('/')
def index():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return render_template('home.html', appName=appName)

@app.route('/files_data')
def files_data():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 20))
    start = (page - 1) * per_page
    end = start + per_page
    paginated_data = dict(list(files[1].items())[start:end])
    return jsonify(paginated_data)

if __name__ == "__main__":
    files = get_files_data(rootDir)
    try:
        app.run(debug=True)
    except KeyboardInterrupt:
        exit(0)
