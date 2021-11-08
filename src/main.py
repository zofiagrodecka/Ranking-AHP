import numpy as np


def calculate_priority(matrix):
    matrix /= matrix.sum(axis=0)
    print("Po normalizacji:\n", matrix)
    priority = matrix.mean(axis=1)
    print("Priority:", priority)
    return priority


def synthesize_result(criterion_priorities, alternatives_priorities):
    result = np.array([[None] * len(alternatives_priorities[0]) for _ in range(len(criterion_priorities))])
    for i in range(len(criterion_priorities)):
        for j in range(len(alternatives_priorities[0])):
            result[i][j] = alternatives_priorities[i][j] * criterion_priorities[i]
    return result


if __name__ == "__main__":
    n_criterion = 2
    experience = np.array([[1, 1/4, 4], [4, 1, 9], [1/4, 1/9, 1]])
    education = np.array([[1, 3, 1/5], [1/3, 1, 1/7], [5, 7, 1]])
    priorities = [calculate_priority(experience), calculate_priority(education)]
    criteria = np.array([[1, 4], [1/4, 1]])
    criterion_priorities = calculate_priority(criteria)
    print("Criterion priorities:", criterion_priorities)
    res = synthesize_result(criterion_priorities, priorities)
    for i in range(len(criterion_priorities)):
        print(res[i])
    total = res.sum(axis=0)
    print("Total:", total)
    print("The best choice is:", np.argmax(total), " alternative")  # indeksowane od 0
