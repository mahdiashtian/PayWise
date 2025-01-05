# Payment and Product Management System Documentation

## **Project Overview**
This project is a Django-based payment and product management system that utilizes JWT authentication for secure access. The system includes user management, product handling, invoice creation, and transaction recording. It integrates third-party services such as MinIO for image storage and utilizes DRF Spectacular for API documentation.

---

## Project Structure

```
├── common/            # Common utilities and shared code
├── config/            # Project configuration and settings
├── informing/         # Notification system
├── users/            # User management app
├── warehouse/        # Product and inventory management
├── templates/        # HTML templates
├── static/           # Static files
└── requirements.txt  # Project dependencies
```


---

## **Project Configuration (Settings)**
The project settings are split across multiple files to separate concerns:
- **base.py**: Core settings.
- **dev.py**: Development-specific settings.
- **prod.py**: Production-specific settings.
- **local.py**: Local-specific settings.

### **Environment Variables**
The project relies on environment variables for sensitive configurations:
```env
SECRET_KEY=your_secret_key
DEBUG=True/False
ALLOWED_HOST=your_allowed_hosts
AWS_ACCESS_KEY_ID=your_aws_key
AWS_SECRET_ACCESS_KEY=your_aws_secret
AWS_STORAGE_BUCKET_NAME=your_bucket_name
AWS_S3_ENDPOINT_URL=your_endpoint
BROKER_PROTOCOL=amqp
BROKER_USERNAME=your_username
BROKER_PASSWORD=your_password
BROKER_HOST=your_host
BROKER_PORT=your_port
REDIS_HOST=localhost
REDIS_PORT=6379
```


### **Additional Environment Variables for Production and Development**
```
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_passwod
DB_HOST=your_db_host
DB_PORT=your_db_port
```
---
## **Features**
### **Authentication**
- JWT-based authentication using `rest_framework_simplejwt`.
- Register, login, and logout APIs.
- User profile management.

### **Product Management**
- Admin-only product management APIs.
- Upload and manage product images stored in MinIO.
- Secure access to images via signed URLs.

### **Invoice Management**
- Users can create invoices.
- Retrieve a list of invoices with details.
- Many-to-Many relationship between products and invoices.

### **Transaction Management**
- Record transactions for invoices.
- View transaction history.

---

## **Third-Party Integrations**
### **MinIO**
MinIO is used for storing product images securely. The `django-storages` library facilitates the integration.
```python
# MinIO Configuration
AWS_ACCESS_KEY_ID = env.str('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env.str('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = env.str('AWS_STORAGE_BUCKET_NAME')
AWS_S3_ENDPOINT_URL = env.str('AWS_S3_ENDPOINT_URL')
AWS_S3_FILE_OVERWRITE = False
```

### **Celery**
Celery is used for handling asynchronous tasks.
```python
# Broker Configuration
BROKER_URL = f"{env.str('BROKER_PROTOCOL')}://{env.str('BROKER_USERNAME')}:{env.str('BROKER_PASSWORD')}@{env.str('BROKER_HOST')}:{env.str('BROKER_PORT')}"
CELERY_BROKER_URL = BROKER_URL
```

### **Redis**
Redis is used as a backend for Django channels.
```python
# Redis settings for channels
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [(env.str('REDIS_HOST'), env.int('REDIS_PORT'))],
        },
    },
}
```

---

## **API Endpoints**
### **Authentication APIs**
| Method | Endpoint          | Description              |
|--------|-------------------|--------------------------|
| POST   | /api/v1/register/    | Register a new user      |
| POST   | /api/v1/login/       | User login and get token |
| POST   | /api/v1/logout/      | Invalidate token         |
| GET    | /api/v1/profile/     | View/edit user profile   |

### **User APIs**
| Method | Endpoint                    | Description                          |
|--------|-----------------------------|--------------------------------------|
| GET    | /api/v1/users/                 | Get a list of users (Admin)          |
| POST   | /api/v1/users/                 | Create a new user                    |
| GET    | /api/v1/users/me/              | Get current user's details           |
| POST   | /api/v1/users/change-password/ | Change the current user's password   |
| GET    | /api/v1/users/{id}/            | Get user details by ID               |
| PUT    | /api/v1/users/{id}/            | Update user details                  |
| DELETE | /api/v1/users/{id}/            | Delete a user                        |

### **Product APIs**
| Method | Endpoint            | Description                |
|--------|---------------------|----------------------------|
| POST   | /api/v1/products/      | Create a product (Admin)   |
| GET    | /api/v1/products/      | Get a list of products     |
| GET    | /api/v1/products/<id>/ | Get product details        |
| PUT    | /api/v1/products/<id>/ | Update a product (Admin)   |
| DELETE | /api/v1/products/<id>/ | Delete a product (Admin)   |

### **Invoice APIs**
| Method | Endpoint             | Description                  |
|--------|----------------------|------------------------------|
| POST   | /api/v1/invoices/       | Create an invoice            |
| GET    | /api/v1/invoices/       | Get a list of invoices       |
| GET    | /api/v1/invoices/<id>/  | Get details of an invoice    |

### **Transaction APIs**
| Method | Endpoint                 | Description                  |
|--------|--------------------------|------------------------------|
| POST   | /api/v1/transactions/       | Register a transaction        |
| GET    | /api/v1/transactions/       | Get a list of transactions    |
| GET    | /api/v1/transactions/<id>/  | Get details of a transaction  |

---

## **Testing and Documentation**
### **Tests**
- Ensure API endpoints work as expected.
- Test JWT authentication flows.
- Test User creation, updating, and deletion.

### **API Documentation**
Using DRF Spectacular to generate Swagger documentation.
```python
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}
```
Access the documentation at `/swagger/`.

---

## **Bonus Features**
- **WebSocket Notifications**: Use Django Channels to send live notifications.

---

## **Conclusion**
This project provides a comprehensive solution for managing users, products, invoices, and transactions. The system leverages JWT for secure authentication, MinIO for image storage, and Redis for WebSocket communication, making it robust and scalable.

