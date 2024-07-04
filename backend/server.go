package main

import (
	"log/slog"
	"net/http"

	"github.com/gorilla/mux"
)

type Server struct {
	address string
	logger  *slog.Logger
}

func NewServer(address string, logger *slog.Logger) *Server {
	return &Server{
		address: address,
		logger:  logger,
	}
}

func (s *Server) Start() error {
	r := mux.NewRouter()
	r.HandleFunc("/api/ping", s.handlePing).Methods("GET")

	http.Handle("/", r)

	s.logger.Info("server has been started", "address", s.address)

	err := http.ListenAndServe(s.address, nil)
	if err != http.ErrServerClosed {
		return err
	}

	return nil
}

func (s *Server) handlePing(w http.ResponseWriter, r *http.Request) {
	_, _ = w.Write([]byte("pupupu"))
}
