package database

import (
	"database/sql"
	"time"

	_ "github.com/lib/pq"
)

func New() (*sql.DB, error) {
	db, err := sql.Open("postgres", "host=127.0.0.1 port=5432 user=root password=test database=default sslmode=disable")
	if err != nil {
		return nil, err
	}

	db.SetMaxIdleConns(10)
	db.SetConnMaxIdleTime(1 * time.Minute)
	db.SetConnMaxLifetime(1 * time.Minute)

	return db, err
}
