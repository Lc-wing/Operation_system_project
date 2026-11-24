# CS340 Operating Systems Project

## 1. Project Overview

This project focuses on reproducing selected experiments from Paper 9 using LEBench.

The main objective is to investigate Linux kernel performance by running OS benchmarks under different kernel versions and comparing the experimental results.

This project uses two Linux kernel versions:
- Linux 6.8.0-138-generic
- Linux 6.8.0-149-generic

Each kernel version was tested three times.

## 2. Experimental Environment

| Component | Configuration |
|---|---|
| Operating System | Ubuntu 22.04.5 LTS |
| Architecture | x86_64 |
| Virtual CPUs | 4 |
| Memory | 8 GB |
| Compiler | GCC 11.4.0 |
| Make | GNU Make 4.3 |
| Python | Python 3.10.12 |
| Benchmark | LEBench |

## 3. Weekly Progress

### Week 1 – Environment Setup

- Installed Ubuntu 22.04.5 LTS.
- Installed GCC, Make, and Git.
- Checked system information and Linux kernel version.
- Created an environment checking script.
- Saved the environment information.

### Week 2 – LEBench Benchmark Experiments

- Studied the LEBench benchmark source code.
- Compiled and executed the OS_Eval benchmark.
- Collected three benchmark runs using Linux 6.8.0-138-generic.
- Saved the experimental CSV files.
- Created Python scripts for data analysis and visualization.

### Week 3 – Kernel Comparison

- Installed and tested Linux 6.8.0-149-generic.
- Completed three benchmark runs for the second kernel.
- Calculated summary statistics for both kernel versions.
- Generated a kernel comparison CSV file.

### Week 4 – Code Verification and Project Finalization

- Corrected file paths in the analysis and plotting scripts.
- Checked Python script syntax.
- Re-ran the benchmark data analysis.
- Regenerated the average performance and stability charts.
- Organized project files and documentation.

## 4. Repository Structure

```text
.
├── docs/
│   └── week1-environment.md
├── experiments/
│   └── lebench/
│       └── OS_Eval.c
├── results/
│   ├── lebench/
│   │   ├── output.6.8.0-138-generic-run1.csv
│   │   ├── output.6.8.0-138-generic-run2.csv
│   │   ├── output.6.8.0-138-generic-run3.csv
│   │   ├── output.6.8.0-149-generic-run1.csv
│   │   ├── output.6.8.0-149-generic-run2.csv
│   │   ├── output.6.8.0-149-generic-run3.csv
│   │   ├── kernel_comparison.csv
│   │   ├── benchmark_average.png
│   │   └── benchmark_stability.png
│   └── week1-environment.txt
└── scripts/
    ├── check_environment.sh
    └── lebench/
        ├── analyze_results.py
        ├── compare_kernels.py
        ├── plot_results.py
        └── plot_stability.py
```

## 5. Experimental Results

A total of six benchmark runs were collected:

| Kernel Version | Number of Runs |
|---|---:|
| 6.8.0-138-generic | 3 |
| 6.8.0-149-generic | 3 |
| Total | 6 |

The analysis scripts processed 84 metric entries for each kernel version.

The project generated:
- Individual kernel summary statistics.
- Kernel comparison data in CSV format.
- Average benchmark execution time chart.
- Benchmark stability chart.

The average and stability charts are generated from the three runs of kernel 6.8.0-138-generic.

## 6. Analysis Scripts

The following scripts are included:

| Script | Purpose |
|---|---|
| analyze_results.py | Analyzes three runs of the first kernel |
| compare_kernels.py | Compares the two kernel versions |
| plot_results.py | Generates the average performance chart |
| plot_stability.py | Generates the benchmark stability chart |

## 7. How to Run the Analysis

Run the following commands from the project root directory:

```bash
python3 -m py_compile scripts/lebench/*.py

python3 scripts/lebench/analyze_results.py

python3 scripts/lebench/compare_kernels.py

python3 scripts/lebench/plot_results.py

python3 scripts/lebench/plot_stability.py
```

The scripts read the previously collected CSV files. They do not rerun the original benchmarks.

## 8. Limitations

- Only two Linux kernel versions were evaluated.
- Each kernel version was tested three times.
- Experiments were conducted in a virtualized Ubuntu environment.
- The results represent the tested environment and do not cover all possible hardware configurations.

This project reproduces selected LEBench experiments rather than the complete set of experiments in the original paper.

## 9. Conclusion

This project established a Linux benchmarking environment, executed LEBench experiments under two kernel versions, collected and analyzed benchmark data, and generated performance and stability visualizations.

The collected results and analysis scripts are maintained in this repository for reference and further evaluation.
