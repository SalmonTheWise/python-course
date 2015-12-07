__author__ = 'jack-a-lynn'
graph = dict()


def AddEdge(v1, v2):
    if (v1 not in graph):
        graph[v1] = []
    graph[v1] += v2
