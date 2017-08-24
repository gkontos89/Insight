import os
from Datatypes import *

class Extractor():
  def __init__(self):
    self.movieDb = MovieDb()

  def extract(self, rootDirectory):
    '''
    Parse entire drive and store the contents
    Args:
      rootDirectory - string. location of root directory of drive containing files
    Returns:
      dictionary of genres with movies belonging to each genre
    '''
    genreList = os.listdir(rootDirectory)

    for genre in genreList:
      g = Genre(genre)

      genrePath = os.path.join(rootDirectory, genre)
      letterList = os.listdir(genrePath)

      for letter in letterList:
        letterPath = os.path.join(genrePath, letter)
        movieList = os.listdir(letterPath)

        for movieFile in movieList:
          movieAbsPath = os.path.join(letterPath, movieFile)
          title = movieFile
          fileType = movieFile.split('.')[1]
          size = os.path.getsize(movieAbsPath)
          genre = g.name
          # TODO:  compute length 

          m = Movie(title, generator, size, fileType, length) 
          g.addMovie(m.title)

      self.movieDb.addGenre(g)
      self.movieDb.addMovie(m)

    return self.movieDb