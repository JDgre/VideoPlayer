
class LibraryItem:
    def __init__(self, name, director, rating=0, playcount=0):
        self.name = name
        self.director = director
        self.rating = rating
        self.play_count = playcount

    def info(self):
        return f"{self.name} - {self.director} {self.stars()}"

    def stars(self):
        stars = ""
        for i in range(self.rating):
            stars += "*"
        return stars


library = {'01': LibraryItem("Tom and Jerry", "Fred Quimby", 4, 0),
           '02': LibraryItem("Breakfast at Tiffany's", "Blake Edwards", 5, 0),
           '03': LibraryItem("Casablanca", "Michael Curtiz", 2, 0),
           '04': LibraryItem("The Sound of Music", "Robert Wise", 1, 0),
           '05': LibraryItem("Gone with the Wind", "Victor Fleming", 3, 0)}


def list_all():
    output = ""
    for key in library:
        item = library[key]
        output += f"{key} {item.info()}\n"
    return output


def get_name(key):
    try:
        item = library[key]
        return item.name
    except KeyError:
        return None


def get_director(key):
    try:
        item = library[key]
        return item.director
    except KeyError:
        return None


def get_rating(key):
    try:
        item = library[key]
        return item.rating
    except KeyError:
        return -1


def set_rating(key, rating):
    try:
        item = library[key]
        item.rating = rating
    except KeyError:
        return


def get_play_count(key):
    try:
        item = library[key]
        return item.play_count
    except KeyError:
        return -1


def increment_play_count(key):
    try:
        item = library[key]
        item.play_count += 1
    except KeyError:
        return
