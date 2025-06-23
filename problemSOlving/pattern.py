'''
print the below pattern

     *
   * * *
 * * * * *
   * * *
     *

follow the steps learned and achive this

      A
    B A B
  C B A B C
D C B A B C D
  C B A B C
    B A B
      A

This one too guys.
'''

char = 'A'

for i in range(0,26):
    printed_val = (ord(char) + i)
    print( chr(printed_val), end=" ")

    # 'a' + 1 = 'b' 