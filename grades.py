# grades.py
# A simple student grade calculator

def calculate_grade(marks):
 if marks >= 90:
    return "A"
 elif marks >= 75:
    return "B"
 elif marks >= 60:
    return "C"
 else:
    return "F"

def topper(marks_dict):
 return max(marks_dict, key=marks_dict.get)
 
if __name__ == "__main__":
 marks = 82
 print("Marks:", marks)
 print("Grade:", calculate_grade(marks))
 print("Topper:", topper(marks))
