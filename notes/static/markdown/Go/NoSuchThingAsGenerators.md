# Go doesn't have Generators

Instead, using a combination of channels and goroutines to achieve a similar affect.

# Example

```Go
package main

import (
	"fmt"
)

func main () {
	fib := go_fib(70)
	for num := range fib {
		fmt.Printf("The next Fib number is %d\n", num)
	}
}


func go_fib(i int) chan int {
	c := make(chan int) // Create a channel

	go func() {
		a, b := 1, 1 // Set the 1st two terms

		for k :=0; k < i; k++ {
			c <- a // "yield" a to the channel

			// generate next term
			a, b = b, a+b
		}
		close(c) // Close a channel
	}()

	return c

}
```

# Breakdown

### Boring Basics

```Go
package main

import (
	"fmt"
)
```

This section of code declares that the file is part of the main package.
Next we import `fmt`, this is the Go standard library's string formatting tool.

### Func Go Fib

```Go
func go_fib(i int) chan int {
	c := make(chan int) // Create a channel

	go func() {
		...
	}()

	return c

}
```

This function takes an integer, and returns a channel of integers. In very basic terms a
channel is a queue that can be passed between concurrent goroutines.

### The Anonymous Function

This anonymous function is a goroutine so that the outer function can return the channel while
the inner anon function is still calculating values.

```Go
	go func() {
		a, b := 1, 1 // Set the 1st two terms

		for k :=0; k < i; k++ {
			c <- a // "yield" a to the channel

			// generate next term
			a, b = b, a+b
		}
		close(c) // Close a channel
	}()
```

It starts with two integers, `a` and `b`, both set to one.
Then, using `i` from the outer scope, it creates a for loop.
Within the for loop we first add the value to the channel,
then generate the next term.

Assuming nothing is consuming the channel on the other end,
It could be modeled as such:

| `k` |    `c`     |
| :-: | :--------: |
|  0  |     1      |
|  1  |    1, 1    |
|  2  |  1, 1, 2   |
|  3  | 1, 1, 2, 3 |

Finally, once the for-loop completes the channel is closed. It is best practice to close
channels within the same function that creates them. This prevents memory leaks and infinite loops.

### The Main Function

```Go
func main () {
	fib := go_fib(70)
	for num := range fib {
		fmt.Printf("The next Fib number is %d\n", num)
	}
}
```

The `main` function in `package main` is the entry point for the application.
Here it first receives a channel from `go_fib`, it then consumes the channel within the for loop.
Printing each term using `fmt.Printf`.

The for loop will end when the channel is both closed and empty.

Even though we're using goroutines (the main function is a go routine too), the program still runs sequentially.
`main` still has to wait for the digits to be consumed. In fact, a sequential implementation is much faster (102,889 ns/op vs 62,092 ns/op).
