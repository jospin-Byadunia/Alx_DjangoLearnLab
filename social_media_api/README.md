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
