def ValidateRegistration(Registration):
  t=0
  f=0
  Reglen=0
  Reglen=len(Registration)
  if (Reglen<5) and (Reglen>10):
      f+=1
  else:
      t+=1
  while t>0 and t<2 :
      p=0
      for p in range(3):
          ASC=ord(Registration[p])
          if ASC >= ord('A') and ASC<= ord('Z'):
              t+=1
          else:
              f+=1
          p+=1
      NUM=ord(Registration[3])
      if NUM >= ord('0') and NUM <= ord('9'):
          t+=1
      else:
          f+=1
      NUM2=ord(Registration[4])
      if NUM2>= ord('0') and NUM2<= ord('9'):
          t+=1
      else:
          f+=1
      test=0
      test=Reglen-5
      for count in range(test):
          count=6
          if ord(Registration[count])>= ord('A') and ord(Registration[count])<=ord('Z'):
              t+=1
          else:
              f+=1
          count+=1 
  if (f>0):
      print("The number is invalid")
  else:
      print("The number is valid")



Registration=input("Please enter your registration number ")
ValidateRegistration(Registration)





