package main

import "fmt"

func removeElement(nums []int, val int) int {
	i := 0
	end := len(nums) - 1

	for i <= end {
		if nums[i] == val {
			nums[i] = nums[end]
			end--
		} else {
			i++
		}
	}
	return end + 1
}

func main() {
	fmt.Println(removeElement([]int{3, 2, 2, 3}, 3))
}
