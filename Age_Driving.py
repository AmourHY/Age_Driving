driving = input('請問有沒有開過車? ')
if driving != 'Yes' or driving != 'No':
	print('請輸入 Yes /No ')
	raise SystemExit   #若使用者輸入非Yes / No，則觸發(raise)離開系統。

age = int(input('請問年齡? '))

if driving == 'Yes':
	if age >= 18:
		print('合法開車，不錯!')
	else:
		print('你車速(年齡)有點快喔!')
elif driving == "No":
	if age >= 18:
		print('可以考駕照了喔!')
	else:
		print('再過', 18 - age, '年就可以考駕照了!')

