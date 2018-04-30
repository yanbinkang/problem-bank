class Vertex(object):
    def __init__(self, key):
        self.id = key
        self.connected_to = {}

    def get_connections(self):
        return self.connected_to.keys()

    def add_neighbor(self, nbr, weight=0):
        self.connected_to[nbr] = weight

    def get_id(self):
        return self.id

class Graph:
    def __init__(self):
        self.vert_list = {}
        self.num_vertices = 0

    def add_vertex(self, key):
        self.num_vertices += 1
        new_vertex = Vertex(key)
        self.vert_list[key] = new_vertex
        return new_vertex

    def __contains__(self, n):
        return n in self.vert_list

    def add_edge(self, from_vertex, to_vertex, cost=0):
        if from_vertex not in self.vert_list:
            nv = self.add_vertex(from_vertex)

        if to_vertex not in self.vert_list:
            nv = self.add_vertex(to_vertex)

        self.vert_list[from_vertex].add_neighbor(self.vert_list[to_vertex], cost)

    def __iter__(self):
        return iter(self.vert_list.values())

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = Graph()
        for course_list in prerequisites:
            new_course, prereq = course_list
            graph.add_edge(prereq, new_course)

        stack = []
        visited = set()

        for vertex in graph:
            if vertex in visited:
                continue

            self.top_sort_util(vertex, stack, visited)

        return [vertex.get_id() for vertex in stack][::-1]

    def top_sort_util(self, vertex, stack, visited):
        visited.add(vertex)

        for child_vert in vertex.get_connections():
            if child_vert in visited:
                continue

            self.top_sort_util(child_vert, stack, visited)

        stack.append(vertex)


if __name__ == '__main__':
    s = Solution()
    print s.findOrder(2, [[1,0]])
