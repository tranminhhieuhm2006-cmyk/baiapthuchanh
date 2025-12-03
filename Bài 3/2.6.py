
print('ho ten: Tran Minh Hieu; mssv245752021610155')

def get_sum(*nums):
    tmp = 0
    # Duyet qua cac tham so duoc truyen vao ham
    for i in nums:
        tmp +=i
    return tmp

result = get_sum(7,8,9,10)
print(result)

