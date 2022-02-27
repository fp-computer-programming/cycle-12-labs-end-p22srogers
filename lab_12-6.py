# Author: SMR (AMDG) 2/27/22
# Set variable report card equal to assignment of grades per assignment
report_card = {"Start S2 Labs":100,"End S1 Labs":0,"Mid-year Project Proposal":100,"Cycle 10 Practice Quiz":100,"Cycle 10 Quiz":72}
# prints report_card
print(report_card)
# for the assignment in list, print assignment
for assignment,grade in report_card.items():
    print(assignment)
# for the assignment and grade above a 70 print it out with added strings
for assignment,grade in report_card.items():
    if grade >= 75:
        print("You received  a",grade,"on",assignment,"Keep it up.")
for assignment,grade in report_card.items():
    if 73>=grade >= 51: 
        print("You received  a",grade,"on",assignment,"Do a bit better.")       
# for the assignment and grade below a 50 print it out with the added strings
for assignment,grade in report_card.items():
    if grade <= 50:
        print("You received a",grade,"on",assignment, "You need to improve.")
        