import numpy as np
import plotly
import plotly.express as px
import pandas as pd
import json

class ChartPlot():

    def __init__(self, labelx,xaxe,labely,yaxe):
        self.xaxe= xaxe
        self.yaxe= yaxe
        self.labelx= labelx
        self.labely= labely
    

    def __repr__(self): 
        df = pd.DataFrame({self.labelx : self.xaxe, self.labely: self.yaxe})
        fig = px.bar(df,x=self.labelx, y=self.labely, barmode='group' )   
        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        return graphJSON
