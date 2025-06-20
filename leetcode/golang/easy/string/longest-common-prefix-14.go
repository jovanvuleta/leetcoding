package main

import (
	"fmt"
	"math"
)

func longestCommonPrefix(strs []string) string {
	minVal := math.MaxInt

	for _, str := range strs {
		if len(str) < minVal {
			minVal = len(str)
		}
	}

	res := ""

	for i := 0; i < minVal; i++ {
		for _, str := range strs {
			if str[i] != strs[0][i] {
				return res
			}
		}
		res = res + string(strs[0][i])
	}
	return res
}

func main() {
	strs := []string{"flower", "flow", "flight"}
	fmt.Println(longestCommonPrefix(strs))
}
