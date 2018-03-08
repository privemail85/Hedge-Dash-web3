from django.shortcuts import render

import pandas as pd

from .models import filterList

def home(request):

	filter_list =[]

	metaData = pd.read_csv('resources/static/csv/firms_metaData.csv')

	heads = list(metaData)

	for head in heads:
		filter_list.append(filterList(head, [], sorted(list(metaData[head].value_counts().index))))
	#filter_list.append(filterList("Industry", ["Savings", "Aluminum", "Life Insurance"], ["Gold", "Oil & Gas Drilling & Exploration", "Communication Equipment"]))
	#return render_to_reponse('filter_lists/dynamic-table.html', {'listInc':testListInc}, {'listExc':testListExc},)
	return render(request, 'filter_lists/dynamic-table.html', {"filter_list" : filter_list})

