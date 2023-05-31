from collections import defaultdict

names_avg: dict = defaultdict(float)

notas_dict: dict = {"Jhon": [10, 9.5, 8], "Maria": [9, 8, 7], "Pedro": [8, 7, 6]}


def get_average_for_each_student(notas_per_student: dict) -> dict:

    for name, notas in notas_per_student.items():
        if any(isinstance(nota,str) for nota in notas):
            return None
        
        if any(nota < 0 for nota in notas):
            return None
        
        avg_student: float = float(sum(notas) / 3)

        names_avg[name] = round(avg_student,2)

    return names_avg


def get_average_of_the_whole_class(avg_per_student: dict) -> float:
    class_average: float = 0

    for avg in avg_per_student.values():
        class_average += avg

    class_average /= notas_dict.__len__()
    class_average=round(class_average,2)
    return class_average

