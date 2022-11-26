package main

import "fmt"

func increment() func() {
    num := 0
    return func() {
        num = num + 1
        fmt.Printf("num : %d\n",num)
    }
}

func main() {
     inc := increment()
     inc()
     inc()
     inc()
}
