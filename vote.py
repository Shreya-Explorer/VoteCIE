import sys
if len(sys.argv)==2:
    age=int(sys.argv[1])
    if age > 18:
        print("Eligible to vote")
    else:
        print("Ineligible to vote")
else:
    age=20
    print("Eligible to vote")



