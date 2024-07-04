package main

import (
	"log/slog"
	"net/http"
	"text/template"

	"github.com/gorilla/mux"
)

var home = template.Must(template.ParseFiles("./frontend/index.html"))
var second = template.Must(template.ParseFiles("./frontend/second_page.html"))

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
	r.HandleFunc("/homepage", s.HomePage).Methods("GET")
	r.HandleFunc("/secondpage", s.SecondPage).Methods("GET")

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
	home.Execute(w, nil)
}

func (s *Server) SecondPage(w http.ResponseWriter, r *http.Request) {
	second.Execute(w, nil)
}
