from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

# Enable CORS for all routes
CORS(app, origins=["https://todofood-webapp.onrender.com"])  # Specify the frontend URL

# Database config (Replace with your actual Neon.tech connection string)
DATABASE_URL = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define a model
class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    meal_name = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.String(500))
    description = db.Column(db.String(500))
    time_in_minutes = db.Column(db.Integer, nullable=False)
    is_vegan = db.Column(db.Boolean, default=False)
    is_gluten_free = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return {
            "id": self.id,
            "meal_name": self.meal_name,
            "ingredients": self.ingredients,
            "description": self.description,
            "time_in_minutes": self.time_in_minutes,
            "is_vegan": self.is_vegan,
            "is_gluten_free": self.is_gluten_free
        }

# Create the database tables
with app.app_context():
    db.create_all()

# Routes
@app.route("/food", methods=["GET"])
def get_foods():
    foods = Food.query.all()
    return jsonify([food.to_dict() for food in foods])

@app.route("/food", methods=["POST"])
def add_food():
    data = request.json
    new_food = Food(
        meal_name=data["meal_name"],
        ingredients=data["ingredients"],
        description=data.get("description", ""),
        time_in_minutes=data["time_in_minutes"],
        is_vegan=data["is_vegan"],
        is_gluten_free=data["is_gluten_free"]
    )
    db.session.add(new_food)
    db.session.commit()
    return jsonify(new_food.to_dict()), 201

@app.route("/food/<int:id>", methods=["DELETE"])
def delete_food(id):
    food = Food.query.get(id)
    if food is None:
        return jsonify({"error": "Food not found"}), 404

    db.session.delete(food)
    db.session.commit()
    return jsonify({"message": "Food deleted successfully", "deleted_food": food.to_dict()}), 200


if __name__ == "__main__":
    app.run(debug=True)
