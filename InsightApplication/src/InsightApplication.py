# !/usr/local/bin/python
from tkinter import *
from tkinter import ttk
import easygui

from DataManger import *

class MovieListbox(Listbox):
  '''
  Class for a listbox that will contain movies and have callbacks specific
  for this application
  '''
  def __init__(self, master = None, cnf = {},  **kw):
    '''
    Initializes the listbox and sets attributes
    Args:
      master - container for where the listbox will be stored
    '''
    super().__init__(master, cnf, **kw)
    self.config(selectmode = SINGLE)
    self.bind('<<ListboxSelect>>', self.onSelect)
    self.parentContainer = master

  def generateMovieList(self, movies = []):
    '''
    This function simply populates the listbox
    Args:
      movies - list of movie titles
    '''
    idx = 1
    for title in movies:
      self.insert(idx, title)
      idx += 1

  def onSelect(self, evt):
    '''
    Callback for when an entry in the listbox is selected
    '''
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    self.parentContainer.appCallback(value)

class DynamicGenreNotebook(ttk.Notebook):
  '''
  Wrapper class for a tkinter notebook, which is a tabbed interface.
  The wrapper allows for dynamic updating of the tabs and contents
  '''
  def __init__(self, master = None, dataEventCb = None, **kw):
    '''
    initialize class
    Args:
      dataEventCb - call back function for when data has changed and
                    needs to be propogated back to the app.
    '''
    super().__init__(master, **kw)
    self.appCallback = dataEventCb

  def generateTabs(self, genres = {}):
    '''
    This function generates the genre tabs.  Also clears out old ones on
    a refresh operation.
    Args:
      genres - dictionary of {genreName, genreObject}
    '''
    tabs = self.tabs()

    # Clear out old tabs
    if len(tabs) != 0:
      for tab in tabs:
        self.forget(tab)

    # Add genre tab with a listbox of the movies belonging to that genre
    for genreName, genreObject in genres.items():
      listbox = MovieListbox(self)
      listbox.generateMovieList(genreObject.movies)
      self.add(listbox, text=genreName)

class InsightApplication():
  def __init__(self):
    '''
    Create the GUI and hooks to the business logic
    Args:
      None
    '''
    self.dataManger = DataManager()

    self.main = Tk()
    self.frame = Frame(self.main)
    self.frame.pack()

    self.tabbedInterface = DynamicGenreNotebook(self.frame, self.selectMovieCb)
    self.dbSyncButton = Button(self.frame, text = "Sync Database", command = self.dbSyncCb)
    self.loadDbButton = Button(self.frame, text = "Load Database", command = self.loadDbCb)

    self.tabbedInterface.pack()
    self.dbSyncButton.pack()
    self.loadDbButton.pack()

    self.main.mainloop()

  def dbSyncCb(self):
    '''
    Callback for DB Sync button. This will prompt the user to select
    a root directory where movies are located and run the extraction.
    This will facilitate the movie list box to be updated and the genre tabs
    Args:
      None
    '''
    folder = easygui.diropenbox()
    self.dataManger.setRootDirectory(folder)
    self.dataManger.runExtraction()

    if self.dataManger.movieDb:
      self.tabbedInterface.generateTabs(self.dataManger.movieDb.genres)

  def loadDbCb(self):
    '''
    Callback for the Load DB button. This will prompt the user to select
    a .csv file containing movie information
    This will facilitate the movie list box to be updated and the genre tabs
    Args:
      None
    '''
    file = easygui.fileopenbox()

    self.dataManger.loadDatabase(file)
    if self.dataManger.movieDb:
      self.tabbedInterface.generateTabs(self.dataManger.movieDb)

  def selectMovieCb(self, movieSelection):
    '''
    Callback for when a movie is selected by the user.  This will facilitate
    the Info and Link fields to be generated in the GUI
    Args:
      movieSelection - the movie name that was just selected by the user.
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

if __name__ == '__main__':
  app = InsightApplication()
  while 1:
    pass