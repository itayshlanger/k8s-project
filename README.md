# Survey Flask App on Kubernetes

## Overview

This project demonstrates my understanding of Kubernetes (K8s), database integration, monitoring, and Python development by deploying a Flask application on Minikube. The application features a user-friendly survey interface that collects user responses and stores them in a database. Additionally, it utilizes Prometheus and Grafana to visualize and monitor metrics derived from the survey data.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Architecture](#architecture)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Monitoring](#monitoring)
- [License](#license)

## Features

- **Flask Web Application**: A simple survey application built using Flask.
- **Database Integration**: User responses are stored in a relational database.
- **Kubernetes Deployment**: The application is containerized and deployed on Minikube.
- **Monitoring**: Metrics are collected and visualized using Prometheus and Grafana.
- **User-friendly Interface**: Easy to use survey form for users to submit their responses.

## Technologies Used

- **Python**: The programming language used for building the Flask application.
- **Flask**: A lightweight web framework for Python.
- **Minikube**: A tool for running Kubernetes locally.
- **PostgreSQL**: The relational database used to store survey responses.
- **Prometheus**: Monitoring system for collecting metrics.
- **Grafana**: Visualization tool for monitoring metrics.

## Architecture

```diff

+-----------------+
|                 |
|   Flask App     |
|                 |
+--------+--------+
         |
         |
+--------v--------+
|                 |
|  PostgreSQL DB  |
|                 |
+--------+--------+
         |
         |
+--------v--------+
|                 |
|   Prometheus    |
|                 |
+--------+--------+
         |
         |
+--------v--------+
|                 |
|     Grafana     |
|                 |
+-----------------+

```

