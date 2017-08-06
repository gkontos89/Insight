# class for   holding a movie entry
class Movie():
  def __init__(self, title, size, fileType, length):
    self.title = title
    self.size = size
    self.fileType = fileType
    self.length = length

# class for genre
class Genre():
  def __init__(self, name):
    self.name = name
    self.movies = {} # dict of movie.title, movie object

  def addMovie(self, movie = None):
    self.movies[movie.title] = movie

class MovieDb():
  def __init__(self):
    self.genres = {}

  def purgeDb(self):
    self.genres = {} # dict of genre.title, genre object

  def addGenre(self, genre = None):
    '''
    Add a new genre to the extractor
    Args:
      genre - instance of genre class
    '''
    if genre:
      self.genres[genre.name] = genre