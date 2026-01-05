# Automated Software Delivery Process
FMI DevOps Course Project, Winter Semester 2025-2026

## Pipeline
This repository contains a complete, "As Code" DevOps solution for a containerized application. It leverages a T-shaped approach, providing a comprehensive horizontal pipeline with a deep-dive focus on Static Application Security Testing (SAST).

## High-level Solution Design
The solution implements a `Shift-Left` security philosophy within a GitOps-ready framework. It automates the transition of code from a developer's local environment to a production-ready Kubernetes cluster.

Core Components
- **Orchestration**: GitHub Actions
- **Containerization**: Docker
- **Orchestration**: Kubernetes (K8s)
- **Security Vertical**: SonarCloud (SAST) & Trivy (Image Scanning)
- **Infrastructure**: Terraform (IaC) & Kubernetes Manifests 

## Low-Level Solution Design
The pipeline is triggered by the SDLC phases defined in the branching strategy.

### SDLC & Branching Strategy
- **Collaborate**: All work begins with a GitHub Issue.
- **Branching**: Developers use `feature/*` branches.
- **Pull Requests**: Merging to main requires passing all status checks (Tests, SAST, and Container Scans).

#### Pipeline Stages
- Continuous Integration (CI): 
     Linting and Unit Testing to ensure code quality.
- SQL Delta Testing: Validation of migration scripts against ephemeral databases.
- Security Deep Dive: SAST scanning via SonarCloud.
- Artifact Creation: 
    Docker image build using multi-stage builds for optimization.
- Vulnerability scanning of the image filesystem using Trivy.
- Continuous Delivery (CD): 
    Automated deployment to Kubernetes using a Rolling Update strategy to ensure zero downtime.

## Static Application Security Testing (SAST)
The vertical focus is on SAST, integrated directly into the CI loop. 

By catching vulnerabilities at the SAST stage, insecure artifacts are prevented from ever reaching the Docker registry.

### Technical Implementation
`SonarCloud` is utilized to enforce a Quality Gate. The pipeline is configured to fail if the following criteria are not met:
- **Zero Blocker Vulnerabilities**: Prevents SQL Injections and insecure cryptographic algorithms.
- **Security Hotspots**: Highlights suspicious code patterns for manual review.
- **Maintainability**: Ensures code complexity remains low to prevent bad coding practices security risks.

## Setup
### Prereqs
- Kubernetes Cluster (GKE, EKS, or Minikube).
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

- **GitOps**: Transition to ArgoCD for pull-based deployments to eliminate the need for cluster credentials within GitHub Actions.

