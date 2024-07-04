package main

import (
	"log/slog"
	"net/http"
	"text/template"

	"github.com/gorilla/mux"
)

var tpl = template.Must(template.ParseFiles("./frontend/index.html"))

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

	r.HandleFunc("/api/ping", s.HandlePing).Methods("GET")
	r.HandleFunc("/api/homepage", s.HomePage).Methods("GET")

	http.Handle("/static/", http.StripPrefix("/static/", http.FileServer(http.Dir("frontend/assets"))))
	http.Handle("/", r)

	s.logger.Info("server has been started", "address", s.address)

	err := http.ListenAndServe(s.address, nil)
	if err != http.ErrServerClosed {
		return err
	}

	return nil
}

func (s *Server) HandlePing(w http.ResponseWriter, r *http.Request) {
	_, _ = w.Write([]byte("pupupu"))
}

func (s *Server) HomePage(w http.ResponseWriter, r *http.Request) {
	tpl.Execute(w, nil)
}
