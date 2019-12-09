
class Solution:
    def get_range(self, arr, target):
        first = self.binary_search(arr, 0, len(arr) - 1, target, True)
        last = self.binary_search(arr, 0, len(arr) - 1, target, False)
        return [first, last]

    def binary_search(self, arr, start, end, target, find_first):
        """
        recursive method
        calculate mid point. (start + (end - start)) / 2
        if searching for the first index,
            compare mid and the one left to check if left is lower than mid.
        if searching for the last index,
            compare mid and the one right to check if left is lower than mid.
        if mid equal target, return mid index
        if mid is lower than target, recursively call with the right half.
        if mid is higher than target, recursively call with the left half.
        """
        if end < start: return -1
        mid = (start + (end - start)) / 2
        if find_first:
            if (mid == 0 or target > arr[mid - 1]) and arr[mid] == target:
                return mid
            if arr[mid] < target:
                return self.binary_search(arr, mid + 1, end, target, find_first)
            elif target < arr[mid]:
                return self.binary_search(arr, start, mid - 1, target, find_first)
        else:
            if (mid == len(arr) - 1 or target < arr[mid + 1]) and arr[mid] == target:
                return mid
            if arr[mid] < target:
                return self.binary_search(arr, mid + 1, end, target, find_first)
            elif target < arr[mid]:
                return self.binary_search(arr, start, mid - 1, target, find_first)
    
    def b_search(self, arr, start, end, t, first):
        """
        iterative method
        """
        while True:
            if end < start: return -1
            mid = (start + (end - start)) / 2
            if first:
                if (mid == 0 or t > arr[mid - 1]) and arr[mid] == t:
                    return mid
                if arr[mid] < t:
                    start = mid + 1
                elif t < arr[mid]:
                    end = mid - 1
            else:
                if (mid == len(arr) - 1 or t < arr[mid + 1]) and arr[mid] == t:
                    return mid
                if arr[mid] < t:
                    start = mid + 1
                elif t < arr[mid]:
                    end = mid - 1


arr = [1, 3, 3, 5, 7, 8, 9, 9, 15]
print(Solution().get_range(arr, 9))
