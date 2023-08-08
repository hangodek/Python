The itertools module standardizes a core set of fast, memory efficient tools that are useful by themselves or in combination. Together, they form an iterator algebra making it possible to construct specialized tools succinctly and efficiently in pure Python.

To read more about the functions in this module, check out their documentation here.

You are given a list of n lowercase English letters. For a given integer k, you can select any k indices (assume -based indexing) with a uniform probability from the list.

Find the probability that at least one of the k indices selected will contain the letter: ''.

Input Format
The input consists of three lines. The first line contains the integer n, denoting the length of the list. The next line consists of  space-separated lowercase English letters, denoting the elements of the list.

The third and the last line of input contains the integer k, denoting the number of indices to be selected.

Output Format
Output a single line consisting of the probability that at least one of the k indices selected contains the letter:'a'.

Note: The answer must be correct up to 3 decimal places.

Sample Input
4 
a a c d
2

Sample Output
0.8333

