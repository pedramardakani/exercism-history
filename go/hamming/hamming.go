package hamming

import "errors"

func Distance(a, b string) (int, error) {
	if len(a) != len(b) {
		return 0, errors.New("DNA strands must have equal length")
	}
	difference := 0
	for index, _ := range a {
		if a[index] != b[index] {
			difference++
		}
	}
	return difference, nil
}
