import pandas as pd
import requests
from io import BytesIO
from bs4 import BeautifulSoup
import random

# IMDb dataset URLs
TITLE_BASICS_URL = "https://datasets.imdbws.com/title.basics.tsv.gz"
TITLE_RATINGS_URL = "https://datasets.imdbws.com/title.ratings.tsv.gz"

def fetch_and_process_data():
    """
    Fetch movie data from IMDb datasets and process it.
    """
    print("Fetching and processing data. This may take a few minutes...")
    
    # Fetch and read title basics
    basics_response = requests.get(TITLE_BASICS_URL)
    basics_df = pd.read_csv(BytesIO(basics_response.content), compression='gzip', sep='\t', low_memory=False)
    
    # Fetch and read title ratings
    ratings_response = requests.get(TITLE_RATINGS_URL)
    ratings_df = pd.read_csv(BytesIO(ratings_response.content), compression='gzip', sep='\t')
    
    # Merge dataframes
    df = pd.merge(basics_df, ratings_df, on='tconst')
    
    # Select and rename relevant columns
    df = df[['tconst', 'primaryTitle', 'startYear', 'genres', 'averageRating', 'numVotes']]
    df = df.rename(columns={
        'tconst': 'id',
        'primaryTitle': 'title',
        'startYear': 'year',
        'averageRating': 'rating',
        'numVotes': 'popularity'
    })
    
    # Convert year to numeric, dropping any rows with non-numeric years
    df['year'] = pd.to_numeric(df['year'], errors='coerce')
    df = df.dropna(subset=['year'])
    df['year'] = df['year'].astype(int)
    
    return df

def get_genre_list(df):
    """
    Get a list of unique genres from the dataset.
    """
    all_genres = set()
    for genres in df['genres'].dropna():
        all_genres.update(genres.split(','))
    return sorted(list(all_genres))

def display_genre_list(genres):
    """
    Display the list of available genres.
    """
    print("Available genres:")
    for i, genre in enumerate(genres, 1):
        print(f"{i}: {genre}")

def get_user_genre_choice(genres):
    """
    Get the user's genre choice.
    """
    while True:
        try:
            choice = int(input("Enter the number of the genre you're interested in: "))
            if 1 <= choice <= len(genres):
                return genres[choice - 1]
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

def get_optional_filters():
    """
    Get optional filter criteria from the user.
    """
    filters = {'min_rating': 0, 'min_year': 0, 'max_year': 9999}
    
    if input("Do you want to set a minimum rating? (y/n): ").lower() == 'y':
        while True:
            try:
                filters['min_rating'] = float(input("Enter minimum rating (0-10): "))
                if 0 <= filters['min_rating'] <= 10:
                    break
                else:
                    print("Rating must be between 0 and 10.")
            except ValueError:
                print("Please enter a valid number.")
    
    if input("Do you want to set a year range? (y/n): ").lower() == 'y':
        while True:
            try:
                filters['min_year'] = int(input("Enter minimum release year: "))
                filters['max_year'] = int(input("Enter maximum release year: "))
                if filters['min_year'] <= filters['max_year']:
                    break
                else:
                    print("Maximum year must be greater than or equal to minimum year.")
            except ValueError:
                print("Please enter valid years.")
    
    return filters

def filter_movies(df, genre, min_rating, min_year, max_year):
    """
    Filter movies based on genre, rating, and release year.
    """
    return df[
        (df['genres'].str.contains(genre)) &
        (df['rating'] >= min_rating) &
        (df['year'] >= min_year) &
        (df['year'] <= max_year)
    ]

def display_random_movies(df, n=10):
    """
    Display n random movies from the DataFrame.
    """
    if df.empty:
        print("No movies found matching the criteria.")
    else:
        sample = df.sample(n=min(n, len(df)))
        print(f"\nHere are {len(sample)} random movies matching your criteria:")
        for _, movie in sample.iterrows():
            print(f"{movie['title']} ({movie['year']}) - Rating: {movie['rating']}")

def get_random_suggestion(df):
    """
    Display a random movie suggestion.
    """
    if df.empty:
        print("No movies available for suggestion.")
    else:
        suggestion = df.sample(n=1).iloc[0]
        print("\nRandom Movie Suggestion:")
        print(f"Title: {suggestion['title']}")
        print(f"Year: {suggestion['year']}")
        print(f"Rating: {suggestion['rating']}")
        print(f"Popularity (number of votes): {suggestion['popularity']}")

def main():
    try:
        # Fetch and process data
        df = fetch_and_process_data()
        
        # Get genre list
        genres = get_genre_list(df)
        
        # Display genres and get user choice
        display_genre_list(genres)
        genre = get_user_genre_choice(genres)
        
        # Get optional filters
        filters = get_optional_filters()
        
        # Apply filters
        filtered_df = filter_movies(df, genre, filters['min_rating'], filters['min_year'], filters['max_year'])
        
        # Display random movies
        display_random_movies(filtered_df)
        
        # Provide random suggestion
        get_random_suggestion(filtered_df)
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
