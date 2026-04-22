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
        // FIXED: Pass loop variable 't' as an argument to the goroutine
        go func(taskName string) {
            defer wg.Done()
            time.Sleep(10 * time.Millisecond)
            fmt.Println("Processed:", taskName)
        }(t)
    }
    
    wg.Wait()
    fmt.Println("All workers finished.")
}

func main() {
    processTasks()
}
