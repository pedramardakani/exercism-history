package luhn

// normalizeStringOfDigits - Normalize a string of digits, return empty string if invalid
func normalizeStringOfDigits(id string) []int {
	parsed := make([]int, 0)
	for _, character := range id {
		// empty whitespace is tolerated
		if character == ' ' {
			continue
		}
		// non-digit characters are not tolerated
		if character < '0' || character > '9' {
			return nil
		}
		parsed = append(parsed, int(character-'0'))
	}
	return parsed
}

// prepareLuhnDigit - Prepare the digit to be calculated in the Luhn sum.
func prepareLuhnDigit(digit int) int {
	newDigit := digit * 2
	if newDigit > 9 {
		newDigit -= 9
	}
	return newDigit
}

func Valid(id string) bool {
	parsedId := normalizeStringOfDigits(id)
	nDigits := len(parsedId)
	if nDigits < 2 {
		return false
	}

	sum := 0
	for index := nDigits - 1; index >= 0; index-- {
		digit := parsedId[index]
		isSecond := (nDigits-index)%2 == 0
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
