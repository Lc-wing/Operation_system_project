# Week 1 – Environment Setup

## 1. Introduction

For our CS340 project, our group chose Paper 9. We plan to reproduce some of the experiments using LEBench to study Linux kernel performance.

In the first week, I mainly worked on setting up the Linux environment. Since I had very little experience with Linux before, I spent some time learning how to use Ubuntu and basic terminal commands.

## 2. Environment Setup

I used my Windows 11 laptop to set up an Ubuntu virtual machine with VirtualBox.

The main system information is listed below:

| Component | Details |
|---|---|
| Host OS | Windows 11 |
| CPU | Intel Core i9-14900HX |
| Virtual Machine | VirtualBox |
| Ubuntu Version | Ubuntu 22.04.5 LTS |
| Linux Kernel | 6.8.0-138-generic |
| CPU Cores | 4 virtual CPUs |
| RAM | 8 GB |
| Disk | 70 GB |
| GCC | 11.4.0 |
| GCC 12 | 12.3.0 |
| Make | 4.3 |
| Git | 2.34.1 |

After installing Ubuntu, I checked the system information using some basic Linux commands, such as `uname -r`, `uname -m`, and `lsb_release -a`.

I also installed GCC, Make, and Git because they will be needed for the project.

## 3. Problems I Encountered

I had a few problems while setting up the environment.

The first problem was that I could not copy and paste commands from Windows into Ubuntu. This made using the terminal quite inconvenient. I tried installing VirtualBox Guest Additions, but the installation failed because GCC 12 was missing. After installing GCC 12 and running the installation again, the problem was solved.

Another problem was that Git was not installed in Ubuntu. I noticed this when I ran my environment checking script. After installing Git, the script worked normally.

These problems took some time to solve, but they also helped me become more familiar with Linux commands.

## 4. Environment Checking Script

After setting up the environment, I created a simple Shell script called `check_environment.sh`.

The script checks the Ubuntu version, Linux kernel version, CPU information, memory, and versions of GCC, Make, and Git.

I ran the script using:

```bash
bash scripts/check_environment.sh
```

I also saved the output to a text file:

```bash
bash scripts/check_environment.sh > results/week1-environment.txt 2>&1
```

This makes it easier to check the environment again when we start running experiments.

## 5. Summary

This week, I finished setting up Ubuntu in VirtualBox and installed the basic tools needed for our project. I also wrote a simple script to check the system environment.

I have not started running the LEBench experiments yet. The main goal of this week was to make sure the Linux environment was working properly.

## 6. Plan for Next Week

Next week, I plan to download the LEBench source code into Ubuntu and try to understand how the benchmark works.

I will also try to compile the benchmark and check whether it can run correctly before starting the kernel performance experiments.
