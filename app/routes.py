from flask import render_template, Response
from app import app
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import random


@app.route('/')
@app.route('/index')
def index():
    #return ('hello')

    return render_template('index.html')

@app.route('/test.png')
def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

def create_figure():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    xs = range(100)
    ys = [random.randint(1, 50) for x in xs]
    axis.plot(xs, ys)
    return fig

@app.route('/series.png')
def plot_png_series():
    fig = create_figure_series()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

def create_figure_series():
    import csv
    with open('pelis.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        data={}
        for row in spamreader:
            #print row
            data[row[0]]=row[6]
        #print data
    
    #data = {
        #'peli 1': 1,
        #'peli 2': 1,
        #'peli 3': 1,
        #'peli 4': 2,
        #'peli 5': 4,
        #'peli 6': 1,
        #'peli 7': 5,
        #'peli 8 asdfasd fasd asdf asdf asdfad asdf asdf': 2,
        #'peli 9': 1,
        #'peli 10': 1,
        #'peli 11': 1,
        #'peli 12': 2,
        #'peli 13': 4,
        #'peli 14': 1,
        #'peli 15': 5,
        #'peli 16 asdfasd fasd asdf asdf asdfad asdf asdf': 2,
        #'peli 17': 1,
        #'peli 18': 1,
        #'peli 19': 1,
        #'peli 20': 2,
        #'peli 21': 4,
        #'peli 22': 1,
        #'peli 23': 5,
        #'peli 24 asdfasd fasd asdf asdf asdfad asdf asdf': 2,
        #'peli 25': 1,
        #'peli 26': 1,
        #'peli 27': 1,
        #'peli 28': 2,
        #'peli 29': 4,
        #'peli 30': 1,
        #'peli 31': 5,
        #'peli 32 asdfasd fasd asdf asdf asdfad asdf asdf': 2,
        #'peli 33': 1,
        #'peli 34': 1,
        #'peli 35': 1,
        #'peli 36': 2,
        #'peli 37': 4,
        #'peli 38': 1,
        #'peli 39': 5,
        #'peli 40 asdfasd fasd asdf asdf asdfad asdf asdf': 2,
        #'peli 41': 1,
        #'peli 42': 1,
        #'peli 43': 1,
        #'peli 44': 2,
        #'peli 45': 4,
        #'peli 46': 1,
        #'peli 47': 5,
        #'peli 48 asdfasd fasd asdf asdf asdfad asdf asdf': 7
        #}

    datos = list(data.values())
    etiq = list(data.keys())

    y_pos = range(len(datos))

    fig = Figure(figsize=[8.0,18.0 ], facecolor='white')
    axis = fig.add_subplot(1, 1, 1)

    #fig.tight_layout()
    #s = range(100)
    #ys = [random.randint(1, 50) for x in xs]
    axis.barh(y_pos, datos, height=.8, linewidth=0, color='skyblue', align='center')
    axis.set_yticks(y_pos)
    axis.set_yticklabels(etiq)
    axis.set_xticks([1,2,3,4,5,6,7,8,9,10])

    fig.subplots_adjust(left=0.4)
    axis.tick_params(labelsize=9)

    return fig

