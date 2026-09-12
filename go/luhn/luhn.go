package luhn

// prepareLuhnDigit - Prepare the digit to be calculated in the Luhn sum.
func prepareLuhnDigit(digit int) int {
	newDigit := digit * 2
	if newDigit > 9 {
		newDigit -= 9
	}
	return newDigit
}

func Valid(id string) bool {
	sum := 0
	position := 0
	for index := len(id) - 1; index >= 0; index-- {
		char := id[index]
		if char == ' ' {
			continue
		}
		if char < '0' || char > '9' {
			return false
		}
		digit := int(char - '0')
		if position%2 == 0 {
			sum += digit
		} else {
			sum += prepareLuhnDigit(digit)
		}
		position++
	}

	// single digits are invalid
	return position > 1 && sum%10 == 0
}
