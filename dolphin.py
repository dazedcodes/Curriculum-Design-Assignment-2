def create_edges(filename, V):
        """
        A filename and list of vertices, V are accepted as parameters and returns
        a list of edges.

        Input:  filename (String) - a file of edges where each line is formatted
                as [vertex (v), a vertex it's interacted with (v_neighbor)]

                vertices_list (Array) -  an array of all the unique vertices from
                the file.

        Output: edges (Array) - an array of tuples where each tuple is an edge
                [index of vertex, neighbor of vertex]

        """
        E = []
        with open(filename) as f:
            lines = f.readlines()
            for line in lines:
                line = line.rstrip("\n")
                v = line.split()[0]
                v_neighbor = line.split()[1]
                v_index = V.index(v)
                edge = [vertex_index, int(neighbor)]
                E.append(edge)
        return E

def update_verticies(V,vertex):
    """
    A list and vertex are inserted as parameters and returns an updated list of
    verticies.

    Input: list, V (Array), vertex (String) - an array of vertices, a vertex to be
           added to V.

    Output: list (Array) - updated list of vertices.

    """
    if V:
        if vertex in V:
            pass
        else:
            V.append(vertex)
    else:
        V.append(vertex)
    return V

def create_verticies(filename):
    """
    A filename is inserted as a parameter and returns a list of vertices from
    the file.

    Input: filename (String) - a file of edges where each line is formatted
           [vertex, a vertex it's interacted with]

    Output: V (Array) - an array of all the unique vertices from the file.

    """
    V = []
    with open(filename) as f:
        lines = f.readlines()
        for x in lines:
            x = x.rstrip("\n")
            vertex = x.split()[0]
            vertex_list = update_verticies(V,vertex)
    return V

def main():
    vertices = create_verticies("mammalia-dolphin-social.edges")
    print "V: ", vertices
    print " "

    edges = create_edges("mammalia-dolphin-social.edges", vertices)
    print "E: ", edges
    print " "

if __name__ == '__main__':
    main()
