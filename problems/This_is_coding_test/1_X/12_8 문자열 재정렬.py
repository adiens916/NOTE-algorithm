S = input()

alphabet_counts = [0] * (ord("Z") - ord("A") + 1)
number_sum = 0

for cha in S:
    if "0" <= cha <= "9":
        number_sum += int(cha)
    else:
        pos = ord(cha) - ord("A")
        alphabet_counts[pos] += 1

sorted_string = ""
for i in range(len(alphabet_counts)):
    alphabet = chr(ord("A") + i)
    sorted_string += alphabet * alphabet_counts[i]

# XXX: 숫자가 있는 경우에만 더하기
if number_sum > 0:
    sorted_string += str(number_sum)
print(sorted_string)

"""
K1KA5CB7
"""  # ABCKK13
"""
AJKDLSI412K4JSSJ9D
"""  # ADDIJJJKKLSS20
