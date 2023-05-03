# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line 
#definition of variables
scorer1 = 'Ruud Gullit '
scorer2 = 'Marco van Basten '
goal_0 = 32
strgoal0 = str(goal_0)
goal_1 = 54
strgoal1 = str(goal_1)

#state which players scored the goals during the EURO1988 Final and when
Score_stat1 = scorer1 + 'scored in the ' + strgoal0 + 'nd minute'
Score_stat2 = scorer2 + 'scored in the ' + strgoal1 + 'th minute'
report=Score_stat1+' '+Score_stat2
scorers = scorer1+strgoal0+', '+scorer2+strgoal1
scorers_explained = 'The players who scored the goals in the EURO1988 final were: \n' + Score_stat1 + ' and\n' + Score_stat2
print(scorers_explained)

# Save the Scorers to a CSV report
import os

file_path = r'C:\Users\Arnoud\Documents\Werk\Magniv\Cursus Data Analytics with Python\Winc\strings\RGMvB.csv'
if os.path.exists(file_path):
    print('The score statistics of the EURO1988 final have already been saved in a csv file')
else:
    #create the csv file
    with open(file_path, 'w') as fp:
        #uncomment if you want empty file  
        fp.write(scorers)


player = 'Hans_van_Breukelen'
first_name = player[0:4]
last_name = player[5:8]+' '+player[9:18]
last_name_len = len(last_name)
name_short = player[0:1] + '. ' + player[5:8] + ' ' + player[9:18]
print(name_short)
print(first_name)
print(last_name)
print(first_name+'! '+first_name+'! '+first_name+'!'+' Wat een geweldige save!!')
print(2 !=3)
file_path = r'C:\Users\Arnoud\Documents\Werk\Magniv\Cursus Data Analytics with Python\Winc\strings\HvB.csv'
if os.path.exists(file_path):
    print('The goalkeeper of the EURO1988 final has already been saved in a csv file')
else:
    #create the csv file
    with open(file_path, 'w') as fp:
        #uncomment if you want empty file  
        fp.write(name_short)




   
      
       
        






 