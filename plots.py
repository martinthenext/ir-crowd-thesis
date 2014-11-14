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
  return '%s-#%s.png' % ("-".join(tokens), randrange(100))

def plot_learning_curve(name, xdata, ydata, xname=None, yname=None, baseline=None):
  plt.plot(xdata, ydata)
  plt.title(name, fontsize=16)
  plt.xlabel(xname, fontsize=14)
  plt.ylabel(yname, fontsize=14)
  
  if baseline:
    plt.axhline(y=baseline, color='grey')

  filename = get_filename(name)
  plt.savefig('plots/%s' % filename)
  plt.close()
