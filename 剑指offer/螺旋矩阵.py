class Solution:
    # @param {int[][]} matrix a matrix of m x n elements
    # @return {int[]} an integer array

    answ = [709, 873, 272, 847, 284, 487, 669, 958, 922, 399, 38, 648, 664, 982, 564, 308, 359, 357, 592, 618, 790, 835,
            664, 203, 338, 632, 762, 845, 917, 113, 384, 754, 451, 291, 343, 139, 579, 945, 641, 595, 759, 419, 154,
            454,
            671, 599, 641, 917, 288, 576, 198, 141, 763, 592, 289, 888, 463, 907, 310, 410, 586, 289, 822, 140, 90, 561,
            839, 754, 494, 989, 694, 350, 717, 850, 855, 628, 210, 111, 228, 771, 80, 21, 715, 152, 486, 688, 109, 722,
            648, 821, 299, 173, 327, 248, 38, 450, 327, 538, 688, 474, 910, 957, 599, 978, 915, 408, 307, 270, 152, 548,
            517, 411, 478, 134, 774, 452, 669, 226, 346, 233, 925, 879, 181, 751, 938, 18, 519, 527, 534, 822, 23, 227,
            149, 159, 422, 566, 627, 50, 70, 98, 646, 605, 132, 282, 907, 598, 606, 499, 889, 206, 242, 105, 801, 444,
            209, 124, 109, 603, 200, 137, 193, 216, 98, 509, 487, 303, 594, 951, 424, 63, 239, 736, 368, 975, 797, 808,
            209, 878, 545, 154, 169, 452, 446, 412, 815, 666, 12, 47, 82, 822, 894, 518, 861, 838, 268, 597, 903, 939,
            118, 526, 446, 395, 628, 697, 24, 674, 862, 770, 988, 934, 955, 832, 991, 749, 804, 35, 794, 154, 902, 889,
            181, 468, 186, 291, 304, 53, 272, 218, 104, 193, 375, 915, 438, 362, 960, 208, 579, 397, 125, 549, 705, 942,
            188, 702, 169, 352, 553, 469, 816, 323, 145, 453, 114, 360, 315, 499, 37, 84, 78, 313, 676, 63, 161, 348,
            923, 958, 931, 300, 971, 39, 333, 288, 160, 185, 74, 175, 974, 565, 143, 598, 415, 595, 906, 498, 520, 337,
            340, 821, 668, 841, 292, 494, 495, 140, 112, 824, 260, 309, 950, 944, 773, 965, 248, 376, 901, 926, 98, 185,
            180, 259, 648, 454, 182, 847, 891, 319, 562, 220, 222, 619, 730, 808, 198, 770, 53, 206, 612, 64, 906, 793,
            32, 196, 439, 870, 144, 326, 230, 864, 686, 344, 821, 176, 82, 308, 879, 837, 409, 856, 763, 251, 622, 444,
            583, 71, 746, 448, 556, 857, 522, 741, 306, 540, 711, 167, 353, 478, 509, 192, 455, 195, 824, 978, 49, 71,
            661, 367, 967, 109, 741, 720, 694, 233, 985, 999, 361, 905, 975, 910, 616, 991, 584, 838, 276, 888, 590,
            541,
            862, 10, 157, 923, 833, 629, 124, 106, 318, 396, 417, 772, 832, 428, 716, 368, 690, 209, 539, 29, 103, 671,
            308, 544, 294, 745, 398, 829, 735, 22, 982, 196, 109, 221, 182, 479, 730, 290, 917, 401, 930, 855, 645, 271,
            357, 157, 885, 129, 105, 919, 567, 625, 51, 116, 654, 526, 818, 380, 474, 282, 951, 841, 921, 404, 620, 43,
            971, 550, 30, 950, 648, 128, 29, 169, 1000, 145, 777, 280, 610, 251, 749, 168, 109, 501, 176, 435, 922, 406,
            278, 494, 673, 189, 717, 469, 374, 852, 22, 787, 513, 471, 836, 404, 819, 631]
    ans = []
    # matrix = [
    #     [1, 2, 3, 11],
    #     [4, 5, 6, 12],
    #     [7, 8, 9, 13],
    #     [14, 15, 16, 17]
    # ]
    matrix = [
        [709, 873, 272, 847, 284, 487, 669, 958, 922, 399, 38, 648, 664, 982, 564, 308, 359, 357, 592, 618],
        [688, 109, 722, 648, 821, 299, 173, 327, 248, 38, 450, 327, 538, 688, 474, 910, 957, 599, 978, 790],
        [486, 509, 487, 303, 594, 951, 424, 63, 239, 736, 368, 975, 797, 808, 209, 878, 545, 154, 915, 835],
        [152, 98, 362, 960, 208, 579, 397, 125, 549, 705, 942, 188, 702, 169, 352, 553, 469, 169, 408, 664],
        [715, 216, 438, 824, 260, 309, 950, 944, 773, 965, 248, 376, 901, 926, 98, 185, 816, 452, 307, 203],
        [21, 193, 915, 112, 251, 622, 444, 583, 71, 746, 448, 556, 857, 522, 741, 180, 323, 446, 270, 338],
        [80, 137, 375, 140, 763, 541, 862, 10, 157, 923, 833, 629, 124, 106, 306, 259, 145, 412, 152, 632],
        [771, 200, 193, 495, 856, 590, 290, 917, 401, 930, 855, 645, 271, 318, 540, 648, 453, 815, 548, 762],
        [228, 603, 104, 494, 409, 888, 730, 550, 30, 950, 648, 128, 357, 396, 711, 454, 114, 666, 517, 845],
        [111, 109, 218, 292, 837, 276, 479, 971, 494, 673, 189, 29, 157, 417, 167, 182, 360, 12, 411, 917],
        [210, 124, 272, 841, 879, 838, 182, 43, 278, 631, 717, 169, 885, 772, 353, 847, 315, 47, 478, 113],
        [628, 209, 53, 668, 308, 584, 221, 620, 406, 819, 469, 1000, 129, 832, 478, 891, 499, 82, 134, 384],
        [855, 444, 304, 821, 82, 991, 109, 404, 922, 404, 374, 145, 105, 428, 509, 319, 37, 822, 774, 754],
        [850, 801, 291, 340, 176, 616, 196, 921, 435, 836, 852, 777, 919, 716, 192, 562, 84, 894, 452, 451],
        [717, 105, 186, 337, 821, 910, 982, 841, 176, 471, 22, 280, 567, 368, 455, 220, 78, 518, 669, 291],
        [350, 242, 468, 520, 344, 975, 22, 951, 501, 513, 787, 610, 625, 690, 195, 222, 313, 861, 226, 343],
        [694, 206, 181, 498, 686, 905, 735, 282, 109, 168, 749, 251, 51, 209, 824, 619, 676, 838, 346, 139],
        [989, 889, 889, 906, 864, 361, 829, 474, 380, 818, 526, 654, 116, 539, 978, 730, 63, 268, 233, 579],
        [494, 499, 902, 595, 230, 999, 398, 745, 294, 544, 308, 671, 103, 29, 49, 808, 161, 597, 925, 945],
        [754, 606, 154, 415, 326, 985, 233, 694, 720, 741, 109, 967, 367, 661, 71, 198, 348, 903, 879, 641],
        [839, 598, 794, 598, 144, 870, 439, 196, 32, 793, 906, 64, 612, 206, 53, 770, 923, 939, 181, 595],
        [561, 907, 35, 143, 565, 974, 175, 74, 185, 160, 288, 333, 39, 971, 300, 931, 958, 118, 751, 759],
        [90, 282, 804, 749, 991, 832, 955, 934, 988, 770, 862, 674, 24, 697, 628, 395, 446, 526, 938, 419],
        [140, 132, 605, 646, 98, 70, 50, 627, 566, 422, 159, 149, 227, 23, 822, 534, 527, 519, 18, 154],
        [822, 289, 586, 410, 310, 907, 463, 888, 289, 592, 763, 141, 198, 576, 288, 917, 641, 599, 671, 454]
    ]

    def spiralOrder(self, matrix):
        i = 1
        while self.matrix:
            self.so()
            tl = len(self.ans)
            print(i, ',', self.ans == self.answ[:tl])
            i += 1
        return self.ans

    def so(self):
        # 上
        if self.matrix:
            row = self.matrix[0][::]
            if row:
                self.ans.extend(row)
                self.matrix.remove(row)

        # 右
        if self.matrix:
            right = []
            cl = len(self.matrix[0]) - 1  # 列长度
            for i in range(len(self.matrix)):
                if self.matrix[i]:
                    val = self.matrix[i][cl]
                    right.append(val)  # 取出右边的元素
                    self.matrix[i].pop(cl)
            if right:
                self.ans.extend(right)

        # 下
        if self.matrix:
            rl = len(self.matrix) - 1
            bottom = self.matrix[rl]
            if bottom:
                rv_b = bottom[::-1]
                self.ans.extend(rv_b)
            self.matrix.remove(bottom)

        # 左
        if self.matrix:
            left = []
            for i in range(len(self.matrix)):
                if self.matrix[i]:
                    val = self.matrix[i][0]
                    left.insert(0, val)
                    self.matrix[i].pop(0)
            if left:
                self.ans.extend(left)

    def show_ans(self):
        print(self.ans)


arr = []
so = Solution()
so.spiralOrder(arr)

so.show_ans()
