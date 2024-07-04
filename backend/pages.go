package main

type Page struct {
	Path string
	Body []byte
}

// func loadPage(path string) (*Page, error) {
// 	file, err := os.Open(path)
// 	if err != nil {
// 		fmt.Println("Error opening file:", err)
// 		return nil, err
// 	}
// 	defer file.Close()

// 	data, err := io.ReadAll(file)

// 	if err != nil {
// 		fmt.Println("Error reading file:", err)
// 		return nil, err
// 	}
// 	return &Page{Path: path, Body: data}, nil
// }
