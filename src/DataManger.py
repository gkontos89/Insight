from Extractor import *
from Datatypes import *
import csv

class DataManager():
  def __init__(self):
    self.extractor = Extractor()
    self.rootDirectory = ''
    self.movieDb = None

  def setRootDirectory(self, rootDir):
    '''
    Utility to set the root directory used for extracting
    Args:
      Full path to root directory
    '''
    self.rootDirectory = rootDir

  def runExtraction(self):
    '''
    Runs the extractor on a file system located
    at the specified root directory to store the data.
    Args:
      None.
    '''
    self.movieDb = None
    if self.rootDirectory == '':
      return -1

    self.movieDb = self.extractor.extract(self.rootDirectory)

  def loadDatabase(self, dataFile = ''):
    '''
    Loads a file containing movie information pulled out by the
    extractor and stores it into the DataManager.  File must be of type .csv
    Args:
      dataFile - string. Full path to dataFile
    '''
    self.movieDb = None

    if os.path.isfile(dataFile) and dataFile.split('.') == 'csv':
      if self.movieDb:
        self.movieDb.purgeDb()

      with open(dataFile, 'r') as csvFile:
        reader = csv.reader(csvFile)
        g = None
        for row in reader:
          # Genre located
          if row.find('[') > 0:
            if g == None:
              g = Genre()
            else: # save off current genre and start a new one
              self.movieDb.addGenre(g)
              g = Genre()
          else:
            if g:
              movie = Movie(row[0], row[2], row[1], row[3])
              g.addMovie(movie)

  def exportData(self, outputFile):
    '''
    Write extracted movie data to .csv file
    Args:
      outputFile - full path to desired .csv file
    '''
    if self.movieDb and outputFile and outputFile.split('.')[1] == "csv":
      with open(outputFile, 'w', newline='') as csvFile:
        writer = csv.writer(csvFile)

        # Write genreName to file
        for genreName, genreObject  in self.movieDb.genres.items():
          writer.writerow('[' + genreName + ']')
        
          # Parse out and write movies data contained in genre
          for movieTitle, movieObject in genreObject.movies.items():
            writer.writerow([movieTitle, movieObject.fileType, movieObject.size, movieObject.length])
