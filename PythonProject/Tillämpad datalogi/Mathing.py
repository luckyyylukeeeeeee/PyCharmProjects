# =========================
# 1. IMPORTS
# =========================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error


# =========================
# 2. LOAD DATA
# =========================
df = pd.read_csv("spotify_data.csv")

# Select features
features = [
    "tempo", "energy", "valence", "danceability",
    "acousticness", "instrumentalness", "speechiness", "popularity"
]

df = df.dropna(subset=features)
X_raw = df[features]


# =========================
# 3. SCALE DATA
# =========================
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_raw)


# =========================
# 4. UNSUPERVISED LEARNING (K-MEANS)
# =========================
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
df["cluster_id"] = kmeans.fit_predict(X_scaled)


# =========================
# 5. CLUSTER INTERPRETATION
# =========================
print("Cluster means:")
print(df.groupby("cluster_id")[features].mean())


# =========================
# 6. PCA VISUALIZATION
# =========================
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

plt.scatter(X_pca[:, 0], X_pca[:, 1], c=df["cluster_id"], cmap="viridis")
plt.title("Clusters visualized with PCA")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.show()


# =========================
# 7. SIMULATED USERS (GENERATE RATINGS)
# =========================

# Normalize tempo (important)
df["tempo_norm"] = (df["tempo"] - df["tempo"].min()) / (df["tempo"].max() - df["tempo"].min())

# User 1 – High energy
df["rating_user1"] = (
    0.30 * df["energy"] +
    0.25 * df["danceability"] +
    0.15 * df["valence"] +
    0.10 * (1 - df["acousticness"]) +
    0.10 * (1 - df["instrumentalness"]) +
    0.05 * df["speechiness"] +
    0.05 * df["popularity"]
)

# User 2 – Happy
df["rating_user2"] = (
    0.40 * df["valence"] +
    0.25 * df["energy"] +
    0.20 * df["danceability"] +
    0.15 * df["popularity"]
)

# User 3 – Chill
df["rating_user3"] = (
    0.40 * (1 - df["energy"]) +
    0.30 * (1 - df["tempo_norm"]) +
    0.20 * df["valence"] +
    0.10 * df["acousticness"]
)

# User 4 – Mainstream
df["rating_user4"] = (
    0.30 * df["energy"] +
    0.25 * df["valence"] +
    0.20 * df["danceability"] +
    0.25 * df["popularity"]
)


# Scale ratings to 1–10
for col in ["rating_user1", "rating_user2", "rating_user3", "rating_user4"]:
    df[col] = 1 + 9 * (df[col] - df[col].min()) / (df[col].max() - df[col].min())


# =========================
# 8. SUPERVISED LEARNING
# =========================

# Final feature set (including cluster_id)
X = df[features + ["cluster_id"]]

# Targets
y1 = df["rating_user1"]
y2 = df["rating_user2"]
y3 = df["rating_user3"]
y4 = df["rating_user4"]

# Train/test split
X_train, X_test, y1_train, y1_test = train_test_split(X, y1, test_size=0.2, random_state=42)
_, _, y2_train, y2_test = train_test_split(X, y2, test_size=0.2, random_state=42)
_, _, y3_train, y3_test = train_test_split(X, y3, test_size=0.2, random_state=42)
_, _, y4_train, y4_test = train_test_split(X, y4, test_size=0.2, random_state=42)

# Train models
model1 = LinearRegression()
model2 = LinearRegression()
model3 = LinearRegression()
model4 = LinearRegression()

model1.fit(X_train, y1_train)
model2.fit(X_train, y2_train)
model3.fit(X_train, y3_train)
model4.fit(X_train, y4_train)


# =========================
# 9. EVALUATION (MAE)
# =========================
pred1 = model1.predict(X_test)
pred2 = model2.predict(X_test)
pred3 = model3.predict(X_test)
pred4 = model4.predict(X_test)

print("MAE User 1:", mean_absolute_error(y1_test, pred1))
print("MAE User 2:", mean_absolute_error(y2_test, pred2))
print("MAE User 3:", mean_absolute_error(y3_test, pred3))
print("MAE User 4:", mean_absolute_error(y4_test, pred4))


# =========================
# 10. BLEND SCORE
# =========================
blend_score = (pred1 + pred2 + pred3 + pred4) / 4

print("Example blend scores:")
print(blend_score[:10])


# =========================
# 11. CONSISTENCY CHECK
# =========================
# Example: high energy songs should give higher scores for user1
df_test = X_test.copy()
df_test["pred_user1"] = pred1

print("\nAverage predicted score for high energy songs (User 1):")
print(df_test[df_test["energy"] > 0.7]["pred_user1"].mean())

print("Average predicted score for low energy songs (User 1):")
print(df_test[df_test["energy"] < 0.3]["pred_user1"].mean())


#------------------------------------------------------------------