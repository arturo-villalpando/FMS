# FMS
Multilang Faq System with Fastapi (Python) + Masonite ORM (PostgreSQL) + Strawberry (GraphQL)

# Install requirements

pip install -r requirements.txt

# Migrations

masonite-orm migrate

# Database Configuration

config/database.py

# Run

python main.py

# URL

http://localhost:8000/api

# Note

The api is not finished, I used to learn how work a multi lang faq system with JSON field

# First create a Faq Category
```json
mutation CreateFaqCategory {
    createFaqCategory(
        data: {category: "[{\"lang\":\"es\",\"name\":\"Música\"},{\"lang\":\"en\",\"name\":\"Music\"}]"}
    ) {
        id
        category
        createdAt
        updatedAt
        deletedAt
    }
}
```

# Second create a Faq
```json
mutation CreateFaq {
    createFaq(
        data: {categoryId: 1, faq: "[{\"lang\":\"es\",\"question\":\"¿Hola?\", \"answer\": \"Hola mundo!\"},{\"lang\":\"en\",\"question\":\"Hi?\", \"answer\": \"Hello World!\"}]"}
    ) {
        id
        faq
        createdAt
        updatedAt
        deletedAt
    }
}

```