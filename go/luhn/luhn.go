package luhn

func parseId(id string) string {
	var parsed string = ""
	for _, character := range id {
		if character == ' ' {
			continue
		}
		if character < '0' || character > '9' {
			return ""
		}
		parsed += string(character)
	}
	return parsed
}

// Prepare the digit to be calculated in the Luhn sum. Double, if greater than 9, subtract 9.
func prepareLuhnDigit(digit int) int {
	newDigit := digit * 2
	if newDigit > 9 {
		newDigit -= 9
	}
	return newDigit
}

func Valid(id string) bool {
	parsedId := parseId(id)
	if len(parsedId) < 2 {
		return false
	}

	sum := 0
	isSecond := false
	for index := len(parsedId) - 1; index >= 0; index-- {
		digit := int(parsedId[index] - '0')
		if isSecond {
			// the second digit should be processed
			sum += prepareLuhnDigit(digit)
		} else {
			// the first digit doesn't need doubling
			sum += digit
		}
		isSecond = !isSecond
	}

	return sum%10 == 0
}
