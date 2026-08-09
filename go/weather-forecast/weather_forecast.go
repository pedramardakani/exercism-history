// Package weather creates a string representation of the current weather forecast.
package weather

var (
	// CurrentCondition is a string telling the current weather condition.
	CurrentCondition string
	// CurrentLocation is a string telling you where this information belongs to.
	CurrentLocation  string
)

// Forecast takes the city and current condition and returns a readable string for the teleprompter.
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
