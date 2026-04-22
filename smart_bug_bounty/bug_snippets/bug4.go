package main

import (
    "fmt"
    "sync"
    "time"
)

func processTasks() {
    var wg sync.WaitGroup
    tasks := []string{"Task_A", "Task_B", "Task_C", "Task_D"}

    fmt.Println("Starting background workers...")
    
    for _, t := range tasks {
        wg.Add(1)
        // BUG: capturing loop variable 't' by reference
        go func() {
            defer wg.Done()
            time.Sleep(10 * time.Millisecond)
            fmt.Println("Processed:", t)
        }()
    }
    
    wg.Wait()
    fmt.Println("All workers finished.")
}

func main() {
    processTasks()
}
