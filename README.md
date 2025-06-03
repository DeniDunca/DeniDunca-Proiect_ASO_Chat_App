# 💬 Python Django Chat Application

A web-based chat application built using **Python** and **Django**, allowing users to authenticate, send messages, upload images, and interact in dedicated chat rooms. The application supports deployment both in development and production using **Docker** and **Nginx**.

![image](https://github.com/user-attachments/assets/0e033f36-f013-4402-9bb1-d23aa4b5eabd)   ![image](https://github.com/user-attachments/assets/074d2f1b-2354-4a10-9a2c-7d18135aad67)

## Technologies Used

- Python
- Django
- HTML & CSS
- PostgreSQL
- Docker
- Nginx
- FileSystemStorage (for image upload)

## Features

- User login/logout using `django.contrib.auth`
- Authenticated home page showing all messages
- Send text messages and upload images
- File upload handling with `.png` validation
- Create or join chat rooms
- Message sending inside specific rooms
- Development and production Docker environments
- Media and static file handling with Nginx

## Project Structure & Setup

### Phase 1: Initial Setup

1. Created a Django project.
2. Ran the server locally at: `http://localhost:8000`
3. Connected to the database for user and message storage.

### Phase 2: Core Features

- **Authentication**  
  Implemented login and logout with `authenticate`, `login`, `logout`.

- **Home Page**  
  Displays all messages and includes message sending and logout features.

- **Send Text and Images**  
  - Images are stored via `FileSystemStorage` in the `/media` directory.
  - `.png` files are detected and rendered as image URLs in the frontend.
 
    ![image](https://github.com/user-attachments/assets/2d05d971-9f7a-4bc2-80f9-413da9190e0e)


- **Chat Rooms**  
  - Users can create new rooms or join existing ones.
  - Each room has its own messaging interface.

    ![image](https://github.com/user-attachments/assets/e9675838-0a38-49d0-9162-45f452dbe24f)


### Phase 3: Docker Deployment

- Dockerized the app with:
  - `Dockerfile`
  - `docker-compose.yml` (includes PostgreSQL)
- Created:
  - `Dockerfile.prod`
  - `docker-compose.prod.yml`
- Configured **Nginx** to serve static and media files
- Tested both development (`localhost:8000`) and production (`localhost:1337`) modes
- Used `.env.dev` and `.env.prod` to separate configurations

### Docker Commands

```bash
# Build and run containers (development)
docker-compose up --build

# Apply migrations for PostgreSQL
docker-compose exec web python manage.py migrate
```

Developed by **Dunca Denisa Mihaela**  
Faculty of Computer Automation and Computer Science
