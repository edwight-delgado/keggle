import pandas as pd 

from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource, FactorRange
from bokeh.plotting import figure
from bokeh.transform import cumsum
from bokeh.layouts import row,column,gridplot
from bokeh.palettes import Category20c

data = pd.read_csv('vgsales.csv',sep=',')

df=pd.DataFrame(data)

#print(df[['Rank','Platform','Genre','Name','Year']]) 
#print(df.columns)
#verificar duplicados
#print(df.duplicated())
df.sort_values(by=['Year'],ascending=False)
print(df['Platform'].unique())
def getPlatform():
    #juegos por plataforma
    return df['Platform'].value_counts()[:10]
def getGenre():
    #mayor ranking
    print(df['Genre'].value_counts())
def getPublisher():
    #mayor ranking
    print(df['Publisher'].value_counts())


def getGenreForPublisher():
    # -generos de juegos  por empresas 

    data = {}

    for x in df.Publisher.unique()[:5]:
        genero = df.Genre[df.Publisher==str(x)].value_counts()
        if genero.count() >= 5:
            data[x]= genero
            #print('Publisher ' + str(x))
            #print(genero)
            #print('cantidad categoria ' + str(genero.count()))
    
    #print(data)
    return data

def getPublisherforPlatfom():
    print('publisher por plataforma')
    """
        cuales empresas publican sus juegos en x plataformas 
        ejm: 
        ubisoft publica 115 juegos en la plataforma Wii

    """
    data = {}

    for x in df.Platform.unique()[:10]:
        publisher = df.Publisher[df.Platform==str(x)].value_counts()
        if publisher.count() >= 5:
            data[x] = publisher
            #print('Publisher ' + str(x))
            #print(genero)
            #print('cantidad categoria ' + str(genero.count()))
    
    #print(data)
    return data


def getGenreForPlatform():
    print('generos por plataforma')
    """
        cuales generos de juegos son los que caracterizan a una consola 
        ejm: 
        xbox 360 tiene 324 titulos de accion luego 220 titulos de deportes 
        Action          324
        Sports          220
        Shooter         203


    """
    print(df.Genre[df.Platform=="X360"].value_counts())


print('get plataformas')
#x = getPlatform()
#print(x.index)
print('get generos')
#getGenre()
print('get publisher')
#getPublisher()
print('get generos por publisher')
getGenreForPublisher()


def visualization():
    import plotly.graph_objects as go
    """
    fig = go.Figure (
        data = [go.Bar( y = [ 2 , 1 , 3 ])],
        layout_title_text = "Una figura mostrada con fig.show ()"
    )

    fig.show()
    """
    platform = getPlatform()
    keys = platform.keys()
    print(platform)
    
    animals=['giraffes', 'orangutans', 'monkeys']
    fig = go.Figure(
        data=[go.Bar(x=platform.keys(), y=platform)],
        layout_title_text = "titulos por plataformas (consolas)")
    fig.show()
    
    # THIS LINE CHANGED
    #s1.vbar(x='index', bottom=0, top='value',width=2, source=df)



    #show(s1)


visualization()
"""
    cual es el año en que se generan mas titulos y 
    el año que tiene menos 
"""