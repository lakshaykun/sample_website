from flask import Flask, render_template, jsonify

app = Flask(__name__)

Services = [
    {
        'id' : '1',
        'name' : 'Prediction Model',
        'price' : '$200',
        'duration' : "3 Days"
    },
    {
        'id' : '2',
        'name' : 'Time Series Model',
        'price' : '$500',
        'duration' : "3 Days"
    },
    {
        'id' : '3',
        'name' : 'Chatbot',
        'price' : '$700',
        'duration' : "3 Days"
    },
    {
        'id' : '4',
        'name' : 'Web Development',
        'price' : '$1000',
        'duration' : "3 Days"
    }
]

@app.route('/')
def homepage():
    return render_template('index.html', jobs = Services)

# API for services
@app.route('/api/services')
def list_services():
    return jsonify(Services)

if __name__ == '__main__':
    app.run(debug = True)


