# Financial Data Aggregator

This project aggregates financial data from various Japanese financial institutions, providing a unified view of your accounts.

## Key Technologies

*   **Backend:** Python, FastAPI, SQLAlchemy, Alembic
*   **Frontend:** React, Vite
*   **Database:** PostgreSQL (implicitly, as it's common with SQLAlchemy and Alembic)
*   **Containerization:** Docker, Docker Compose

## Setup and Running

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Configure Environment Variables:**
    Copy the `.env.example` file to `.env` and update the values as needed.
    ```bash
    cp .env.example .env
    ```
    Key variables to configure include:
    *   `SBI_SHINSEI_BANK_ID`, `SBI_SHINSEI_BANK_PASSWORD`
    *   `SUMISHIN_SBI_BANK_USER_NAME`, `SUMISHIN_SBI_BANK_PASSWORD`
    *   `RAKUTEN_BANK_ID`, `RAKUTEN_BANK_PASSWORD`, `RAKUTEN_BRANCH_NUMBER`, `RAKUTEN_ACCOUNT_NUMBER`, `RAKUTEN_SECRET1_QUESTION`, `RAKUTEN_SECRET1_WORD`, etc.
    *   `MITSUISUMITOMO_BANK_BRANCH_NUMBER`, `MITSUISUMITOMO_BANK_ACCOUNT_NUMBER`, `MITSUISUMITOMO_BANK_PASSWORD`
    *   `SBI_BENEFIT_SYSTEMS_ID`, `SBI_BENEFIT_SYSTEMS_PASSWORD`
    *   `SBI_SECURITIES_ID`, `SBI_SECURITIES_PASSWORD`
    *   `MITSUISUMITOMO_CARD_ID`, `MITSUISUMITOMO_CARD_PASSWORD`
    *   (It is also assumed that `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB` and `ENCRYPTION_KEY` will be needed, although not present in the example file, these are common for such applications.)


3.  **Build and Run with Docker Compose:**
    (Ensure Docker and Docker Compose are installed)
    ```bash
    docker-compose up --build -d
    ```
    This command will build the Docker images and start the backend server, frontend application, and the database.

4.  **Database Migrations:**
    Once the containers are running, apply the database migrations:
    ```bash
    docker-compose exec backend alembic upgrade head
    ```

5.  **Access the application:**
    *   Backend API will likely be available at `http://localhost:8000` (or as configured in `compose.yaml`).
    *   Frontend application will likely be available at `http://localhost:9000` (or as configured in `compose.yaml`).

## Supported Financial Institutions

The application supports data aggregation from the following institutions (based on repository and service names):

*   Mitsui Sumitomo Bank
*   Mitsui Sumitomo Card
*   Rakuten Bank
*   SBI Benefit System (likely for iDeCo or corporate DC pensions)
*   SBI Securities
*   SBI Shinsei Bank
*   Sumishin SBI Net Bank

## Project Structure Overview

*   `app/`: Contains the backend FastAPI application.
    *   `db/`: Database setup and SQLAlchemy models.
    *   `internal/`: Core logic like cryptography and logging.
    *   `repositories/`: Data access layer for each financial institution.
    *   `routers/`: API endpoint definitions.
    *   `services/`: Business logic for interacting with financial institutions.
    *   `use_cases/`: Higher-level application logic orchestrating services.
*   `frontend/`: Contains the React, Vite frontend application.
*   `migrations/`: Alembic database migration scripts.
*   `compose.yaml`: Docker Compose configuration for running the application stack.
*   `Dockerfile`: Docker configuration for the backend application.
*   `.env.example`: Example environment variables needed for the application.

## Development

(Placeholder for future development guidelines, testing instructions, etc. For example, how to run linters, formatters, or tests.)

## Contributing

(Placeholder for contribution guidelines.)

## License

This project is licensed under the Apache License 2.0.
See [LICENSE.md](LICENSE.md) for the full license text.
