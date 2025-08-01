import pandas as pd
import matplotlib.pyplot as plt

# Generate sample dataset
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Age': [25, 30, 35, 28, 32],
    'Salary': [50000, 75000, 90000, 65000, 80000],
    'Experience (years)': [2, 5, 10, 4, 7]
}

df = pd.DataFrame(data)

# Show data
print("📊 Sample Data:")
print(df)

# Plot salary vs age
plt.figure(figsize=(8, 5))
plt.bar(df['Name'], df['Salary'], color='skyblue')
plt.title('Employee Salary by Name')
plt.ylabel('Salary ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('salary_plot.png')  # Save the chart
print("\n✅ Plot saved as 'salary_plot.png'")

# Show in window (optional, for local use)
plt.show()

# Run with "python data_analyzer.py"
