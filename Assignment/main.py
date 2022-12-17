x = input(f"Enter the String you want to get converted into Morse Code")
l = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
     ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
ans = ""
alphablet = ['A', 'B', 'C', 'D', 'E', 'F','G', 'H', "I", 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
x = x.upper()

for i in x:
    r = alphablet.index(i)
    ans = ans + l[r]

print(ans)
