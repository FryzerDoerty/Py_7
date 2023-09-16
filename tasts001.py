st = input(str('Введите строку:'))
stri = st.split()
print(stri)
glasn = "аАоОуУеЕэЭюЮяЯёЁиИыЫ"
def same_by(func, objs):
    return len(set(map(func, objs)))<2
arru= []
for i in stri:
    m = 0
    for j in i:
        m+=1 if j in glasn else 0
    arru.append(m)
if same_by(lambda x: x, arru):
    print("Парам пам-пам")
else:
    print("Пам парам")