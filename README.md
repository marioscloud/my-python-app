# 🐍 Python Microservice & Continuous Integration (CI)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)

## 📖 Overview
This repository contains the source code for a containerized Python microservice. It is engineered to be lightweight, stateless, and fully optimized for Kubernetes orchestration.

Beyond the application code, this repository dictates the **Continuous Integration (CI)** pipeline via GitHub Actions. Upon every merge to the main branch, the pipeline automatically lints the code, executes test suites, builds the Docker image, and pushes the immutable artifact to the container registry.

> **Architectural Note:** This repository is **Part 2 of a 3-tier GitOps ecosystem**. It strictly handles application logic and the CI build process. Cluster provisioning and Continuous Delivery (GitOps) states are managed externally to ensure a secure, decoupled architecture.

## ✨ Key Features
* **Containerized Architecture:** Fully Dockerized application ready for Kubernetes deployment.
* **Automated CI Pipeline:** GitHub Actions workflow for linting, testing, and building images.
* **Immutable Artifacts:** Every successful build generates a uniquely tagged container image.
* **Health Probes:** Built-in readiness and liveness endpoints for Kubernetes orchestration.

## 🚀 Local Development

### Prerequisites
* [Docker](https://docs.docker.com/get-docker/)
* [Python 3.x](https://www.python.org/downloads/)

### Build and Run Locally
1. **Clone the repository:**
```bash
   git clone [https://github.com/marioscloud/my-python-app.git](https://github.com/marioscloud/my-python-app.git)
   cd my-python-app
   ```

2. **Build the Docker Image:**
```bash
   docker build -t my-python-app:local .
   ```

3. **Run the Container:**
```bash
   docker run -p 8080:8080 my-python-app:local
   ```
   *The application will be accessible at `http://localhost:8080`.*

## 🔗 Ecosystem Repositories
* **Infrastructure Provisioning:** [`my-python-app-infra`](https://github.com/marioscloud/my-python-app-infra)
* **Application Source Code & CI (Current):** `my-python-app`
* **GitOps State & CD:** [`my-python-app-gitops`](https://github.com/marioscloud/my-python-app-gitops)
