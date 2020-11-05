driving = input('請問您有沒有開過車？')
if driving != '有' and driving != '沒有':
	print('請輸入有/沒有')
	raise SystemExit

age = input('請問您的年齡？')
age = int(age)
if driving == '有':
	if age >= 18:
		print('您通過測驗了')
	else:
		print('奇怪，您怎麼會有開過車')
elif driving == '沒有':
	if age >= 18:
		print('您可以考駕照了')
	else:
		print('再過幾年就可以考駕照了')
