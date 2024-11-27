
# Django Calendar Event Application

A scalable backend service for managing calendar events. This application supports CRUD operations, filtering, and notifications, designed to showcase a production-ready solution using Django and Python.

---

## **Features**
- **CRUD Operations**: Create, Read, Update, and Delete events.
- **Filtering**: Filter events by attributes such as date and location.
- **Notifications**: Email or logging notifications for newly created events.
- **Scalability**: Designed for future scalability with caching and task queues.
- **API Documentation**: Simple RESTful endpoints for event management.

---

## **Tech Stack**
- **Backend**: Django, Django REST Framework
- **Database**: PostgreSQL (or SQLite for local development)
- **Caching**: Redis
- **Task Queue**: Celery with Redis
- **Deployment**: Docker, AWS Elastic Beanstalk

---

## **Setup Instructions**

### **Local Development**
1. Clone the repository:
   ```bash
   git clone https://github.com/omitent/calendar-test-app.git
   cd calendar-test-app
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

6. Access the app at `http://127.0.0.1:8000/api/events/`.

---

### **Using Docker**
1. Build and run the app with Docker:
   ```bash
   docker-compose up --build
   ```
2. Access the app at `http://localhost:8000/api/events/`.

---

### **Deployment to AWS Elastic Beanstalk**
1. Install the EB CLI:
   ```bash
   pip install awsebcli
   ```
2. Initialize the Elastic Beanstalk environment:
   ```bash
   eb init -p python-3.8 django-calendar-app
   eb create django-calendar-env
   ```
3. Deploy:
   ```bash
   eb deploy
   ```

---

## **API Endpoints**
- **GET** `/api/events/`: List all events.
- **POST** `/api/events/`: Create a new event.
- **GET** `/api/events/<id>/`: Retrieve an event by ID.
- **PUT/PATCH** `/api/events/<id>/`: Update an event.
- **DELETE** `/api/events/<id>/`: Delete an event.

---

## **Testing**
1. Run tests with `pytest`:
   ```bash
   pytest
   ```

2. View test coverage (if using `coverage.py`):
   ```bash
   coverage run -m pytest
   coverage report
   ```

---

## **Scalability Enhancements**
- **Database Optimization**: Indexed frequently queried fields.
- **Caching**: Implemented Redis for caching.
- **Background Tasks**: Used Celery with Redis for email notifications.
- **Load Balancing**: Configured for scalability with AWS Elastic Beanstalk.

---

## **Future Improvements**
- Add JWT authentication for secure API access.
- Enhance filtering options with complex queries.
- Use CI/CD pipelines for automated testing and deployment.
- Implement additional monitoring tools (e.g., Sentry, AWS CloudWatch).

---
