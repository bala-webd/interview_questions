def version_finder(v1=None, v2=None):
    if not isinstance(v1, str):
        return "Version 1 is not in valid format"
    if not isinstance(v2, str):
        return "Version 2 is not in valid format"
    v1_parts = v1.split('.')
    v2_parts = v2.split('.')

    nums = get_version_list(v1_parts)
    nums2 = get_version_list(v2_parts)

    list_range_finder = len(nums) if len(nums) > len(nums2) else len(nums2)
    result = "Equal"
    for index in range(list_range_finder):
        try:
            if nums[index] > nums2[index]:
                result = "Downgraded"
                break
            elif nums[index] < nums2[index]:
                result = "Upgraded"
                break
        except:
            if len(nums) > len(nums2):
                result = "Downgraded"
            elif len(nums2) > len(nums):
                result = "Upgraded"
            continue
    print("result", result)
    return result


def get_version_list(parts):
    whole_version = []
    for part in parts:
        try:
            whole_version.append(int(part))
        except:
            pass
    return whole_version

version_finder(v1="5", v2="4.0.1")