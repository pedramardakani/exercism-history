package twofer

import "fmt"

func ShareWith(name string) string {
	var resolvedName string
	if len(name) == 0 {
		resolvedName = "you"
	} else {
		resolvedName = name
	}
	return fmt.Sprint("One for ", resolvedName, ", one for me.")
}
