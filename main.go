package main

import (
	"log"
	"net/http"

	"github.com/tshiba06/alterna/database"
)

func main() {
	db, err := database.New()
	if err != nil {
		log.Fatal(err)
	}
	defer db.Close()

	log.Println("test")

	server := http.Server{
		Addr:    "0.0.0.0:18080",
		Handler: nil,
	}

	if err := server.ListenAndServe(); err != nil {
		log.Fatal(err)
	}
}
