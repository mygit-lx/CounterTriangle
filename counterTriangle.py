# -*- coding: UTF-8 -*-

'''
picture is as follows:

   a*
    *  *  *
    * *  *    *
    *  *   *      *
    *   *    *        *
    *    *c    *d         * e
   b* * * * * * * * * * * * **
    *      *       *     *       *
    *       *        * f             *
    *        *   *     *                 *
    *         * g        *                   *
    *     *    *           *                     *
    *  *        *i           *j                      *k
   h* * * * * * * * * * * * * * * * * * * * * * * * * * **

Created on 2016年9月28日
Counter all the triangles in a picture
thinking:
其实，我觉得这个问题应该很简单，以一个程序员的思维我的解决方案如下：
1，自动生成任意三个点的所有组合；
2，看看任意两个点是不是在图中同一条线上，如果在进入第3步，不在的话说明这个组合不构不成三角形；
3，如果三个点全都在同一条直线上，构不成三角形，否则能够构成三角形。
OK，算法搞定，所有的工作这样就分成了两类：第一，找出所有最长边的点组合；第二，排列组合并判断。第一个是个体力活，稍微简单。第二个其实也简单，也就是一个迭代器的使用。
@author: luoxiang
'''

import itertools, string


def CounterTriangle():
    print "All the triangles we can find in the picture are as follows:"
    triangle_number = 0
    sides_match_list = ['abh', 'acgi', 'adfj', 'aek', 'bcde', 'efgh', 'hijk']
    dot_list = []
    i = 0
    while i < 26:
        dot_list.append(string.lowercase[i])
        if string.lowercase[i] == 'k':
            break
        else:
            i += 1

    for each_combination in itertools.combinations(dot_list, 3):
        triangle_flag = True
        for each_dot_combination in itertools.combinations(each_combination, 2):
            for each_side in sides_match_list:
                if each_dot_combination[0] in each_side and each_dot_combination[1] in each_side:
                    triangle_flag = True
                    break
                else:
                    triangle_flag = False
            else:
                triangle_flag = False
                break
        line_flag = False
        for each_side in sides_match_list:
            if each_combination[0] in each_side and each_combination[1] in each_side \
                    and each_combination[2] in each_side:
                line_flag = True

        if triangle_flag == True and line_flag == False:
            triangle_number += 1
            print "%d : %s" % (triangle_number, each_combination)

    print "The number of triangles in the picture is : %d" % triangle_number


if __name__ == '__main__':
    CounterTriangle()


