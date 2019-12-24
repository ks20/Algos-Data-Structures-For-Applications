# TODO: Your name, Cornell NetID
# TODO: Your Partner's name, Cornell NetID

# Please see instructions.txt for the description of this problem.
from exceptions import NotImplementedError

def shortest_path(graph, source, target):
  # `graph` is an object that provides a get_neighbors(node) method that returns
  # a list of (node, weight) edges. both of your graph implementations should be
  # valid inputs. you may assume that the input graph is connected, and that all
  # edges in the graph have positive edge weights.
  # 
  # `source` and `target` are both nodes in the input graph. you may assume that
  # at least one path exists from the source node to the target node.
  #
  # this method should return a tuple that looks like
  # ([`source`, ..., `target`], `length`), where the first element is a list of
  # nodes representing the shortest path from the source to the target (in
  # order) and the second element is the length of that path
  #
  # NOTE: Please see instructions.txt for additional information about the
  # return value of this method.

  shortest_distances = dict()
  allNodes = list()

  if (type(graph.graph) is dict):
    allNodes = graph.graph.keys()
  elif (type(graph.graph) is list):
    for items in graph.graph:
      allNodes.append(items[0])

  allNodes.append(target)

  for nodes in allNodes:
    path = []
    shortest_distances[nodes] = (float("inf"), path)

  currNode = source
  shortest_distances[source] = (0, [source])

  while(len(allNodes) > 0 and allNodes.__contains__(target)):
    currNode = min(shortest_distances, key=lambda k: shortest_distances[k]) #key with min value in shortest_distance

    if (currNode not in allNodes):
      del shortest_distances[currNode]
      currNode = min(shortest_distances, key=lambda k: shortest_distances[k])

    allNodes.remove(currNode)
    curr_neighbors = graph.get_neighbors(currNode)
    # print(curr_neighbors)
    for neighbor_tuples in curr_neighbors:
      node = neighbor_tuples[0]
      weight = neighbor_tuples[1]

      if (node in shortest_distances.keys()):
        if (shortest_distances[currNode][0] + weight < shortest_distances[node][0]):
          shortest_distances[node] = (shortest_distances[currNode][0] + weight, shortest_distances[currNode][1] + [node])
          # print(shortest_distances[node])

  # print(shortest_distances[target][1], shortest_distances[target][0])
  return (shortest_distances[target][1], shortest_distances[target][0])