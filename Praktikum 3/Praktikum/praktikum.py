from collections import defaultdict

movies = [
    {"title": "Avengers: Endgame", "year": 2019, "rating": 8.4, "genre": "Action"},
    {"title": "Parasite", "year": 2019, "rating": 8.6, "genre": "Drama"},
    {"title": "Nomadland", "year": 2020, "rating": 7.3, "genre": "Drama"},
    {"title": "Dune", "year": 2021, "rating": 7.9, "genre": "Sci-Fi"},
    {"title": "Spider-Man: No Way Home", "year": 2021, "rating": 7.6, "genre": "Action"},
    {"title": "The French Dispatch", "year": 2021, "rating": 7.0, "genre": "Comedy"},
    {"title": "A Quiet Place Part II", "year": 2020, "rating": 7.4, "genre": "Horror"},
    {"title": "No Time To Die", "year": 2021, "rating": 6.8, "genre": "Action"},
    {"title": "THe Power of the Dog", "year": 2021, "rating": 7.3, "genre": "Drama"},
    {"title": "Eternals", "year": 2021, "rating": 6.4, "genre": "Action"},
    {"title": "The Last Duel", "year": 2021, "rating": 7.0, "genre": "Drama"},
]


def count_genres(movies, genre):
    genre_movies = filter(lambda movie: movie["genre"].lower() == genre.lower(), movies)
    return genre, len(list(genre_movies))

genre_counts = dict(map(lambda genre: count_genres(movies, genre), set(movie["genre"] for movie in movies)))


def avg_rate_by_year(movies, year):
    ratings = [movie["rating"] for movie in movies if movie["year"] == year]
    if len(ratings) > 0:
        avg_rating = sum(ratings) / len(ratings)
        return year, avg_rating
    else:
        return year, 0  

year_to_average_rating = {}
for movie in movies:
    year = movie["year"]
    if year not in year_to_average_rating:
        year_to_average_rating[year] = avg_rate_by_year(movies, year)

def higher_rate(movies):
    if not movies:
        return None
    highest_rated = max(movies, key=lambda movie: movie["rating"])
    return highest_rated

highest_rated = higher_rate(movies)

def find_movie_by_title(movies, title):
    found_movies = [movie for movie in movies if movie["title"].lower() == title.lower()]
    return found_movies

def find_movie(movies):
    title_to_search = input("Masukkan judul film yang ingin dicari: ")
    matching_movies = find_movie_by_title(movies, title_to_search)

    if matching_movies:
        for movie in matching_movies:
            title = movie["title"]
            year = movie["year"]
            genre = movie["genre"]
            rating = movie["rating"]
            print(f"Informasi Film: \n{title} ({year}), \nGenre: {genre}, \nRating: {rating}")
    else:
        print("Film tidak ditemukan.")

def main():
    while True:
        print("\nPilih tugas yang ingin dilakukan: ")
        print("1. Menghitung Jumlah Film Berdasarkan genre")
        print("2. Menghitung rata-rata rating film berdasarkan tahun rilis")
        print("3. Menemukan film dengan rating tertinggi")
        print("4. Cari Judul film")
        print("5. Keluar")
        choose = int(input("Masukan pilihan : "))

        if choose == 1:
            for genre, count in genre_counts.items():
                print(f"Jumlah Film Berdasarkan Genre '{genre}': {count}")
        elif choose == 2:
            for year, avg_rating in year_to_average_rating.items():
                print(f"Rata-rata rating untuk tahun rilis {year}: {avg_rating[1]:.2f}")
        elif choose == 3:
            if highest_rated:
                title = highest_rated["title"]
                year = highest_rated["year"]
                genre = highest_rated["genre"]
                rating = highest_rated["rating"]
                print(f"Informasi Film Terbaik: {title} ({year}), Genre: {genre}, Rating: {rating}")
            else:
                print("Film dengan judul tersebut tidak ditemukan")
        elif choose == 4:
            find_movie(movies)
        elif choose == 5:
            break
        else:
            print("Invalid Input")

if __name__ == "__main__":
    main()