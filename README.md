# Prerequisites

1. Clone the repository
```
https://github.com/romedikc/repository-chat.git
```
2. Install the requirements
```
pip install -r requirements.txt
```
3. Create a new PostgreSQL database

In your terminal:
```
psql postgres
CREATE DATABASE databasename
\c databasename
```
4. Run the server
```
python -m uvicorn src.main:app --reload
```

