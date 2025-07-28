# GitHub Actions Project 🛠️

This repository demonstrates the implementation of **GitHub Actions** for automating the testing of a simple Python function.

## 🔍 Project Overview

We define a simple Python function that performs addition and write a test case using `pytest` to validate it. The goal is to automate the testing process using GitHub Actions whenever code is pushed to the repository.

## ⚙️ Features

- ✅ CI/CD pipeline using **GitHub Actions**
- ✅ Automated testing on **push** events
- ✅ Runs on both:
  - **GitHub-hosted runner**
  - **Self-hosted runner**

## 🚀 How It Works

### 1. GitHub-hosted Runner

- Uses a GitHub-managed virtual machine (Ubuntu)
- Triggers on every `push`
- Installs dependencies and runs `pytest`

### 2. Self-hosted Runner

- You configure your own machine as a GitHub runner
- Workflow runs on your specified machine
- Ideal for more control over environment and testing infrastructure

## 🧪 Testing

The test is written using [`pytest`](https://docs.pytest.org/). It checks whether the `add` function returns correct output for given inputs.

To run tests locally:

```bash
pip install pytest
pytest
