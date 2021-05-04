from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Article

import numpy as np
import io
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import base64

def index( request ):
    articles = Article.objects.all()

    data = np.array( [70,30] )
    colors = ["lightgreen", "white"]
    create_graph( data, colors )
    graph_java = get_image()

    context = {
        "message" : "wellcom my BBS",
        "articles" : articles,
        #"players" : ["勇者", "戦士", "魔法使い", "忍者"]
        "graph": graph_java
    }

    return render( request, "bbs/index.html", context )

    #return HttpResponse( "hello, world" )

def detail( request, id ):
    article = get_object_or_404( Article, pk=id )
    context = {
        "message": "show Article" + str(id),
        "article": article,
    }

    return render( request, "bbs/detail.html", context )

def create_graph( data, colors ):
    plt.cla() #初期化
    plt.pie( data, colors=colors, counterclock=False, startangle=90 )

    centre_circle = plt.Circle( ( 0, 0 ), 0.6, color='black', fc='white', linewidth=0 )
    fig = plt.gcf()
    fig.gca().add_artist( centre_circle )

def get_image():
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()

    return graph
