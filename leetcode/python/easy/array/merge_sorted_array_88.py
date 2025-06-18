def merge(nums1, m, nums2, n):
    nums2_idx = n - 1
    last_nums1_idx = m + n - 1
    nums1_idx = m - 1

    while nums2_idx >= 0:
        if nums1_idx >= 0 and nums2[nums2_idx] < nums1[nums1_idx]:
            nums1[last_nums1_idx] = nums1[nums1_idx]
            nums1_idx -= 1
        else:
            nums1[last_nums1_idx] = nums2[nums2_idx]
            nums2_idx -= 1
        last_nums1_idx -= 1

    print(nums1)