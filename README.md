# Ops Dashboard - Live Data Pipeline

## Overview

This project implements a live data pipeline deployed on AWS using Docker, Amazon ECR, ECS Fargate, and an Application Load Balancer. The system processes and visualizes operational data in real time through a Streamlit dashboard.

## Architecture

Docker image → Amazon ECR → ECS Fargate → Application Load Balancer → User (browser)

## Technologies Used

Python  
Streamlit  
Docker  
AWS ECR  
AWS ECS (Fargate)  
Application Load Balancer  
Terraform  

## Features

Real-time dashboard with multiple views:
- Operations
- Energy
- Security
- Market
- Emerging Technology

Live deployment using cloud infrastructure  
Scalable container-based architecture  
Infrastructure as Code using Terraform  

## Deployment

The entire infrastructure is deployed using Terraform:

```bash
terraform init
terraform apply
