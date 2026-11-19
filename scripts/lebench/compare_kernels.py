
import csv
import os
import re
import statistics

RESULT_DIR = "results/lebench"

kernels = {
    "6.8.0-138-generic": [
        os.path.join(RESULT_DIR,
                     f"output.6.8.0-138-generic-run{i}.csv")
        for i in range(1, 4)
    ],
    "6.8.0-149-generic": [
        os.path.join(RESULT_DIR,
                     f"output.6.8.0-149-generic-run{i}.csv")
        for i in range(1, 4)
    ]
}


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


summaries = {}

for kernel, files in kernels.items():

    all_runs = []

    for filename in files:
        if not os.path.exists(filename):
            raise FileNotFoundError(filename)

        all_runs.append(read_results(filename))

    keys = set(all_runs[0].keys())

    for run in all_runs[1:]:
        if set(run.keys()) != keys:
            raise ValueError(
                "Different metrics found: " + kernel
            )

    summaries[kernel] = {}

    output_file = os.path.join(
        RESULT_DIR,
        "summary_" + kernel + ".csv"
    )

    with open(output_file, "w", newline="") as f:
        writer = csv.writer(f)

        writer.writerow([
            "Test", "Metric",
            "Run1", "Run2", "Run3",
            "Mean", "StdDev"
        ])

        for name, metric in sorted(keys):
            values = [
                run[(name, metric)]
                for run in all_runs
            ]

            mean_value = statistics.mean(values)
            std_value = statistics.stdev(values)

            summaries[kernel][(name, metric)] = mean_value

            writer.writerow([
                name,
                metric,
                *values,
                mean_value,
                std_value
            ])

    print(kernel, ":", len(keys), "metrics")
    print("Saved:", output_file)


# Compare the two kernel versions

kernel138 = "6.8.0-138-generic"
kernel149 = "6.8.0-149-generic"

keys138 = set(summaries[kernel138].keys())
keys149 = set(summaries[kernel149].keys())

if keys138 != keys149:
    raise ValueError("Kernel metrics do not match.")

comparison_file = os.path.join(
    RESULT_DIR,
    "kernel_comparison.csv"
)

with open(comparison_file, "w", newline="") as f:
    writer = csv.writer(f)

    writer.writerow([
        "Test", "Metric",
        "Kernel138_Mean",
        "Kernel149_Mean",
        "Change_Percent"
    ])

    for name, metric in sorted(keys138):

        old = summaries[kernel138][(name, metric)]
        new = summaries[kernel149][(name, metric)]

        change = (new - old) / old * 100 if old != 0 else 0

        writer.writerow([
            name,
            metric,
            old,
            new,
            change
        ])

print("\nKernel comparison completed!")
print("Total metrics:", len(keys138))
print("Saved:", comparison_file)
