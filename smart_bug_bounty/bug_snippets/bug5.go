package main
import ("fmt"; "sync")
func main() {
    var wg sync.WaitGroup
    tasks := []string{"A", "B", "C"}
    for _, task := range tasks {
        wg.Add(1)
        // BUG: loop variable 'task' is captured by reference
        go func() {
            fmt.Println("Processing", task)
            wg.Done()
        }()
    }
    wg.Wait()
}
