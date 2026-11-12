
import csv
import matplotlib.pyplot as plt

input_file = "results/summary_statistics.csv"
output_file = "results/benchmark_stability.png"

tests = []
cv_values = []

# Read summary statistics
with open(input_file, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if row["Metric"] == "average":
            mean = float(row["Mean"])
            std = float(row["StdDev"])

            if mean > 0:
                cv = std / mean * 100

                tests.append(row["Test"].strip())
                cv_values.append(cv)

# Sort by CV
data = sorted(zip(cv_values, tests))

cv_values = [item[0] for item in data]
tests = [item[1] for item in data]

# Draw chart
plt.figure(figsize=(11, 12))

plt.barh(tests, cv_values)

plt.xlabel("Coefficient of Variation (%)")
plt.ylabel("Benchmark Tests")
plt.title("LEBench Benchmark Result Stability")

plt.grid(axis="x", linestyle="--", alpha=0.5)
plt.tight_layout()

plt.savefig(output_file, dpi=300)
plt.show()

print("Stability chart saved to:", output_file)
print("Number of benchmark tests:", len(tests))
