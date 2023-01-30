
my_favorite_books = {
    "Book One" : {
        "title": "Things We Never Got Over",
        "author" : "Lucy Score",
        "rating": 5
    },

      "Book Two" : {
        "title": "Exodus: The Ravenhood Series",
        "author" : "Kate Stewart",
        "rating": 5
    },

      "Book Three" : {
        "title": "The Stop Over",
        "author" : "TL Swan",
        "rating": 4.5
    },
}


def get_title(fav_books):
   return fav_books["Book Three"].get("title")

title_of_book = get_title(my_favorite_books)
print(title_of_book)

