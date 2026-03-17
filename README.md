# Roomzy – Roommate Finder System

## Project Overview

Roomzy is a Roommate Finder System designed to help students find compatible roommates based on their lifestyle preferences. Many students face challenges while choosing roommates due to differences in habits, routines, and expectations.

This project simplifies the process by collecting user preferences and matching them with similar profiles using backend filtering logic.

---

## Features

* Find compatible roommates based on lifestyle
* User preference collection (routine, habits, hobbies, etc.)
* Smart filtering logic for matching users
* Full-stack web application
* Fast and responsive UI
* MongoDB-based data storage

---

## Tech Stack

### Frontend

* React.js
* HTML, CSS, JavaScript

### Backend

* Node.js
* Express.js

### Database

* MongoDB

---

## Containerization & Deployment

* Docker – Containerizes the application for consistent environments
* Multi-Stage Dockerfile – Optimizes build and reduces image size
* Docker Compose – Manages frontend, backend, and database services together

---

## Version Control

* Git – Tracks code changes
* GitHub – Repository hosting and collaboration

---

## How It Works

1. User registers and enters preferences
2. Preferences are stored in MongoDB
3. Backend filters users based on similarity
4. Matching profiles are retrieved
5. Recommended roommates are displayed

---

## Project Structure (Basic)

```
Roomzy/
│── frontend/        # React App
│── backend/         # Node + Express API
│── database/        # MongoDB config
│── docker-compose.yml
│── README.md
```

---

## Running the Project (Docker)

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-repo/roomzy.git
cd roomzy
```

### Step 2: Run using Docker Compose

```bash
docker-compose up --build
```

### Step 3: Access the Application

* Frontend: http://localhost:3000
* Backend: http://localhost:5000

---

## Team Members

| No. | Name               | Enrollment No |
| --- | ------------------ | ------------- |
| 1   | PALAK HARDE        | EN22CS301673  |
| 2   | PARIKSHIT GOLE     | EN22CS301685  |
| 3   | NITIN KUMAR SINGH  | EN22CS301662  |
| 4   | NITISH SINGH YADAV | EN22CS301663  |
| 5   | PRIYAL GUPTA       | EN22CS301619  |

---

## Conclusion

Roomzy provides a simple, efficient, and user-friendly solution for finding compatible roommates. By leveraging structured preference filtering and a modern tech stack, the system makes roommate selection easier and more reliable.

---

## Future Improvements

* Chat system between matched users
* Profile verification system
* Advanced filtering & ranking
* Mobile application

---
