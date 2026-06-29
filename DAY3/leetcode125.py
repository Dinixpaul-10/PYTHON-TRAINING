checkpalindrome=input("Enter the text : ")
cleaned=""
for ch in checkpalindrome:
     if ch.isalnum():
                cleaned+=ch.lower()
     if cleaned==cleaned[::-1]:
            print(True)
     else:
            print(False)            
    