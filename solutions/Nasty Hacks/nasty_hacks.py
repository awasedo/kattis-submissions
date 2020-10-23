for i in range(int(input())):
    nums = list(map(int, input().split()))
    if nums[1]-nums[2] == nums[0]:
        print("does not matter")
    elif nums[1]-nums[2] > nums[0]:
        print("advertise")
    else:
        print("do not advertise")
