package main

import "fmt"

func merge(nums1 []int, m int, nums2 []int, n int) {
	nums2Idx := n - 1
	lastNums1Idx := m + n - 1
	for nums1Idx := m - 1; nums2Idx >= 0; lastNums1Idx-- {
		if nums1Idx >= 0 && nums2[nums2Idx] < nums1[nums1Idx] {
			nums1[lastNums1Idx] = nums1[nums1Idx]
			nums1Idx--
		} else {
			nums1[lastNums1Idx] = nums2[nums2Idx]
			nums2Idx--
		}
	}
	fmt.Println(nums1)
}

func merge2(nums1 []int, m int, nums2 []int, n int) {
	p1 := m - 1
	p2 := n - 1
	end := m + n - 1

	for p1 >= 0 && p2 >= 0 {
		if nums1[p1] > nums2[p2] {
			nums1[end] = nums1[p1]
			p1--
		} else {
			nums1[end] = nums2[p2]
			p2--
		}
		end--
	}

	for p2 >= 0 {
		nums1[end] = nums2[p2]
		end--
		p2--
	}
}

func main() {
	merge([]int{1, 2, 3, 0, 0, 0}, 3, []int{2, 5, 6}, 3)
}
