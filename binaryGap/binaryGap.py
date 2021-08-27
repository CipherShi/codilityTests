def solution(A):     
     binary = str(bin(A))[2:]
     bin_gap = False
     bin_max = 0
     bin_counter = 0
     for char in binary:
         if char == '1':
             if bin_max < bin_counter:
                 bin_max = bin_counter
             bin_gap = True
             bin_counter = 0
         elif bin_gap:
             bin_counter += 1
     return bin_max