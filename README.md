# YouTube-Comment-Analyzer

## You can test our app here: <a href="https://ec2-3-121-199-55.eu-central-1.compute.amazonaws.com">Analize youtube video</a>

This project analyzes YouTube video comments to classify them as positive or negative using a sentiment analysis backend. The application consists of a **Streamlit frontend** and a **Flask backend** running in a Docker container, all deployed on an **AWS EC2 instance**.

## How to use

**Enter youtube link into text area and submit it to perform analise**

<img width="789" alt="Zrzut ekranu 2025-01-13 o 12 15 11" src="https://github.com/user-attachments/assets/7ca7c47e-a2d8-42eb-b773-f8fa0a24e5f3" />

## Features

- Submit a YouTube video link to analyze its comments.
- View a video player embedded directly in the app.
- Receive an overview of the analysis, including:
  - Total comments analyzed.
  - Percentage and count of positive and negative comments.
- View detailed lists of positive and negative comments.

## Architecture

The project has a modular design consisting of the following components:

### 1. **Frontend**
- **Framework:** Streamlit
- **Key Features:**
  - Accepts YouTube video links from the user.
  - Displays an embedded video player for the submitted link.
  - Provides an overview and detailed breakdown of the sentiment analysis results.
- **Deployment:** Streamlit app is deployed on an **AWS EC2 instance**.

### 2. **Backend**
- **Framework:** Flask
- **Key Features:**
  - Processes the submitted YouTube link.
  - Fetches and analyzes comments using a sentiment analysis model.
  - Returns structured JSON responses to the frontend.
- **Containerization:** The backend is containerized using **Docker** for portability and easy deployment.

### 3. **Deployment**
- **Platform:** AWS EC2
- **Deployment Details:**
  - The Flask backend runs inside a Docker container on the EC2 instance.
  - Streamlit serves as the user-facing interface, also deployed on the same EC2 instance.
  - Backend and frontend communicate over HTTP.
