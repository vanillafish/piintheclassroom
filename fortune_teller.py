import random
fortunes=['Yes','Probably','Certainly','Maybe','Not sure','Ask again','Doubtful','No']
how_many_fortunes=len(fortunes)
raw_input('Think of a question, press Enter for the answer')
which_fortune=random.randint(0,how_many_fortunes-1)
print fortunes[which_fortune]
