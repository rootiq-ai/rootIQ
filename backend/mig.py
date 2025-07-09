# Step 1: Create migration script
alembic revision --autogenerate -m "Add alert_id to RCA table"

# Step 2: Apply migration to DB
alembic upgrade head

