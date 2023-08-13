# FMS
Multilang Faq System with Fastapi + Masonite ORM (PostgreSQL) + Strawberry

# Install requirements

pip install -r requirements.txt

# Migrations

masonite-orm migrate -d app/databases/migrations

# Database Configuration

config/database.py

# Run

python main.py

# Note

The api is not finished, I used to learn how works a JSON field with Fastapi + Masonite ORM (PostgreSQL) + Strawberry

# Create a Faq Category
```json
mutation MyMutation {
  addFaqCategory(
    data: {category: "[{\"category\":\"Basketball\"}]", deletedAt: null}
  ) {
    id
    category
    deletedAt
  }
}
```