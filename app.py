from flask import Flask, render_template, request, jsonify
import mysql.connector
import os

app = Flask(__name__)
# Using static folder so images can be displayed in the browser
app.config['UPLOAD_FOLDER'] = 'static/uploads/'

# --- STEP 1: DATABASE CONNECTION ---
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="", # Default XAMPP password is empty
        database="calorie_tracker"
    )

# --- STEP 2: NUTRITION LOGIC ---
def analyze_food_image(image_path):
    # This simulates the AI detection logic
    return {
        "name": "Chapati/Roti",
        "kcal": 375,
        "protein": "10g",
        "carbs": "75g",
        "fat": "5g",
        "health_score": 7
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({"error": "No file"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    
    path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(path)
    
    # Process Image
    nutrition_data = analyze_food_image(path)

    # --- STEP 3: SAVE TO XAMPP DATABASE ---
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "INSERT INTO daily_logs (user_id, food_name, calories_consumed) VALUES (%s, %s, %s)"
        cursor.execute(query, (1, nutrition_data['name'], nutrition_data['kcal']))
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Database Error: {e}")

    return jsonify(nutrition_data)

if __name__ == '__main__':
    app.run(debug=True)
    
  
