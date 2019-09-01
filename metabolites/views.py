from django.shortcuts import render
import csv
import pandas as pd
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {}

    metabolites_df = pd.read_csv('metabolites.csv')

    all_metabolites = metabolites_df['Name'].unique()
    
    context['all_metabolites'] = all_metabolites
    return render(request, 'metabolites/index.html', context)


def metabolite_details(request):
    metabolites_df = pd.read_csv('metabolites.csv')
    metabolite_type = request.POST.get('metabolite_type').strip()
    all_metabolite_rows = metabolites_df.loc[metabolites_df['Name'] == metabolite_type]
    all_metabolite_na_data = all_metabolite_rows.groupby(['Label'])['NA Corrected with zero'].agg('sum')
    metabolite_na_corrected_sums = all_metabolite_na_data.tolist()
    metabolite_labels = all_metabolite_na_data.index.tolist()

    y = metabolite_na_corrected_sums
    x = metabolite_labels



    fig=Figure()
    ax=fig.add_subplot(111)
    ax.set_xlabel('metabolites')
    ax.set_ylabel('NA Corrected with zero (Sum)')
    ind = range(len(y))     # the x locations for the groups

    ax.bar(ind, y)

    #ax.bar(y)


    canvas=FigureCanvas(fig)
    response=HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response