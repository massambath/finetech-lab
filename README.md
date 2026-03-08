# FinTech Reliability Lab

## Overview

This project is a **mini FinTech microservices architecture** designed to simulate real-world reliability issues in distributed systems.

The goal of this lab is to practice **Site Reliability Engineering (SRE)** concepts such as:

* Service communication
* Failure scenarios
* System resilience
* Observability
* Incident analysis

This project is intentionally designed so that services **can break**, allowing us to analyze and improve system reliability.

---

## Architecture

The system is composed of three microservices and a reverse proxy.

```
fintech-lab/
│
├── docker-compose.yml
│
├── api-user/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── service-account/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── service-payment/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
└── nginx/
    └── nginx.conf
```

### Services

**api-user**

* Entry point API
* Handles user requests
* Communicates with account and payment services

**service-account**

* Manages user accounts
* Returns account information

**service-payment**

* Simulates a payment processing service

**nginx**

* Reverse proxy
* Routes external requests to the internal services

---

## System Flow

```
Client
  ↓
NGINX
  ↓
api-user
  ↓
service-account
  ↓
service-payment
```

---

## Requirements

* Docker
* Docker Compose

---

## Running the Project

Clone the repository:

```bash
git clone https://github.com/yourusername/fintech-lab.git
cd fintech-lab
```

Start the system:

```bash
docker-compose up --build
```

List running containers:

```bash
docker ps
```

Stop the environment:

```bash
docker-compose down
```

---

## Example Request

Example API request:

```bash
curl http://localhost/user
```

---

## Failure Testing (SRE Practice)

This lab allows simulation of common distributed system failures.

### Stop a service

```bash
docker stop service-payment
```

### Restart a service

```bash
docker restart service-payment
```

### Observe system behavior

Questions to explore:

* What happens when the payment service is unavailable?
* Does the API return a useful error?
* Do requests timeout?
* How does the system recover?

---

## Future Improvements

Planned SRE enhancements:

* Prometheus monitoring
* Grafana dashboards
* Centralized logging
* Chaos testing
* Kubernetes deployment
* Service health checks

---

## Learning Goals

This lab helps practice concepts related to:

* Microservices architecture
* Distributed systems
* Failure scenarios
* Observability
* Reliability engineering

---

## Author

Personal lab project to practice **DevOps and SRE concepts** in a FinTech-like environment.
