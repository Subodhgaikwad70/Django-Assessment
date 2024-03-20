Gas Utility Consumer Services
This Django project provides consumer services for a gas utility company. It allows customers to submit service requests online, track the status of their requests, and view their account information. It also provides customer support representatives with a tool to manage requests and provide support to customers.

Installation
Clone the repository:

```bash
git clone https://github.com/your-username/gas-utility-consumer-services.git
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Apply the database migrations:

```bash
python manage.py migrate
```

Create a superuser for accessing the admin interface:

```bash
python manage.py createsuperuser
```

Run the development server:

```bash
python manage.py runserver
```

Usage

Access the admin interface at http://localhost:8000/admin/ and log in with your superuser credentials.

Manage service requests and other data through the admin interface.

Access the consumer services at http://localhost:8000/.
