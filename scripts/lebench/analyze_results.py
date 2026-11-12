
import csv
import os
import re
import statistics

RESULT_DIR = "results"

files = [
    os.path.join(RESULT_DIR,
        f"output.6.8.0-138-generic-run{i}.csv")
    for i in range(1, 4)
]

def read_results(filename):
    results = {}

    with open(filename, "r", newline="") as f:
        reader = csv.reader(f)

        for row in reader:
            if len(row) < 2:
                continue

            match = re.search(
                r"^\s*(.*?)\s+(kbest|average):$",
                row[0]
            )

            if not match:
                continue

            name = match.group(1).strip()
            metric = match.group(2)

            try:
                value = float(row[1].strip())
            except ValueError:
                continue

            results[(name, metric)] = value

    return results


all_runs = [read_results(filename) for filename in files]

for i, run in enumerate(all_runs, 1):
    print(f"Run {i}: {len(run)} metrics")

if not all_runs[0]:
    raise ValueError("No benchmark metrics found. Check CSV format.")

keys = set(all_runs[0].keys())

for run in all_runs[1:]:
    if set(run.keys()) != keys:
        raise ValueError("Different benchmark metrics across runs.")

output_file = os.path.join(
    RESULT_DIR, "summary_statistics.csv"
)

with open(output_file, "w", newline="") as f:
    writer = csv.writer(f)

    writer.writerow([
        "Test", "Metric",
        "Run1", "Run2", "Run3",
        "Mean", "StdDev"
    ])

    for name, metric in sorted(keys):
        values = [run[(name, metric)] for run in all_runs]

        writer.writerow([
            name,
            metric,
            *values,
            statistics.mean(values),
            statistics.stdev(values)
        ])

print("\nBenchmark data analysis completed!")
print("Total metrics:", len(keys))
print("Number of runs:", len(all_runs))
print("Saved to:", output_file)
