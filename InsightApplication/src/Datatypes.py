# class for   holding a movie entry
class Movie():
  def __init__(self, title, genre, size, fileType, length):
    self.title = title
    self.size = size
    self.fileType = fileType
    self.length = length
    self.genre = genre

# class for genre
class Genre():
  def __init__(self, name):
    self.name = name
    self.movies = [] # list of movie titles belong to this genre

  def addMovie(self, movie = ''):
    self.movies.append(movie)

class MovieDb():
  def __init__(self):
    self.genres = {} # dict of genre.title, genre object
    self.movies = {} # dict of movie.title, movie object

  def purgeDb(self):
    self.genres = {} 
    self.movies = {}

  def addGenre(self, genre = None):
    '''
    Add a new genre to the extractor
    Args:
      genre - instance of genre class
    '''
    if genre:
      self.genres[genre.name] = genre

  def addMovie(self, movie = None):
    '''
    Add a new movie to the database
    Args:
      movie - instance of a movie class
    '''
    if movie:
      self.movies[movie.title] = movie