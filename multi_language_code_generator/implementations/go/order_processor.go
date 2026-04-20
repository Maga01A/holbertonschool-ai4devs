package main

import "fmt"

type OrderResponse struct {
    Item   string  json:"item"
    Total  float64 json:"total"
    Status string  json:"status"
}

func ProcessOrder(item string, price float64, quantity int) OrderResponse {
    total := price * float64(quantity)
    status := "Invalid"
    if total > 0 {
        status = "Processed"
    }
    return OrderResponse{Item: item, Total: total, Status: status}
}

func main() {
    fmt.Printf("%+v\n", ProcessOrder("Laptop", 1200, 2))
}
