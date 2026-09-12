package luhn

import "fmt"

func parseId(id string) (string, error) {
	var parsed string = ""
	for _, character := range id {
		if character == ' ' {
			continue
		}
		if character < '0' || character > '9' {
			return "", fmt.Errorf("Expected digits, received '%v'", character)
		}
		parsed += string(character)
	}
	return parsed, nil
}

// Prepare the digit to be calculated in the Luhn sum. Double, if greater than 9, subtract 9.
func prepareLuhnDigit(digit int) int {
	newDigit := digit * 2
	if newDigit > 9 {
		return newDigit - 9
	}
	return newDigit
}

func Valid(id string) bool {
	parsedId, err := parseId(id)
	if err != nil || len(parsedId) < 2 {
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
