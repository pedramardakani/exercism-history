package collatzconjecture

import "fmt"

func CollatzConjecture(n int) (int, error) {
	if n < 1 {
		return 0, fmt.Errorf("expected positive integer, received '%d'", n)
	}
	cur := n
	step := 0
	for cur != 1 {
		step += 1
		if cur%2 == 0 {
			cur /= 2
		} else {
			cur = cur*3 + 1
		}
	}
	return step, nil
}
