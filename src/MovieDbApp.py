from tkinter import *

from DataManger import *

class MovieListbox(Listbox):
  def __init__(self, master = None, cnf = {}, **kw):
    super().__init__(master, cnf, **kw)
    self.config['selectmode'] = SINGLE
    self.bind('<<ListboxSelect>>', self.onSelect)

  def generateMovieList(self, movies = {}):
    idx = 1
    for movieName in movies:
      self.insert(idx, movieName)
      idx += 1

  def onSelect(self, evt):
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)

class DynamicGenreNotebook(ttk.Notebook):
  def __init__(self, master = None, **kw):
    super().__init__(master, **kw)

  def generateTabs(self, genres = {}):
    tabs = self.tabs()

    # Clear out old tabs
    if len(tabs) != 0:
      for tab in tabs:
        self.forget(tab)

    # Add genre tab with a listbox of the movies belonging to that gene
    for genreName, genreObject in genres.items():
      listbox = MovieListbox(self)
      listbox.generateMovieList(genreObject.movies)
      self.add(genreName, listbox)

class MovieDbApp():
  def __init__(self):
    '''
    Create the GUI and hooks to the business logic
    Args:
      None
    '''
    self.dataManger = DataManager()

    self.main = Tk()

    self.tabbedInterface = DynamicGenreNotebook(self.main)
    self.dbSyncButton = Button(self.main, text = "Sync Database", command = self.dbSyncCb)
    self.loadDbButton = Button(self.main, text = "Load Database", command = self.loadDbCb)


    self.main.mainloop()

  def dbSyncCb(self):
    '''
    Callback for DB Sync button. This will prompt the user to select
    a root directory where movies are located and run the extraction.
    This will facilitate the movie list box to be updated and the genre tabs
    Args:
      None
    '''
    self.dataManger.runExtraction()
    if self.dataManger.movieDb:
      self.tabbedInterface.generateTabs(self.dataManger.movieDb)

  def loadDbCb(self):
    '''
    Callback for the Load DB button. This will prompt the user to select
    a .csv file containing movie information
    This will facilitate the movie list box to be updated and the genre tabs
    Args:
      None
    '''
    # TODO: have user select data file
    self.dataManger.loadDatabase()
    if self.dataManger.movieDb:
      self.tabbedInterface.generateTabs(self.dataManger.movieDb)

  def selectMovieCb(self):
    '''
    Callback for when a movie is selected by the user.  This will facilitate
    the Info and Link fields to be generated in the GUI
    Args:
      None - for now
    '''
    pass

  def runSearchCb(self, searchString):
    '''
    Callback for when a search is ran.  If the movie is found the genre tab where
    the movie falls under becomes active, the listbox shows the movies under that genre
    and the movie searched for is highlighted.  Then info and links are displayed
    Args:
      searchString
    '''
    pass

  def displayMovieInfo(self, movie = None):
    '''
    Parses out and formats the movie file information and displays it on the GUI
    Args:
      movie - movie object.
    '''
    pass

  def generateWebLink(self, movie = None):
    '''
    Generates a link to the movie on IMDB and displays it
    Args:
      movie - movie object.
    '''
    pass




