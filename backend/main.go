package main

import (
	"log/slog"
)

func main() {
	logger := slog.Default()

	var s Server
	s.address = "localhost:8080"
	s.logger = logger

	err := s.Start()

	if err != nil {
		logger.Error("server has been stopped", "error", err)
	}
}
