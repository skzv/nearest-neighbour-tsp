import math


# Computes the length of the shortest path that visits all cities once using the nearest neighbour heuristic
class NearestNeighbourTspSolution:

    def __init__(self):
        self.num_cities = 0
        self.city_coordinates = []
        self.cities_not_visited = []

    def read_cities_from_file(self, filename):
        with open(filename) as f:
            self.num_cities = int(f.readline())
            for line in f:
                tokens = line.split(' ')
                self.cities_not_visited.append(int(tokens[0]))
                x = float(tokens[1])
                y = float(tokens[2])
                self.city_coordinates.append((x, y))

    # Returns index of the nearest unvisited neighbour
    def get_nearest_unvisited_neighbour_index_and_distance(self, current_city_index):
        nearest_index = 9999999999999
        min_squared_distance = 999999999999999999999

        for i in self.cities_not_visited:
            candidate_squared_distance = self.compute_square_l2_distance(current_city_index, i)
            if candidate_squared_distance < min_squared_distance or (
                    candidate_squared_distance == min_squared_distance and i < nearest_index):
                min_squared_distance = candidate_squared_distance
                nearest_index = i

        return nearest_index, math.sqrt(min_squared_distance)

    # Computes the square of the L2 (Euclidean) distance between two cities
    def compute_square_l2_distance(self, first_city_index, second_city_index):
        dx = self.city_coordinates[first_city_index - 1][0] - self.city_coordinates[second_city_index - 1][0]
        dy = self.city_coordinates[first_city_index - 1][1] - self.city_coordinates[second_city_index - 1][1]
        return dx * dx + dy * dy

    def print_progress(self):
        num_cities_processed = self.num_cities - len(self.cities_not_visited)
        if num_cities_processed % 10 != 0:
            return

        print("{:}/{:}:{:.2f}%".format(num_cities_processed, self.num_cities,
                                       num_cities_processed / self.num_cities * 100))

    # Computes the length of the shortest path that visits all cities once using the nearest neighbour heuristic
    def compute_min_tsp_path_distance(self):
        current_city_index = 1
        #print(current_city_index)
        self.cities_not_visited.remove(current_city_index)
        total_distance = 0
        while len(self.cities_not_visited) > 0:
            self.print_progress()

            nearest_city_index, distance_to_next_city = self.get_nearest_unvisited_neighbour_index_and_distance(
                current_city_index)
            self.cities_not_visited.remove(nearest_city_index)
            current_city_index = nearest_city_index
            #print(current_city_index)
            total_distance = total_distance + distance_to_next_city

        #print(1)
        total_distance = total_distance + math.sqrt(self.compute_square_l2_distance(current_city_index, 1))
        return total_distance


if __name__ == '__main__':
    sol = NearestNeighbourTspSolution()
    sol.read_cities_from_file('data.txt')

    print(sol.compute_min_tsp_path_distance())
