# Automated Software Delivery Process
FMI DevOps Course Project, Winter Semester 2025-2026

## Overview
This repository contains a complete DevOps solution as an automated software delivery process for a Python-based application. It leverages a T-shaped approach, providing a comprehensive horizontal pipeline with deep-diving into Automated Security and SAST to ensure code integrity before deployment.
*Note: the solution assumes a dummy python project in `./src`.*

## High-level Solution Design
The solution implements a `Shift-Left` security philosophy within a GitOps-ready framework. It automates the transition of code from a developer's local environment to a production-ready Kubernetes cluster.

The architecture follows:
**Source Control:** Managed in GitHub with a branching strategy.
**CI Pipeline:** Triggered on push/PR to handle testing, linting, and security.
**Containerization:** Dockerized application packaging.
**CD Pipeline:** Automated deployment to a local kind (Kubernetes in Docker) cluster via a self-hosted WSL runner.

Core Components
- **Orchestration**: GitHub Actions
- **Containerization**: Docker
- **Orchestration**: Kubernetes (K8s)
- **Security Vertical**: SonarCloud (SAST) & Trivy (Image Scanning)
- **Infrastructure**: Kubernetes Manifests 

## Low-Level Solution Design
The pipeline is triggered by the SDLC phases defined in the branching strategy.

### 1. Workflow & Collaboration
**Source Control:** [GitHub repository](arctfx/devops-automated-software-delivery-process).
**Collaborate**: Development starts by opening an Issue and linking it to a feature branch.
**Branching Strategy:** Developers use `feature/*` branches.
     - `main` → always deployable
     - `feature/*` → new features
     - `release/*` → final QA before merging
     - `hotfix/*` → emergency fixes

All new contributions start with an issue in GitHub and are assigned to someone. The convention is to substitute `*` with `#<N>-<short-name>` where _N_ is the issue number and _short-name_ is a short name for the issue. 

### 2. SDLC Phases & Automation
This project maps directly to the following SDLC phases:
- **Planning & design:** Define application logic and infrastructure requirements.
- **Development:** Python 3.12 logic in src/.
- **Continuous Integration:** Handled by `pipeline.yml` (Unit tests, SonarCloud, Docker Build).
- **Security:** Integrated SAST and Image Scanning (Trivy).
- **Continous Deployment:** Handled by `deploy.yml` targeting a Kubernetes namespace.
- **Pull Requests**: Merging to main requires passing all status checks (Tests, SAST, and Container Scans).
Development: Python 3.12 logic in src/.

### 3. Infrastructure as Code (IaC)
- **Kubernetes:** Defined via declarative manifests in `k8s/deployment.yaml`.
- **Runner:** Self-hosted WSL runner provides the bridge to the local infrastructure.

#### Pipeline Stages
- **Continuous Integration (CI):** 
     Linting and Unit Testing to ensure code quality.
- **SQL Delta Testing:** Validation of migration scripts against ephemeral databases. [NOTIMPL]
- **Security Deep Dive:** SAST scanning via SonarCloud.
- **Artifact Creation:** 
    Docker image build using multi-stage builds for optimization.
- **Vulnerability scanning** of the image filesystem using Trivy.
- **Continuous Delivery (CD):** 
    Automated deployment to Kubernetes using a Rolling Update strategy to ensure zero downtime.

## Static Application Security Testing (SAST)
The vertical focus is on SAST, integrated directly into the CI loop. 

By catching vulnerabilities at the SAST stage, insecure artifacts are prevented from ever reaching the Docker registry.

### Technical Implementation
`SonarCloud` is utilized to enforce a Quality Gate. The pipeline is configured to fail if the following criteria are not met:
- **Zero Blocker Vulnerabilities**: Prevents SQL Injections and insecure cryptographic algorithms.
- **Security Hotspots**: Highlights suspicious code patterns for manual review.
- **Maintainability**: Ensures code complexity remains low to prevent bad coding practices security risks.

### Infrastructure as code (IaC)
- **Kubernetes:** Defined via declarative manifests in k8s/deployment.yaml.
- **Runner:** Self-hosted WSL runner provides the bridge to the local infrastructure.

## Setup
### Prereqs
- Kubernetes Cluster (currently using _kind_).
- SonarCloud account and Project Token.
- Docker Hub account for image hosting.

### GitHub Secrets Configuration
Storing the following secrets in `Settings > Secrets > Actions`:

`DOCKER_USERNAME` / `DOCKER_PASSWORD`

`SONAR_TOKEN`

`KUBE_CONFIG_DATA` (Base64 encoded)

### Deployment
Pushing a change to the main branch to trigger the pipeline:
```bash
git add .
git commit -m "feat: implement secure login logic"
git push origin main
```

### Future Improvements
- **Infrastructure as Code** (IaC): Integrate Terraform into the pipeline to automate cluster provisioning.
- **Dynamic Analysis** (DAST): Implement OWASP ZAP scans against the running K8s service.
- **Functionality:** add a fully functional web server application template [NOTIMPL]

- **GitOps**: Transition to ArgoCD for pull-based deployments to eliminate the need for cluster credentials within GitHub Actions.

