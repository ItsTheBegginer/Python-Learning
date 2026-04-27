import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# ==============================
# STEP 2: Load Dataset (SMALL SAMPLE)
# ==============================
movies_url = "https://raw.githubusercontent.com/zygmuntz/goodbooks-10k/master/books.csv"
ratings_url = "https://raw.githubusercontent.com/zygmuntz/goodbooks-10k/master/ratings.csv"

movies = pd.read_csv(movies_url)
ratings = pd.read_csv(ratings_url)

# Reduce dataset size (IMPORTANT)
movies = movies[['book_id', 'title']].head(1000)
ratings = ratings[['user_id', 'book_id', 'rating']]

ratings = ratings[
    (ratings['user_id'] < 300) & 
    (ratings['book_id'] < 1000)
]

print("Data loaded successfully")

# ==============================
# STEP 3: CONTENT-BASED FILTERING
# ==============================
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['title'])

cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

def content_recommend(title):
    idx = movies[movies['title'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]
    movie_indices = [i[0] for i in sim_scores]
    return movies['title'].iloc[movie_indices]

print("\nContent-Based Recommendations:")
print(content_recommend(movies['title'].iloc[0]))

# ==============================
# STEP 4: COLLABORATIVE FILTERING (ITEM-BASED)
# ==============================
item_user_matrix = ratings.pivot_table(
    index='book_id', 
    columns='user_id', 
    values='rating'
).fillna(0)

item_similarity = cosine_similarity(item_user_matrix)

item_similarity_df = pd.DataFrame(
    item_similarity, 
    index=item_user_matrix.index, 
    columns=item_user_matrix.index
)

def item_based_recommend(book_id, num_recommendations=5):
    similar_items = item_similarity_df[book_id].sort_values(ascending=False)[1:num_recommendations+1]
    return movies[movies['book_id'].isin(similar_items.index)]['title']

print("\nCollaborative (Item-Based) Recommendations:")
print(item_based_recommend(movies['book_id'].iloc[0]))

# ==============================
# STEP 5: SIMPLE EVALUATION
# ==============================
def rmse():
    actual = ratings['rating']
    predicted = ratings['rating'].mean()
    return np.sqrt(np.mean((actual - predicted) ** 2))

print("\nRMSE:", rmse())