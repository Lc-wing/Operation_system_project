
import csv
import matplotlib.pyplot as plt

input_file = "results/summary_statistics.csv"
output_file = "results/benchmark_average.png"

tests = []
times = []

# Read benchmark results
with open(input_file, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if row["Metric"] == "average":
            tests.append(row["Test"].strip())
            times.append(float(row["Mean"]))

# Sort results
data = sorted(zip(times, tests))

times = [item[0] for item in data]
tests = [item[1] for item in data]

# Draw chart
plt.figure(figsize=(11, 12))

plt.barh(tests, times)

plt.xscale("log")
plt.xlabel("Average Execution Time (seconds)")
plt.ylabel("Benchmark Tests")
plt.title("LEBench Average Benchmark Results")

plt.grid(axis="x", linestyle="--", alpha=0.5)
plt.tight_layout()

plt.savefig(output_file, dpi=300)
plt.show()

print("Chart saved to:", output_file)
