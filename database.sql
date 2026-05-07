-- 1. Create the Database
CREATE DATABASE IF NOT EXISTS calorie_tracker;
USE calorie_tracker;

-- 2. Users Table (To store student/user profiles)
CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL, -- Stored as hash
    daily_calorie_goal INT DEFAULT 2000,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 3. Food Items Table (Reference data for nutrition)
CREATE TABLE IF NOT EXISTS food_items (
    food_id INT AUTO_INCREMENT PRIMARY KEY,
    food_name VARCHAR(100) NOT NULL,
    calories_per_100g FLOAT NOT NULL,
    protein_g FLOAT,
    carbs_g FLOAT,
    fat_g FLOAT,
    health_score INT CHECK (health_score BETWEEN 1 AND 10)
);

-- 4. Daily Logs Table (Records what users eat)
CREATE TABLE IF NOT EXISTS daily_logs (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    food_name VARCHAR(100),
    calories_consumed INT,
    log_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- 5. Insert some Sample Data for your Demo
INSERT INTO food_items (food_name, calories_per_100g, protein_g, carbs_g, fat_g, health_score)
VALUES 
('Chapati', 264, 9.1, 46.0, 3.6, 8),
('Paneer Tikka', 250, 15.0, 6.0, 18.0, 7),
('Dal Tadka', 120, 6.0, 15.0, 4.0, 9);

