package luhn

import "fmt"

// normalizeStringOfDigits - Normalize a string of digits, return empty string if invalid
func normalizeStringOfDigits(id string) ([]int, error) {
	parsed := make([]int, 0)
	for _, character := range id {
		// empty whitespace is tolerated
		if character == ' ' {
			continue
		}
		// non-digit characters are not tolerated
		if character < '0' || character > '9' {
			return nil, fmt.Errorf("Expected digits, received '%c'", character)
		}
		parsed = append(parsed, int(character-'0'))
	}

	if nDigits := len(parsed); nDigits <= 1 {
		return nil, fmt.Errorf("At least two digits expected, received '%d'", nDigits)
	}

	return parsed, nil
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
	parsedId, err := normalizeStringOfDigits(id)
	if err != nil {
		return false
	}

	nDigits := len(parsedId)
	sum := 0
	for index, digit := range parsedId {
		isSecond := (nDigits-index)%2 == 0
		if isSecond {
			// the second digit should be processed
			sum += prepareLuhnDigit(digit)
		} else {
			// the first digit doesn't need doubling
			sum += digit
		}
	}

	return sum%10 == 0
}
