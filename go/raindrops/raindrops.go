package raindrops

import "fmt"

type RainSound struct {
	num int
	sound string
}

// Array items must stay sorted by "num"
var rainSoundArray = [3]RainSound{
	{num: 3, sound: "Pling"},
	{num: 5, sound: "Plang"},
	{num: 7, sound: "Plong"},
}

func Convert(number int) string {
	var sound string = ""

	for _, item := range rainSoundArray {
		if number % item.num == 0 {
			sound += item.sound
		}
	}
	if sound == "" {
		sound = fmt.Sprintf("%d", number)
	}
	return sound
}
