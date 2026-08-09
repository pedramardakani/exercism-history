package cars

// CalculateWorkingCarsPerHour calculates how many working cars are
// produced by the assembly line every hour.
func CalculateWorkingCarsPerHour(productionRatePerHour int, successRate float64) float64 {
	return float64(productionRatePerHour) * successRate / 100
}

// CalculateWorkingCarsPerMinute calculates how many working cars are
// produced by the assembly line every minute.
func CalculateWorkingCarsPerMinute(productionRatePerHour int, successRate float64) int {
	result := (successRate / 100) * float64(productionRatePerHour) / 60 
	return int(result)
}

// CalculateCost works out the cost of producing the given number of cars.
func CalculateCost(carsCount int) uint {
	groupsOfTen := carsCount / 10
	remainder := carsCount % 10
	cost := groupsOfTen * 95000 + remainder * 10000
	return uint(cost)
}
