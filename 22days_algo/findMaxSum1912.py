# cnt = int(input())
cnt = 7
# nums=[1,2,3,4,5,6,-7,8,9,10]
# nums = [34,2,3,10,-150,36,2]
nums = list(map(int,input().split()))
# maxNum = max(nums)
# group = 0
# while True:
#     group += 1
#     for i in range(len(nums)-group):
#         check = sum(nums[i:i+group+1])
#         # print(nums[i], nums[i+group])
#         if check > maxNum:
#             maxNum = check
#     if group == len(nums):
#         break
# print(maxNum)

psum = 0
ret = max(nums)
for i in range(cnt):
    print("nums[%s]"%(i),nums[i],", ",end="")
    psum = max(psum, 0) + nums[i]
    print("psum:", psum,", ", end="")
    ret = max(psum,ret)
    print("ret:",ret)

print(ret)


"""
int fastestMaxSum(const vector<int>& A) {
    int N = A.size(), ret = MIN, psum = 0;
    for(int i = 0; i < N; ++i) {
        psum = max(psum, 0) + A[i];
        ret = max(psum, ret);
    }
    return ret;
}
"""