package isbnverifier

func IsValidISBN(isbn string) bool {
	position := 1
	sum := 0
	for index := len(isbn) - 1; index >= 0; index-- {
		char := isbn[index]
		digit := 0

		// hyphens are tolerated
		if char == '-' {
			continue
		}

		if position == 1 && char == 'X' {
			// X is only tolerated as the last digit
			digit = 10
		} else if char >= '0' && char <= '9' {
			digit = int(char - '0')
		} else {
			// non-digits are not tolerated
			return false
		}

		sum += position * digit
		position++
	}
	return position == 11 && sum%11 == 0
}
