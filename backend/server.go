package main

import (
	"fmt"
	"io"
	"log/slog"
	"net/http"
	"os"
	"text/template"

	"github.com/gorilla/mux"
)

var home = template.Must(template.ParseFiles("./frontend/index.html"))
var second = template.Must(template.ParseFiles("./frontend/view-video.html"))

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
	r.HandleFunc("/secondpage", s.SecondPage).Methods("POST")

	http.Handle("/static/", http.StripPrefix("/static/", http.FileServer(http.Dir("frontend/static"))))
	http.Handle("/src/", http.StripPrefix("/src/", http.FileServer(http.Dir("frontend/src"))))
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
	file, handler, err := r.FormFile("video")
	if err != nil {
		fmt.Println("Error with reading video: ", err)
		return
	}

	defer file.Close()

	filename := handler.Filename
	dst, err := os.Create(fmt.Sprintf("../%s", filename))
	if err != nil {
		fmt.Println("Error with creating new file: ", err)
		return
	}
	defer dst.Close()

	if _, err := io.Copy(dst, file); err != nil {
		fmt.Println("Error with copying file: ", err)
		return
	}

	fmt.Println("Success")
	second.Execute(w, nil)
}
