import os
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import OrdinalEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

print("Files in current folder:")
print(os.listdir("C:\\Users\\manit\\Desktop\\Roommates\\student_cluster_app"))
# ✅ Correct dataset path
df = pd.read_csv("C:\\Users\\manit\\Desktop\\Roommates\\student_cluster_app\\dataset_3.csv")



# ✅ Load dataset
df = pd.read_csv("C:\\Users\\manit\\Desktop\\Roommates\\student_cluster_app\\dataset_3.csv")


print("📂 Dataset loaded successfully with shape:", df.shape)

# ✅ Drop unnecessary columns (only if they exist)
for col in ["Timestamp", "Username"]:
    if col in df.columns:
        df = df.drop(columns=[col])

# Rename columns (adjust as per your file)
df.columns = ["Important_Factor", "Daily_Routine", "Social_Activity",
              "Expense_Sharing", "Deal_Breaker", "Hobbies_Importance"]

# Encode categorical data
encoder = OrdinalEncoder(handle_unknown="use_encoded_value", unknown_value=-1)
df_encoded = encoder.fit_transform(df)

# Apply clustering
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
clusters = kmeans.fit_predict(df_encoded)
df["Cluster"] = clusters

# Train ML model
X = df.drop(columns=["Cluster"])
y = df["Cluster"]
X_encoded = encoder.transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_encoded, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

print("✅ Model trained with accuracy:", model.score(X_test, y_test))

# Save model & encoder
joblib.dump(model, "student_cluster_model.pkl")
joblib.dump(encoder, "student_encoder.pkl")
print("🎉 Model and encoder saved successfully!")
