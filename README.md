Overview

This project fetches, processes, and analyzes movie data from the IMDb dataset to provide users with customized movie recommendations. The tool allows users to filter movies based on genre, rating, and release year, and then displays a selection of random movies that meet the specified criteria. Additionally, it provides a random movie suggestion based on the filtered results.
Features

    Fetch and Process Data: Retrieve movie data from IMDb's online datasets and process it for analysis.
    Genre Selection: Display a list of available genres and allow the user to choose one.
    Optional Filters: Set optional filters for minimum rating and release year range.
    Movie Filtering: Filter movies based on the chosen genre and optional filters.
    Random Movie Display: Display a random selection of 10 movies that match the user's criteria.
    Random Movie Suggestion: Provide a single random movie suggestion from the filtered list.

Data Sources

The project utilizes the following IMDb datasets:

    Title Basics: Contains basic information about movies such as title, release year, and genres.
    Title Ratings: Contains user ratings and the number of votes for each movie.

Project Flow

    Fetch and Process Data:
        Download the IMDb datasets.
        Read and decompress the data.
        Merge the title basics and title ratings datasets.
        Select and rename relevant columns for analysis.
        Convert release year to numeric and drop rows with invalid years.

    Genre Selection:
        Extract and display a list of unique genres from the dataset.
        Prompt the user to select a genre.

    Optional Filters:
        Ask the user if they want to set a minimum rating and/or a release year range.
        Get the user's input for the filters if they choose to set them.

    Movie Filtering:
        Filter the movies based on the selected genre and optional filters (minimum rating and release year range).

    Display Random Movies:
        Display a random selection of 10 movies that match the user's criteria.

    Random Movie Suggestion:
        Provide a random movie suggestion from the filtered list.


Screenshots Example_1 Displaying all availabl genre and asking user to chose 1. Here Crime Genre is chosen (no.7)
![image](https://github.com/user-attachments/assets/6ac38d90-ae3d-4e8b-9e49-5ad45ce73c60)

Screenshots Example_2 Optional User Choices of rating and year range along with the suggested movie list
![image](https://github.com/user-attachments/assets/5c8dd562-ca13-40a5-845d-1638927b744e)

