from flask import Flask, request, jsonify
from services.nlp_service import process_text
from services.sql_generator import generate_sql
from database.db import db

app = Flask(__name__)
app.config.from_object('config')

db.init_app(app)

@app.route('/convert', methods=['POST'])
def convert():
    user_input = request.json.get("query")
    structured = process_text(user_input)
    sql_query = generate_sql(structured)
    return jsonify({"sql": sql_query})

if __name__ == "__main__":
    app.run(debug=True)
