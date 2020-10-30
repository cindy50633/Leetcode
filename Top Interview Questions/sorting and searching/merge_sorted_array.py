def merge(nums1, m, nums2, n):
    """merge two sorted lists by merge sort strategy"""
    result = []
    nums1 = nums1[:m]

    while nums1 and nums2:
        if nums1[0] <= nums2[0]:
            result.append(nums1.pop(0))
        else:
            result.append(nums2.pop(0))
    result.extend(nums1)
    result.extend(nums2)

    return result

# print(merge([1,2,3,0,0,0], 3, [2,5,6], 3))
merge([1,2,3,0,0,0], 3, [2,5,6], 3)

def merge_inplace(nums1, m, nums2, n):
    """merge two sorted lists by merge sort strategy"""
    current_index_nums2 = 0
    nums2.append(float('inf'))
    temp_queue = []

    for i in range(m+n):
        if not temp_queue:
            if i >= m:
                nums1[i] = nums2[current_index_nums2]
                current_index_nums2 += 1
                continue
            if nums1[i] <= nums2[current_index_nums2]:
                continue
            else:
                temp_queue.append(nums1[i])
                nums1[i] = nums2[current_index_nums2]
                current_index_nums2 += 1
        else:
            if i < m:
                temp_queue.append(nums1[i])
            if temp_queue[0] <= nums2[current_index_nums2]:
                nums1[i] = temp_queue.pop(0)
            else:
                nums1[i] = nums2[current_index_nums2]
                current_index_nums2 += 1

    return nums1

# print(merge([1,2,3,0,0,0], 3, [2,5,6], 3))
# merge([1,2,3,0,0,0], 3, [2,5,6], 3)
print(merge_inplace([0,0,3,0,0,0,0,0,0], 3, [-1,1,1,1,2,3], 6))
