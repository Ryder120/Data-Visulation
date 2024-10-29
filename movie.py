import matplotlib.pyplot as plt
import pandas as pd
import os

# CSV file
CSV_FILE = 'movies_data.csv'

# Function to load movie data from a CSV file
def load_movies():
    try:
        print(f"Loading movies from {CSV_FILE}...")
        return pd.read_csv(CSV_FILE).to_dict(orient='records')
    except FileNotFoundError:
        print(f"{CSV_FILE} not found. Initializing with default movies.")
        return []

# Function to save movie data to a CSV file
def save_movies(movies):
    df = pd.DataFrame(movies)
    df.to_csv(CSV_FILE, index=False)
    print(f"Movies saved to {CSV_FILE}.")


# Initial movie data if the CSV file doesn't exist
initial_movies = [
    {"title": "Inception", "average_rating": 8.8, "box_office": 836, "release_year": 2010, "genre": "Sci-Fi"},
    {"title": "The Dark Knight", "average_rating": 9.0, "box_office": 1004, "release_year": 2008, "genre": "Action"},
    {"title": "Interstellar", "average_rating": 8.6, "box_office": 677, "release_year": 2014, "genre": "Sci-Fi"},
    {"title": "The Shawshank Redemption", "average_rating": 9.3, "box_office": 58, "release_year": 1994, "genre": "Drama"},
    {"title": "Pulp Fiction", "average_rating": 8.9, "box_office": 214, "release_year": 1994, "genre": "Crime"}
]

# Save initial data if CSV file does not exist
if not os.path.exists(CSV_FILE):
    print(f"{CSV_FILE} does not exist. Saving initial movies.")
    save_movies(initial_movies)

# Step 2: Function to visualize movie data
def visualize_movies(movies):
    if not movies:
        print("No movies to display.")
        return

    titles = [movie["title"] for movie in movies]
    average_ratings = [movie["average_rating"] for movie in movies]
    box_office_revenue = [movie["box_office"] for movie in movies]

    # Set up the figure and axes
    fig, ax1 = plt.subplots(figsize=(12, 6))

    # Create a bar chart for average ratings
    ax1.bar(titles, average_ratings, color='skyblue', alpha=0.7, label='Average Rating')
    ax1.set_ylabel('Average Rating', color='blue')
    ax1.set_ylim(0, 10)  # Set the limit for ratings

    # Create a second y-axis for box office revenue
    ax2 = ax1.twinx()
    ax2.plot(titles, box_office_revenue, color='orange', marker='o', label='Box Office Revenue (in millions)')
    ax2.set_ylabel('Box Office Revenue (in millions)', color='orange')
    ax2.set_ylim(0, 1100)  # Set the limit for box office revenue

    # Adding titles and labels
    plt.title('Movie Analysis: Average Ratings and Box Office Revenue')
    ax1.grid(axis='y')
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')

    # Show the plot
    plt.show()

# Step 3: Function to add a new movie
def add_movie(movies):
    try:
        title = input("Enter the movie title: ")
        average_rating = float(input("Enter the average rating (0-10): "))
        box_office = float(input("Enter the box office revenue (in millions): "))
        release_year = int(input("Enter the release year: "))
        genre = input("Enter the genre: ")

        new_movie = {
            "title": title,
            "average_rating": average_rating,
            "box_office": box_office,
            "release_year": release_year,
            "genre": genre
        }

        movies.append(new_movie)
        save_movies(movies)
        print(f"{title} has been added successfully!\n")
    except ValueError:
        print("Invalid input. Please make sure to enter numbers correctly for ratings, box office, and release year.")

# Step 4: Function to delete a movie
def delete_movie(movies):
    title = input("Enter the movie title to delete: ")

    for movie in movies:
        if movie['title'].lower() == title.lower():
            movies.remove(movie)
            save_movies(movies)
            print(f"{title} has been deleted successfully!\n")
            return
    
    print(f"Movie '{title}' not found.\n")

# Step 5: Main Function
def main():
    print("Welcome to the Movie Analysis Tool!")
    
    movies = load_movies()

    while True:
        print("\nMenu:")
        print("1. Visualize Movies")
        print("2. Add a Movie")
        print("3. Delete a Movie")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            if movies:
                visualize_movies(movies)
            else:
                print("No movie data available.")
        elif choice == '2':
            add_movie(movies)
        elif choice == '3':
            delete_movie(movies)
        elif choice == '4':
            print("Exiting the tool. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

# Step 6: Run the program
if __name__ == "__main__":
    main()
