package leap

func IsLeapYear(year int) bool {
	// add an extra day every 4 years
	if year%4 == 0 {
		// but this becomes 1 day too fast for each 100 years
		if year%100 == 0 {
			// address the error of one day in every 400 years
			if year%400 == 0 {
				return true
			}
			return false
		}
		return true
	}
	return false
}
