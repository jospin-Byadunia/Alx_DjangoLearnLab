# Social Media API

A Django REST Framework-based API for a social media platform.  
This project provides user authentication, registration, login, logout, and profile management functionalities with JWT token authentication.

---

## Table of Contents

- [Project Description](#project-description)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Setup](#setup)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

---

## Project Description

This project aims to create the foundational elements of a Social Media API. It includes:

- Django project setup with REST API functionality.
- A robust user authentication system using JWT tokens.
- User model with extra fields: bio, profile_picture, and followers.
- API endpoints for registration, login, logout, and profile management.

---

## Features

- Custom user model extending Django’s `AbstractUser`
- JWT-based authentication using **SimpleJWT**
- User registration and login
- Profile management (retrieve and update)
- Logout with token blacklist
- API tested with Postman

---

## Tech Stack

- Python 3.x
- Django 5.x
- Django REST Framework
- Django REST Framework SimpleJWT
- SQLite (default, can be replaced with MySQL/PostgreSQL)
- Postman (for API testing)

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd social_media_api

python -m venv venv
# Windows
venv\Scripts\activate
# Linux / Mac
source venv/bin/activate

Posts API endpoint

| Endpoint           | Method | Description                           |
| ------------------ | ------ | ------------------------------------- |
| `/api/posts/`      | GET    | List all posts                        |
| `/api/posts/`      | POST   | Create a new post                     |
| `/api/posts/{id}/` | GET    | Retrieve a single post                |
| `/api/posts/{id}/` | PUT    | Update a post (author only)           |
| `/api/posts/{id}/` | PATCH  | Partially update a post (author only) |
| `/api/posts/{id}/` | DELETE | Delete a post (author only)           |


## 👥 Follow and Unfollow Users

### Overview
Authenticated users can follow or unfollow other users.  
Each user has two relationship fields:
- **followers** → users who follow them  
- **following** → users they follow  

These endpoints update those relationships accordingly.

---

### 🔐 Authentication
All requests require a valid **JWT token** in the `Authorization` header.


---

### 📌 Endpoints

#### 1️⃣ Follow a User
**URL:** `/api/accounts/follow/<user_id>/`  
**Method:** `POST`  
**Permissions:** `IsAuthenticated`

**Request Example**
```bash
POST /api/accounts/follow/5/
Authorization: Bearer <access_token>
