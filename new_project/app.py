from flask import Flask, request, render_template
import psycopg2

app = Flask(__name__)

# Connect to the database
def get_db_connection():
    conn = psycopg2.connect(
        host='db',
        database='survey',
        user='user',
        password='password'
    )
    return conn

@app.route('/')
def index():
    return render_template('survey.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    age = request.form['age']
    location = request.form['location']
    
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO responses (name, age, location) VALUES (%s, %s, %s)', (name, age, location))
    conn.commit()
    cur.close()
    conn.close()
    return 'Thank you for your response!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
