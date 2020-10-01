from typing import List

def moveZeroes(nums: List[int]) -> None:

    """
    Do not return anything, modify nums in-place instead.
    """

    positionzero = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[positionzero] = nums[positionzero], nums[i]
            positionzero += 1


if __name__ == '__main__':

    lst = [0, 1, 0, 3, 12]
    print(f'Unmodified list {lst}')
    print(moveZeroes(lst))
    print(moveZeroes([0, 0, 1]))
    print(f'Modified list in-place {lst}')
