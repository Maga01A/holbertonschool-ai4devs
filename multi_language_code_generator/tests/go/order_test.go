package main

import (
    "testing"
    "multi_language_code_generator/implementations/go" // Go modulu t?l?b oluna bil?r
)

func TestProcessOrder(t *testing.T) {
    result := ProcessOrder("Laptop", 1200, 2)
    if result.Total != 2400 {
        t.Errorf("Expected 2400, got %f", result.Total)
    }
    if result.Status != "Processed" {
        t.Errorf("Expected Processed, got %s", result.Status)
    }
}
