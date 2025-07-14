import math

scores = [95.5, 85.5, 75.5, 65.5, 55.5, 45.5, 35.5, 25.5, 15.5, 5.5]

try:
    my_score = int(input("Input my score: "))
except ValueError:
    print("Invalid input for score. Please enter a valid integer.")
    exit(1)

sum_scores = 0
students = 0
student_counts = []

for score in scores:
    try:
        student = int(input("Input student count: "))
        if student < 0:
            print("Student count cannot be negative.")
            exit(1)
    except ValueError:
        print("Invalid input for student count. Please enter a valid integer.")
        exit(1)
    
    students += student
    sum_scores += score * student
    student_counts.append(student)

if students == 0:
    print("No students entered. Cannot calculate variance.")
    exit(1)

# Calculate weighted mean
weighted_mean = float(input("Input average score: "))

# Calculate weighted variance: Σ(w_i * (x_i - μ)²) / Σ(w_i)
variance = 0
for i, score in enumerate(scores):
    variance += student_counts[i] * (score - weighted_mean) ** 2

variance = variance / students

if variance < 0:
    print("Warning: Variance is negative, which shouldn't happen with proper data.")
    variance = 0

standard_deviation = math.sqrt(variance)

# Calculate how much your score deviates from the average
my_deviation = my_score - weighted_mean

# Calculate z-score (how many standard deviations your score is from the mean)
z_score = my_deviation / standard_deviation if standard_deviation > 0 else 0

result = z_score * 10 + 50

print(f"Your score: {my_score}")
print(f"Class average: {weighted_mean}")
print(f"Standard deviation: {standard_deviation}")
print(f"Your deviation from average: {my_deviation}")
print(f"Z-score: {z_score}")
print(f"Final result: {result}")
print(f"whole students: {students}")