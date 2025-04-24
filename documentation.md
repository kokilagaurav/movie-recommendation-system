# Movie Recommendation System - Technical Documentation

## Project Overview
A content-based movie recommendation system that uses natural language processing and machine learning to suggest similar movies based on various features like genres, cast, crew, keywords, and overview.

## Data Processing Pipeline

### 1. Data Loading and Preparation
```python
import pandas as pd
import numpy as np

# Load and merge datasets
credits = pd.read_csv('tmdb_5000_credits.csv')
movies = pd.read_csv('tmdb_5000_movies.csv')
df = credits.merge(movies, on='title')
```

### 2. Feature Engineering
The system processes these key features:
- Movie title
- Cast (top 3 actors)
- Crew (director)
- Genres
- Keywords
- Overview

Example of feature extraction:
```python
def converter(obj):
    L = []
    for i in ast.literal_eval(obj):
        L.append(i['name'])
    return L

# Apply to genres and keywords
df['genres'] = df['genres'].apply(converter)
df['keywords'] = df['keywords'].apply(converter)
```

### 3. Text Processing
- Removes spaces from text features
- Combines all features into tags
- Applies Porter Stemming for text normalization

```python
from nltk.stem import PorterStemmer
ps = PorterStemmer()

def stem(text):
    return " ".join([ps.stem(i) for i in text.split()])
```

### 4. Vectorization and Similarity
- Uses CountVectorizer for text vectorization
- Implements cosine similarity for movie comparison

```python
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(new_df['tags']).toarray()
similarity = cosine_similarity(vectors)
```

## Recommendation Function
```python
def recommend(movie):
    try:
        movie = movie.lower()
        index = new_df[new_df['title'].str.lower() == movie].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        for i in distances[1:6]:
            print(f"- {new_df.iloc[i[0]].title.title()}")
    except IndexError:
        print("Movie not found in the database")
```

## Implementation Details

### Dependencies
- pandas
- numpy
- scikit-learn
- NLTK
- ast (Python built-in)
- pickle

### Data Flow
1. Load and merge movie datasets
2. Extract relevant features
3. Process text data
4. Create feature vectors
5. Calculate similarity matrix
6. Generate recommendations

### Output Format
The system returns top 5 movie recommendations based on content similarity.

## Model Storage
The processed data and similarity matrix are saved using pickle:
```python
pickle.dump(new_df, open('movie_list.pkl','wb'))
pickle.dump(similarity, open('similarity.pkl','wb'))
```

## Usage Example
```python
recommend('Avatar')
# Output:
# - Aliens
# - John Carter
# - Rise Of The Planet Of The Apes
# - Mars Needs Moms
# - The Last Airbender
```

## Future Improvements
1. Add weighted similarity scores
2. Implement collaborative filtering
3. Add movie posters and descriptions
4. Include user ratings and reviews
5. Add more movie metadata

---
*Note: This system uses the TMDB 5000 Movie Dataset for recommendations.*
