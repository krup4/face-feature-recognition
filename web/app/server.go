package main

import (
	"bytes"
	"fmt"
	"io"
	"log/slog"
	"net/http"
	"text/template"
	"encoding/json"

	"github.com/gorilla/mux"
)

var home = template.Must(template.ParseFiles("./index.html"))

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
	r.HandleFunc("/", s.HomePage).Methods("GET")
	r.HandleFunc("/api/getInfo", s.GetInfo).Methods("POST")

	http.Handle("/static/", http.StripPrefix("/static/", http.FileServer(http.Dir("static"))))
	http.Handle("/src/", http.StripPrefix("/src/", http.FileServer(http.Dir("src"))))
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

func (s *Server) GetInfo(w http.ResponseWriter, r *http.Request) {
	file, _, err := r.FormFile("image")
	if err != nil {
		fmt.Println("File not found: ", err)
		return
	}
	defer file.Close()

	data, err := io.ReadAll(file)
	if err != nil {
		fmt.Println("Error in reading: ", err)
		return
	}

	body := bytes.NewReader(data)

	req, err := http.NewRequest("POST", "http://model:5050/analysis-frame", body)
	if err != nil {
		fmt.Println("Ошибка при создании запроса:", err)
		return
	}

	req.Header.Set("Content-Type", "image/jpeg") 

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		fmt.Println("Ошибка при отправке запроса:", err)
		return
	}
	defer resp.Body.Close()

	answ, err := io.ReadAll(resp.Body)
	if err != nil {
		fmt.Println("Ошибка при чтении тела ответа:", err)
		return
	}

	w.WriteHeader(http.StatusOK)
	w.Header().Set("Content-Type", "application/json; charset=utf-8")
	w.Header().Set("Access-Control-Allow-Origin", "*")
	json.NewEncoder(w).Encode(answ)
}
