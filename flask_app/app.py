from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generation')
def generation():
    return 'Generation page content'

@app.route('/understanding')
def understanding():
    return 'Understanding page content'

if __name__ == '__main__':
    app.run(debug=True)