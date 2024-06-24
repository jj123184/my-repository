user_age_years = float(input('Enter your age in years:\n'))
user_age_days = user_age_years * 365 # How many days user old
print("You are at least", user_age_days, "days old")

user_age_weeks = user_age_years * 52 # How many weeks user old. 1 year = 52 weeks
print("You are at least", user_age_weeks, "weeks old")
      
user_age_minutes = user_age_years * 1440 # How many minutes user old. 1 day = 1440 minutes
print("You are at least", user_age_years, "years old")
      

age_designation = ' '


if user_age_days>=0  and user_age_days<=30:# Birth to 1 month
    print('Neonates or newborns')
    
   
elif user_age_days>=31  and user_age_days<=365:# 1 month to 1 year   
   
    print('Infants')
    
elif user_age_days>=1*365 and user_age_days<=365*12:# 1 year through 12 years   
   
    print('Children')
    
elif user_age_days>=13*365 and user_age_days<=365*17:# 13 years through 17 years   
    
    print('Adolescents')
    
elif user_age_days>=18*365 and user_age_days<=365*64:# 18 years or older  
   
    print('Adults')
    
elif user_age_days > 365*65 :
    
    print('Older Adults')

