from gremlin_python import statics
from gremlin_python.structure.graph import Graph
from gremlin_python.process.graph_traversal import __
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection

from gremlin_python.process.anonymous_traversal import traversal

connection = DriverRemoteConnection('ws://localhost:8182/gremlin', 'g')
# The connection should be closed on shut down to close open connections with connection.close()
g = traversal().withRemote(connection)
# Reuse 'g' across the application

def create_data():
#  Create two vertices
    v1 = g.addV('person').property('name', 'John Doe').next()
    v2 = g.addV('person').property('name', 'Jane Smith').next()

    #  Create an edge between the vertices
    res = g.V(v1).addE('knows').to(v2).next()
    print(res)

def query():
    # Query all vertices
    vertices = g.V().toList()
    for vertex in vertices:
        print(vertex)

    # Query specific properties of vertices
    results = g.V().has('person', 'name', 'John Doe').values('name', 'age').toList()
    for result in results:
        print(result)

    # Query edges between vertices
    edges = g.V().hasLabel('person').outE('knows').inV().toList()
    for edge in edges:
        print(edge)

# herculesAge = g.V().has('name', 'hercules').values('age').next()
# print('Hercules is {} years old.'.format(herculesAge))

if __name__=="__main__":
    create_data()