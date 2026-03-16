from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load model and encoder
model = joblib.load("student_cluster_model.pkl")
encoder = joblib.load("student_encoder.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        # Collect form data
        data = {
            "Important_Factor": [request.form["important_factor"]],
            "Daily_Routine": [request.form["daily_routine"]],
            "Social_Activity": [request.form["social_activity"]],
            "Expense_Sharing": [request.form["expense_sharing"]],
            "Deal_Breaker": [request.form["deal_breaker"]],
            "Hobbies_Importance": [request.form["hobbies_importance"]],
        }

        df = pd.DataFrame(data)

        # Transform with encoder
        df_encoded = encoder.transform(df)

        # Predict cluster
        prediction = model.predict(df_encoded)[0]

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
