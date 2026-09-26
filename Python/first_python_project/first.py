print("Pls enter your marks for the 3 test")

marks = [0] * 3

for i in range(3):
    marks[i]=int(input("pls enter the marks for test "+str(i+1)+": "))
    print(marks[i])
    if marks[i] < 0 or marks[i] > 100:
        print("Invalid marks entered. Please enter marks between 0 and 100.")
    else:
        print(f"Marks for test {i + 1}: {marks[i]}")
        i=i+1
for i in range(3):
    print(marks[i])

def calculate_average(marks_list):
    return sum(marks_list) / len(marks_list)

print("Calculating average marks.....")
print("Average marks:", calculate_average(marks))