from flask import Flask, render_template, request, jsonify
import mysql.connector
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'

# Database Connection (XAMPP Settings)
def db_conn():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="calorie_tracker"
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    
    path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(path)

    # Mock AI Data for demo
    result = {"name": "Healthy Bowl", "kcal": 450}

    # Save to XAMPP MySQL
    try:
        conn = db_conn()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO daily_logs (user_id, food_name, calories_consumed) VALUES (%s, %s, %s)", 
                       (1, result['name'], result['kcal']))
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"DB Error: {e}")

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
