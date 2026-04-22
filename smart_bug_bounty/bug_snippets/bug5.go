package main

import (
    "fmt"
    "sync"
    "time"
)

func setupTasks() []string {
    // Helper function to initialize data
    return []string{"Task_A", "Task_B", "Task_C", "Task_D", "Task_E"}
}

func main() {
    var wg sync.WaitGroup
    tasks := setupTasks()
    
    fmt.Println("Initializing multi-threaded processing pool...")
    fmt.Println("Total tasks detected:", len(tasks))

    for _, task := range tasks {
        wg.Add(1)
        
        // BUG: loop variable 'task' is captured by reference in goroutine closure
        go func() {
            defer wg.Done()
            // Simulate heavy processing time
            time.Sleep(10 * time.Millisecond)
            fmt.Println("Successfully finished processing:", task)
        }()
    }
    
    wg.Wait()
    fmt.Println("All background jobs have been fully completed.")
}
