package main

import (
	"log/slog"
)

func main() {
	logger := slog.Default()

	s := NewServer("localhost:8080", logger)

	err := s.Start()

	if err != nil {
		logger.Error("server has been stopped", "error", err)
	}
}
