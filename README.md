# Как запустить

**Необходимые зависимости:**

- Python 3.12+
- Poetry 2+
- PostgreSQL

---

1. Создаем базу данных:

```sql
CREATE DATABASE db_internship;
GRANT ALL PRIVILEGES ON DATABASE db_internship TO postgres;
```

2. Затем создаем `.env` файл в корне проекта с содержимым:

```dotenv
DB_URL=postgresql+psycopg2://postgres:password@localhost:5432/db_internship
```

3. Клонируем репозиторий и запускаем скрипт:

```bash
git clone https://github.com/maniakalochka/db_internship.git
cd db_internship
poetry install
. $(poetry env info --path)/bin/activate
cd src
python3 main.py
```

4. Смотрим результат в БД:

```sql
SELECT
    tablename
FROM
    pg_tables
WHERE
    schemaname = 'public';
```
