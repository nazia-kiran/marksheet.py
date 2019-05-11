student = input(" enter the name")
class = input(" enter the class")
group = input(" enter gruop name")
english_mark = int(input(" enter the english marks"))
urdu_mark = int(input(" enter the urdu marks"))
physics_mark = int(input(" enter the physics marks"))
maths_mark = int(input(" enter the maths marks"))
islamiat_mark = int(input(" enter the islamiat marks"))
total_marks = 500
obtained_marks = english_mark + urdu_mark + physics_mark + maths_mark + islamiat_mark
percentage = obtained_marks / total_marks * 100
print("Total Marks: ", total_marks)
print("Obtained Marks:", obtained_marks)
print("Percentage:", percentage)
if percentage <= 80:
    print("grade A+")
elif percentage >= 50:
    print ("grade D")
elif percentage < 80 and percentage > 70:
    print("grade A")
else:
    print("fail")
