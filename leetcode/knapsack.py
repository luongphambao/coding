# -*- coding: utf-8 -*-
import os
import random


class Knapsack(object):
    # Hàm khởi tạo cho lớp Knapsack.
    # @weights là mảng khối lượng mỗi vật.
    # @values là mảng giá trị của mỗi vật.
    # @max_weight là khối lượng tối đa mà balô có thể chứa.
    # @population_size là kích thước quần thể.
    # @max_generation là số thế hệ tối đa.
    # @crossover_rate là tỉ lệ lai [0.0, 1.0].
    # @mutation_rate là tỉ lệ đột biến [0.0, 1.0].
    def __init__(self, weights, values, max_weight, population_size, max_generation, crossover_rate, mutation_rate):
        self.weights = weights
        self.values = values
        self.num_objects = len(weights)
        self.max_weight = max_weight
        self.population_size = population_size
        self.max_generation = max_generation
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate


    # Hàm tính độ thích nghi của 1 cá thể (mở rộng trả về tổng khối lượng cho việc khác).
    # Nếu tổng khối lượng các vật > khối lượng tối đa của balô thì giá trị các vật = 0.
    # @knapsack là dãy nhị phân biểu diễn NST của 1 cá thể.
    def compute_fitness(self, knapsack):
        w = 0
        v = 0
        for i in range(self.num_objects):
            if knapsack[i] == True:
                w += self.weights[i]
                v += self.values[i]
        if w > self.max_weight:
            v = 0
        return w, v


    # Hàm khởi tạo quần thể và kết hợp tính giá trị thích nghi.
    def generate_population(self):
        population = []
        # Tính số vật tối đa có thể bỏ vào balô mà không gây vượt quá trọng lượng cho phép.
        # Mục đích: tạo ra các cá thể có tiềm năng hơn.
        # Nếu khởi tạo NST = [0..0] (chưa chọn vật nào) thì rất chậm (giai đoạn này phụ thuộc tỉ lệ đột biến).
        # Nếu khởi tạo NST = [random...] thì trường hợp xấu nhất dẫn đến không có cá thể nào phù hợp.
        num_picked_items = min(self.max_weight / max(self.weights), self.num_objects)
        if num_picked_items == 0:
            return population

        # Danh sách chỉ số của các vật.
        object_indexes = range(self.num_objects)
        for i in range(self.population_size):
            # Khởi tạo balô rỗng.
            knapsack = [False] * self.num_objects
            # Chọn num_picked_items vật để cho vào balô.
            picked_items = random.sample(object_indexes, num_picked_items)
            for i in picked_items:
                knapsack[i] = True
            # Tính giá trị và khối lượng của balô.
            weight, value = self.compute_fitness(knapsack)
            population.append((knapsack, weight, value))
        return population


    # Hàm chọn ra các cá thể tốt để lai ghép
    # @population là quần thể
    def selection(self, population):
        new_population = []
        population_size = len(population)
        if population_size == 0:
            return new_population

        # Tính vòng roulete
        total_value = population[0][2]
        values = [population[0][2]]
        for individual in population[1:]:
            values.append(values[-1] + individual[2])
            total_value += individual[2]

        for _ in range(population_size):
            # Chọn ra 2 cá thể bố mẹ
            random_point_1 = random.randint(0, total_value - 1)
            random_point_2 = random.randint(0, total_value - 1)
            parent_1 = None
            parent_2 = None
            for i in range(population_size):
                if parent_1 is None and values[i] >= random_point_1:
                    parent_1 = population[i]
                if parent_2 is None and values[i] >= random_point_2:
                    parent_2 = population[i]
                if parent_1 is not None and parent_2 is not None:
                    break
            # Lai
            child_1, child_2 = self.crossover(parent_1, parent_2)
            # Đột biến
            new_population.append(self.mutate(child_1))
            new_population.append(self.mutate(child_2))

        # Chọn lọc lại các cá thể thỏa yêu cầu
        new_population = sorted(new_population, key=lambda x: x[2], reverse=True)
        selected_population = []
        for i in range(len(new_population)):
            if new_population[i][2] == 0 or i >= population_size: break
            selected_population.append(new_population[i])
        return selected_population


    # Toán tử lai ghép giữa 2 cá thể
    # @individual_1 là cá thể
    # @individual_2 là cá thể
    def crossover(self, individual_1, individual_2):
        if self.num_objects < 2 or random.random() >= self.crossover_rate:
            return individual_1[:], individual_2[:]
        # Cách cài đặt khác thay cho random.randint(1, m-2) vì không xét được num_objects=2 do random.randint(1, 0) gây lỗi
        crossover_point = 1 + random.randint(0, self.num_objects - 2)
        knapsack_1 = individual_1[0][:crossover_point] + individual_2[0][crossover_point:]
        weight_1, value_1 = self.compute_fitness(knapsack_1)
        knapsack_2 = individual_2[0][:crossover_point] + individual_1[0][crossover_point:]
        weight_2, value_2 = self.compute_fitness(knapsack_2)
        return (knapsack_1, weight_1, value_1), (knapsack_2, weight_2, value_2)


    # Hàm đột biến
    # @individual là cá thể vừa sinh ra
    def mutate(self, individual):
        knapsack = individual[0][:]
        for i in range(len(knapsack)):
            if random.random() < self.mutation_rate:
                knapsack[i] = not knapsack[i]
        weight, value = self.compute_fitness(knapsack)
        return (knapsack, weight, value)


    # Tìm cá thể có giá trị nhất trong quần thể.
    def find_best_individual(self, population):
        if len(population) == 0:
            return None
        best_individual = population[0]
        for individual in population[1:]:
            if individual[2] > best_individual[2]:
                best_individual = individual
        return best_individual


    # Hàm giải bài toán Knapsack.
    def solve(self):
        # Tạo quần thể và đánh giá
        population = self.generate_population()
        # Chọn cá thể tốt nhất tại thời điềm khởi tạo quần thể để so sánh với cá thể được chọn cuối cùng (nếu có)
        best_initial_individual = self.find_best_individual(population)
        if best_initial_individual is None:
            # Không tồn tại cá thể nào thỏa nên dừng quá trình tiến hóa.
            return None
        # Lặp qua các thế hệ
        current_generation = 0
        while current_generation < self.max_generation:
            population = self.selection(population)
            # Không tồn tại lời giải
            if len(population) == 0:
                break
            # Chọn lọc
            current_generation += 1
        return best_initial_individual, self.find_best_individual(population)


# Hàm đọc nội dung tập tin.
# @file_name là đường dẫn đến tập tin
def read_file(file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r') as f:
            max_weight = map(int, f.readline().split())[0]
            weights = map(int, f.readline().split())
            values = map(int, f.readline().split())
            return max_weight, weights, values


def main():
    file_name = raw_input('Input file name: ')
    params = read_file(file_name)
    if params is None: return
    max_weight, weights, values = params
    knapsack = Knapsack(weights, values, max_weight, 100, 500, 0.75, 0.0015)
    best_initial_individual, best_individual = knapsack.solve()
    # In cá thể tốt nhất khi khởi tạo để so sánh
    print best_initial_individual
    if best_individual is None:
        print 'No solution.'
    else:
        print 'Total weight: %d\nTotal value: %d' % (best_individual[1], best_individual[2])
        for i in range(len(best_individual[0])):
            if best_individual[0][i] == True:
                print 'Object %d: W = %d, V = %d' % (i + 1, weights[i], values[i])


if __name__ == '__main__':
    main()