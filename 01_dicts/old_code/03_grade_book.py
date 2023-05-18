# Empty notas dict

notas_dict: dict = {}

# put the student number

num_student: int = int(input("Enter student number: "))

# we are gona to the ask the name and ask the number of notes avaiable and average the notes

for i in range(num_student):
    name: str = str(input("\nEnter the name: "))
    notas_dict[name] = []
    num_subjet: int = int(input("Enter the number of notes: "))
    sum: float = 0
    for number in range(num_subjet):
        note: float = float(input("Enter the note: "))
        sum += note

    notas_dict[name] = sum / num_subjet

# We show the dict

for key, avg in notas_dict.items():
    print(f"\nName: {key}, average: {avg}")

# Global average
class_average: float = 0


for avg in notas_dict.values():
    class_average += avg

class_average /= num_student

print(f"\nThe average is: {class_average}")
