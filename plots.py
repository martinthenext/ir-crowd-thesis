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

def plot_learning_curve(name, xdata, ydata_dict, xname=None, yname=None, baseline=None):
  """ Gets one xdata and a dict of named ydata's to plot
  """
  plt.title(name, fontsize=16)
  plt.xlabel(xname, fontsize=14)
  plt.ylabel(yname, fontsize=14)
  
  for y_data_name, y_data in ydata_dict.iteritems():
    plt.plot(xdata, y_data, label=y_data_name)
  
  plt.legend(loc=4)

  if baseline:
    plt.axhline(y=baseline, color='grey')

  filename = get_filename(name)
  plt.savefig('plots/%s' % filename)
  plt.close()
