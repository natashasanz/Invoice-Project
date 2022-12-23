#Natasha Sanchez
#10/30/2022
#Sanchez-invoice.py
#This program will print an invoice for a three-credit class showing tuition, lab fees and books from CSCC

print ('*' * 50)
print ('\tColumbus State Community College')
print ('\t550 East Spring Street')
print ('\tColumbus, OH 43215')
print ('-' * 50)
print ('\tProduct name: \tProduct Price')
Books = 52.99
Lab_Fees = 25.00
Tuition = 157.93 * 3
print ('\tBooks \t\t$', format(Books), sep='')
print ('\tLab Fees \t$', format(Lab_Fees), sep='')
print ('\tTuition \t$', format(Tuition), sep='')
print ('-' * 50)
print ('\t\t\tTotal')
print ('\t\t\t$', Books + Lab_Fees + Tuition)
print ('-' * 50)
print ()
print ('   Thank you for being a Columbus State Student')
print ('\n*' * 50)










