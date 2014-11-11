import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from random import randrange

PLOT_FOLDER = 'plots/'

def get_filename(phrase):
  tokens = phrase         \
    .lower()              \
    .replace(",", "")     \
    .replace(".", "")     \
    .split(" ")
  return '%s-%s.png' % ("-".join(tokens), randrange(100))

def plot_to_file(name, xdata, ydata, xname=None, yname=None):
  plt.plot(xdata, ydata)
  plt.title(name, fontsize=16)
  plt.xlabel(xname, fontsize=14)
  plt.ylabel(yname, fontsize=14)
  
  filename = get_filename(name)
  plt.savefig('plots/%s' % filename)
  plt.close()
