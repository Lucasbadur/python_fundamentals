import webbrowser

class Movie():
    """ Class for movies to add in the library """
    
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
    def __init__(self, movie_title, movie_storyline, poster, trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer
        
    def show_trailer(self):
        webbrowser.open(self.trailer)
