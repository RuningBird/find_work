class record:
    def __init__(self, key=[1, 2, 3, 4, 5, 6]):
        self.key = [0]
        self.key.extend(key)

    def show_record(self):
        for each in self.key[1:]:
            print(each, end=' ')
        print('\n')

    # 直接插入排序
    def insert_sort(self):
        for i in range(2, self.key.__len__()):
            self.key[0] = self.key[i]
            j = i - 1

            while self.key[0] < self.key[j]:  # 寻找插入位置
                self.key[j + 1] = self.key[j]  # 后移
                j -= 1
            self.key[j + 1] = self.key[0]

    # 折半插入排序
    def binary_sort(self):
        for i in range(2, self.key.__len__()):
            self.key[0] = self.key[i]  # 监视哨存放待插入的元素

            left = 1
            right = i - 1
            # mid = (left + right) // 2

            while left <= right:  # 寻找插入位置
                mid = (left + right) // 2
                if self.key[0] < self.key[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            for j in range(left, i)[::-1]: # 移动元素
                self.key[j + 1] = self.key[j]

            # while版本移动元素位置
            # j = i - 1
            # while j >= left:
            #     self.key[j + 1] = self.key[j]
            #     j -= 1

            self.key[left] = self.key[0]


obj = record([2, 1, 3])
obj.binary_sort()
obj.show_record()
