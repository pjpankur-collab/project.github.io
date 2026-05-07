from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

# Mock AI Logic - In a real app, you'd call a Vision API here
def analyze_food_image(image_path):
    # Simulated response
    return {
        "name": "Grilled Salmon Bowl",
        "description": "Fresh salmon with quinoa and greens.",
        "health_score": 9.1,
        "kcal": 542,
        "protein": "38g",
        "carbs": "44g",
        "fat": "22g"
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

    path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(path)
    
    # Process with Mock AI
    nutrition_data = analyze_food_image(path)
    return jsonify(nutrition_data)

if __name__ == '__main__':
    if not os.path.exists('uploads/'):
        os.makedirs('uploads/')
    app.run(debug=True)
  
