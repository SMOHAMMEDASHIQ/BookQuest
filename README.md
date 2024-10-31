# BookQuest

# Book Recommender System

## Methodology

This project implements a collaborative filtering book recommendation system using Python. The methodology can be broken down into several key steps:

### 1. Data Collection
- **Dataset**: The project uses a collection of datasets, including information about books, users, and ratings. The data is stored in CSV format and is loaded using the Pandas library.
- **Data Sources**: The datasets utilized in this project are:
  - `books.csv`: Contains book details such as ISBN, title, author, publication year, publisher, and image URL.
  - `users.csv`: Contains user information (not utilized directly in this implementation).
  - `ratings.csv`: Contains user ratings for books, which are critical for generating recommendations.

### 2. Data Preprocessing
- **Loading Data**: The CSV files are read into Pandas DataFrames, allowing for easy manipulation and analysis.
- **Data Cleaning**: 
  - Removed any rows with missing or irrelevant data.
  - Filtered out users with fewer than 200 ratings to focus on more active users.
  - Selected relevant columns to create a cleaner dataset for analysis.
  
### 3. Exploratory Data Analysis (EDA)
- Conducted an initial analysis of the datasets to understand the distribution of ratings, popular books, and active users.
- Used visualizations to explore relationships and trends within the data.

### 4. Building the Recommendation Model
- **Creating User-Item Matrix**: Generated a pivot table where rows represent book titles and columns represent user IDs. The values in the matrix are the ratings given by users to books.
- **Sparse Matrix Conversion**: Converted the user-item matrix into a sparse matrix format for efficient storage and processing.
- **Model Training**: Utilized the `NearestNeighbors` algorithm from the `sklearn` library to find similar books based on user ratings.

### 5. Recommendation Generation
- Implemented a function `recommend_book` that takes a book title as input and retrieves a list of similar books based on the collaborative filtering model.
- The recommendations are derived from the distances calculated between the input book and other books in the dataset.

### 6. Saving the Model
- Used the `pickle` library to save the trained model, book names, final ratings, and user-item matrix to artifacts for future use.

### 7. Web Application Integration
- The recommendation model can be integrated into a web application (e.g., Flask) to provide a user-friendly interface for book recommendations.

### Conclusion
This book recommendation system effectively suggests books to users based on collaborative filtering techniques. It leverages user ratings to identify similarities between books, offering personalized recommendations.

![image](https://github.com/user-attachments/assets/4607a928-1e62-47bd-bba8-26e62cebbc0c)
