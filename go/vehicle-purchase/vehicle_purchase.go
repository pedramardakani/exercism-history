package purchase

import "slices"

// NeedsLicense determines whether a license is needed to drive a type of vehicle. Only "car" and "truck" require a license.
func NeedsLicense(kind string) bool {
	licensedVehicles := []string{"car", "truck"}
	index := slices.Index(licensedVehicles, kind)
	return index != -1
}

// ChooseVehicle recommends a vehicle for selection. It always recommends the vehicle that comes first in lexicographical order.
func ChooseVehicle(option1, option2 string) string {
	choice := option2
	if option1 < option2 {
		choice = option1
	}
	return choice + " is clearly the better choice."
}

// CalculateResellPrice calculates how much a vehicle can resell for at a certain age.
func CalculateResellPrice(originalPrice, age float64) float64 {
	factor := 0.0
	if age >= 10 {
		factor = 0.5
	} else if age >= 3 {
		factor = 0.7
	} else {
		factor = 0.8
	}
	return originalPrice * factor
}
