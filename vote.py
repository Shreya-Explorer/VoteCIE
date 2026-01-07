import sys
if len(sys.argv)==2:
    age=sys.argv[1]

else:
    age=20

if age>=18:
    result="Eligible to vote"

else:
    result="Ineligible to vote"

print(result)
