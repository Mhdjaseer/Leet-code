# Knuth-Morris-Pratt KMP String Matching Algorithm
------


Given a text **txt[0...N-1]** and a pattern **pat[0...M-1]**,write a function search (char pat[],char[]) that prints all occurrences of pat[]in txt[].You may assume that **N>M** 

## Example:
-----------
```
input:txt[]="THIS IS A TEST TEXT", pat[]='TEST'
Output: Pattern found at index 10

Input:txt[]= 'AABAACAADAABAABA'
      pat[]='AABA'

Output:Pattern found at index 0, pattern found at index 9, pattern found at index 12
```
![Alt text](image.png)


-----
pattern searching is an important problem in computer science . when we do seach for a string in a notepad/word file or browser or database. 
pattern-searching algorithms are used to show the search results. 

the worst case complexity of the Naive algorithm is O(m(n-m+1).
the time complexity of the KMP algorithm is O(n+m) in the worst case . 

# KMP (knuth Morris Pratt) Pattern Searching:
The <u>Naive-pattern-searching algorithm</u> doesn't work well in case where we see many matching charecters followed by a mismatching charecter. 

## Example
```
1) txt[]='AAAAAAAAAAAAAAAAAB',pat[]='AAAAB'
2) txt[]='ABABABCABABABCABABABC', pat[] =  “ABABAC” (not a worst case, but a bad case for Naive)

```

The KMP matching algorithm uses degenerating property (pattern having the same sub-patterns appearing more than once in the pattern) of the pattern and improves the worst-case complexity to **O(m+n)**.

The basic idea behind KMP's algorithm is : whenever we detect a mismatch (after some matches ),we already know some of the charecters in the text of the next window , We take advantage of this information to avoid matching the characters that we know will anyway match . 


```
txt = “AAAAABAAABA” 
pat = “AAAA”
We compare first window of txt with pat

txt = “AAAAABAAABA” 
pat = “AAAA”  [Initial position]
We find a match. This is same as Naive String Matching.

In the next step, we compare next window of txt with pat.

txt = “AAAAABAAABA” 
pat =  “AAAA” [Pattern shifted one position]

This is where KMP does optimization over Naive. In this second window, we only compare fourth A of pattern
with fourth character of current window of text to decide whether current window matches or not. Since we know 
first three characters will anyway match, we skipped matching first three characters. 

Need of Preprocessing?

An important question arises from the above explanation, how to know how many characters to be skipped. To know this, 
we pre-process pattern and prepare an integer array lps[] that tells us the count of characters to be skipped
```


### Preprocessing Overview::









# do learn Naive-pattern-searching  algorithm