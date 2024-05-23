import random


class Solution:
    '''!
        \brief Класс для математических операций.

        Данный класс предоставляет функционал разных математических операций для шаблоных типов.
    '''
    def __init__(self):
        pass

    def quicksort(self, nums):
        '''!
            \brief Шаблонная функция ,быстрой сортировки

        
            \param [in] nums Массив, который нужно сложить

            \return Новый объект типа *nums*, равный отсортированному *nums*.
        '''
        if len(nums) <= 1:
            return nums
        else:
            q = random.choice(nums)
        l_nums = [n for n in nums if n < q]
        
        e_nums = [q] * nums.count(q)
        b_nums = [n for n in nums if n > q]
        return self.quicksort(l_nums) + e_nums + self.quicksort(b_nums)