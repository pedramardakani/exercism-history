package twofer

import "fmt"

func ShareWith(name string) string {
	var resolvedName string
	if name != "" {
		resolvedName = name
	} else {
		resolvedName = "you"
	}
	return fmt.Sprint("One for ", resolvedName, ", one for me.")
}
