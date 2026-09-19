# CI/CD Security Lab

## Overview

This project demonstrates a CI/CD pipeline with automated testing, API testing, application security testing, dependency scanning, build packaging, and cloud deployment.

## Technologies Used

- Python
- Flask
- pytest
- Bandit
- pip-audit
- GitHub Actions
- Render
- REST API

## API Testing

The Flask API was tested manually using API requests.

### GET /users

Returns all users.

Expected response:

- HTTP 200 OK

### GET /users/1

Returns a specific user.

Expected response:

- HTTP 200 OK

### GET /users/999

Tests the API response when a user does not exist.

Expected response:

- HTTP 404 Not Found

### POST /users

Creates a new user using a JSON request body.

Example request:

```json
{
  "name": "TestUser"
}
