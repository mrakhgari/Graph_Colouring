from Chromosome import *

chromosomes = []
for _ in range(25):
    chromosomes.append(Chromosome())

for chromosome in chromosomes:
    print(chromosome)
    print(chromosome.fitness_function())
