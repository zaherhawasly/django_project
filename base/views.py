from cgi import print_directory
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .models import Room
from queue import PriorityQueue 

# Create your views here.

rooms=[
    {'id':1,'name':'lets learn python! a adsdsadada'},
    {'id':2,'name':'Design with me'},
    {'id':3,'name':'FronEnd developer'},
]


def home(request):
    # return HttpResponse('homepage')
    return render(request,'base/home.html')
def room(request):
    # return HttpResponse('Room')
    context={'rooms':rooms}
    return render(request,'base/room.html',context)

def room_details(request,id):
    # return HttpResponse('Room')
    context=None
    for room in rooms :
        if room['id']==int(id):
           context={'room':room}
    return render(request,'base/room_details.html',context)

def new_func():
    return 1
    

# GRAPH = {'Arad':{'Zerind':75,'Timisoara':118,'Sibiu':140},
#          'Zerind':{'Oradea':71,'Arad':75},
#          'Oradea':{'Sibiu',151},
#          'Sibiu':{'Rimniciu Vilcea':80,'Fagaras':99,'Arad':140},
#          'Fagaras':{'Sibiu':99,'Bucharest':211},
#          'Rimniciu Vilcea':{'Pitesti':97,'Craiova':146,'Sibiu':80},
#          'Timisoara':{'Lugoj':111,'Arad':118},
#          'Lugoj':{'Mehadia':70},
#          'Mehadia':{'Lugoj':70,'Dorbeta':75},
#          'Dorbeta':{'Mehadia':75,'Craiova':120},
#          'Pitesti':{'Craiova':138,'Bucharest':101},
#          'Craiova':{'Pitesti':138,'Dorbeta':120,'Rimniciu Vilcea':146},
#          'Bucharest':{'Giurgiu':90,'Urziceni':85,'Fagaras':211,'Pitesti':101},
#          'Giurgiu': {'Bucharest':90},
#          'Urziceni':{'Vaslui':142,'Hirsova':98,'Bucharest':85},
#          'Vaslui':{'Lasi':92,'Urziceni':142},
#          'Lasi':{'Neamt':87,'Vaslui':92},
#          'Neamt':{'Lasi':87},
#          'Hirsova':{'Eforie':86,'Urziceni':98},
#          'Eforie':{'Hirsova':86}
#          }
# def a_star(source, destination):
#     straight_line = {
#         'Arad': 366,
#         'Zerind': 374,
#         'Oradea': 380,
#         'Sibiu': 253,
#         'Fagaras': 176,
#         'Rimniciu Vilcea': 193,
#         'Timisoara': 329,
#         'Lugoj': 244,
#         'Mehadia': 241,
#         'Dorbeta': 242,
#         'Pitesti': 100,
#         'Craiova': 160,
#         'Bucharest': 0,
#         'Giurgiu': 77,
#         'Urziceni': 80,
#         'Vaslui': 199,
#         'Lasi': 226,
#         'Neamt': 234,
#         'Hirsova': 151,
#         'Eforie': 161
#     } 
#     p_q,visited = PriorityQueue(),{}
#     p_q.put((straight_line[source], 0, source, [source]))
#     visited[source] = straight_line[source]
#     while not p_q.empty():
#         (heuristic, cost, vertex, path) = p_q.get()
#         print('Queue Status:',heuristic, cost, vertex, path)
#         if vertex == destination:
#            return heuristic, cost, path
#         for next_node in GRAPH[vertex].keys():
#             current_cost = cost + GRAPH[vertex][next_node]
#             heuristic = current_cost + straight_line[next_node]
#             if not next_node in visited or visited[next_node] >= heuristic:
#                 visited[next_node] = heuristic
#                 p_q.put((heuristic, current_cost, next_node,path + [next_node]))

# def main():
#     print('Source :', end=' ')
#     source = input().strip()
#     print('Destination :', end=' ')
#     goal = input().strip()
#     if source not in GRAPH or goal not in GRAPH:
#         print('CITY DOES NOT EXIST.')
#     else:
#         heuristic, cost, optimal_path = a_star(source, goal)
#         print('min of total heuristic_value =', heuristic)
#         print('total min cost =', cost)
#         print('\nRoute:')
#         print(' -> '.join(city for city in optimal_path))


