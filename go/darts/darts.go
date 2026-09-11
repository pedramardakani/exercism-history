package darts

func Score(x float64, y float64) int {
	zSquared := x*x + y*y
	if zSquared > 100 {
		return 0
	} else if zSquared > 25 {
		return 1
	} else if zSquared > 1 {
		return 5
	} else {
		return 10
	}
}
