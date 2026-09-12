package phonenumber

import (
	"fmt"
	"strings"
)

func Number(phoneNumber string) (string, error) {
	acceptablePunctuation := "-.() "
	maxDigits := 10
	normalized := ""
	position := 0
	for index := len(phoneNumber) - 1; index >= 0; index-- {
		character := phoneNumber[index]
		if strings.Contains(acceptablePunctuation, string(character)) {
			continue
		}
		if position == maxDigits && (character == '+' || character == '1') {
			continue
		}
		if position >= maxDigits {
			return "", fmt.Errorf("Expected %d digits, received more", maxDigits)
		}
		if (position == 6 || position == 9) && character < '2' {
			return "", fmt.Errorf("Invalid Area code/Local number, got '%c'", character)
		}
		if character < '0' || character > '9' {
			return "", fmt.Errorf("Expected digits, received '%c'", character)
		}
		normalized = string(character) + normalized
		position++
	}
	if len(normalized) != maxDigits {
		return "", fmt.Errorf("Expected %d digits, received less", maxDigits)
	}
	return normalized, nil
}

func AreaCode(phoneNumber string) (string, error) {
	number, err := Number(phoneNumber)
	if err != nil {
		return "", err
	}
	return number[:3], nil
}

func Format(phoneNumber string) (string, error) {
	number, err := Number(phoneNumber)
	if err != nil {
		return "", err
	}
	return fmt.Sprintf("(%s) %s-%s", number[:3], number[3:6], number[6:]), nil
}
