s1="google.com"
s2={}
for i in s1:
   if i in s2:
      s2[i]+=1
   else:
      s2[i]=1
k = list(s2.keys())
n = len(k)
for i in range(n):
    for j in range(0, n - i - 1):
        if s2[k[j]] < s2[k[j + 1]]:
            k[j] = k[j + 1]
            k[j+1] = k[j]
s = {}
for key in k:
    s[key] = s2[key]
print(s)
