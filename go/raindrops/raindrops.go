package raindrops

import "fmt"

var soundMap = map[int]string{
	3: "Pling",
	5: "Plang",
	7: "Plong",
}

func Convert(number int) string {
	var sound string = ""

	// DO NOT DO THIS!
	// Iteration order over a map is not guaranteed to be deterministic!
	// https://go.dev/blog/maps#iteration-order
	for k, v := range soundMap {
		if number%k == 0 {
			sound += v
		}
	}
	if sound == "" {
		sound = fmt.Sprintf("%d", number)
	}
	return sound
}
