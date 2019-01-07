----------------------------------------------------------------------
### PROJECT: GET YOUR ZODIAC SIGN AND AGE BASED ON USER INPUT DATE ###
----------------------------------------------------------------------
#importing library
from datetime import date

#creting inputs
Year = input("What's your year of birth? [ex: 1992]" )
Month = input("What's your month of birth? [ex: 10]" )
Day = input("What's your day of birth? [ex: 25]" )
print('Your Date of Birth is ', (Day + "/" + Month + "/" + Year))

#defining user age
today_day = date.today()
age = today_day.year - int(Year)
print('You are', age, 'years old')

#creating if conditions to check the zodiac sign
if ((int(Month)==12 and int(Day) >= 22) or (int(Month)==1 and int(Day)<= 19)):
    sign = ("\n Capricorn")
elif ((int(Month)==1 and int(Day) >= 20)or(int(Month)==2 and int(Day)<= 18)):
    sign = ("\n aquarius")
elif ((int(Month)==2 and int(Day) >= 19)or(int(Month)==3 and int(Day)<= 20)):
    sign = ("\n Pisces")
elif ((int(Month)==3 and int(Day) >= 21)or(int(Month)==4 and int(Day)<= 19)):
    sign = ("\n Aries")
elif ((int(Month)==4 and int(Day) >= 20)or(int(Month)==5 and int(Day)<= 20)):
    sign = ("\n Taurus")
elif ((int(Month)==5 and int(Day) >= 21)or(int(Month)==6 and int(Day)<= 20)):
    sign = ("\n Gemini")
elif ((int(Month)==6 and int(Day) >= 21)or(int(Month)==7 and int(Day)<= 22)):
    sign = ("\n Cancer")
elif ((int(Month)==7 and int(Day) >= 23)or(int(Month)==8 and int(Day)<= 22)): 
    sign = ("\n Leo")
elif ((int(Month)==8 and int(Day) >= 23)or(int(Month)==9 and int(Day)<= 22)): 
    sign = ("\n Virgo")
elif ((int(Month)==9 and int(Day) >= 23)or(int(Month)==10 and int(Day)<= 22)):
    sign = ("\n Libra")
elif ((int(Month)==10 and int(Day) >= 23)or(int(Month)==11 and int(Day)<= 21)): 
    sign = ("\n Scorpio")
elif ((int(Month)==11 and int(Day) >= 22)or(int(Month)==12 and int(Day)<= 21)):
    sign = ("\n Sagittarius")

#printing a user zodiac sign
print(sign)

