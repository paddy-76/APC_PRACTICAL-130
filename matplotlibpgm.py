
import matplotlib.pyplot as plt
import numpy as np

# Employee dataset
employees = ["Amit", "Neha", "Raj", "Priya", "Sneha", "Karan", "Pooja", "Rohan"]
salary = [30000, 45000, 28000, 50000, 38000, 42000, 55000, 35000]
bonus = [3000, 5000, 2500, 6000, 4000, 4500, 7000, 3500]
performance = [75, 90, 65, 95, 80, 85, 98, 72]
attendance = [88, 95, 78, 96, 90, 85, 99, 82]

total_salary = [salary[i] + bonus[i] for i in range(len(employees))]
average_salary = [total / 2 for total in total_salary]

# 1. Line graph
plt.plot(employees, salary, marker="o")
plt.title("Employee Salary - Line Graph")
plt.xlabel("Employees")
plt.ylabel("Salary")
plt.show()

# 2. Vertical bar graph
plt.bar(employees, salary)
plt.title("Employee Salary - Bar Graph")
plt.xlabel("Employees")
plt.ylabel("Salary")
plt.show()

# 3. Horizontal bar graph
plt.barh(employees, bonus)
plt.title("Employee Bonus - Horizontal Bar Graph")
plt.xlabel("Bonus")
plt.ylabel("Employees")
plt.show()

# 4. Multiple bar graph
x = np.arange(len(employees))
width = 0.25
plt.bar(x - width, salary, width, label="Salary")
plt.bar(x, bonus, width, label="Bonus")
plt.bar(x + width, performance, width, label="Performance")
plt.xticks(x, employees)
plt.title("Employee Details")
plt.xlabel("Employees")
plt.ylabel("Values")
plt.legend()
plt.show()


# 6. Pie chart
plt.pie(salary, labels=employees, autopct="%1.1f%%")
plt.title("Employee Salary Share")
plt.show()

# 7. Histogram
plt.hist(salary, bins=5, edgecolor="black")
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")
plt.show()

# 8. Box plot
plt.boxplot([salary, bonus, performance],
            tick_labels=["Salary", "Bonus", "Performance"])
plt.title("Employee Data - Box Plot")
plt.ylabel("Values")
plt.show()

# 9. Area graph
plt.fill_between(employees, salary, alpha=0.5)
plt.plot(employees, salary, marker="o")
plt.title("Employee Salary - Area Graph")
plt.xlabel("Employees")
plt.ylabel("Salary")
plt.show()

# 10. Stem plot
plt.stem(employees, performance)
plt.title("Employee Performance - Stem Plot")
plt.xlabel("Employees")
plt.ylabel("Performance")
plt.show()

# 11. Step plot
plt.step(employees, attendance, where="mid")
plt.title("Employee Attendance - Step Plot")
plt.xlabel("Employees")
plt.ylabel("Attendance (%)")
plt.show()

# 12. Stack plot
plt.stackplot(employees, salary, bonus,
              labels=["Salary", "Bonus"])
plt.title("Salary and Bonus - Stack Plot")
plt.xlabel("Employees")
plt.ylabel("Amount")
plt.legend(loc="upper left")
plt.show()


