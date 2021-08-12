# ReplAccountAPI
Replapi that allows you to access data for a user 
## Run the flask webpage demo
well, just literally download the repo xD
install the `os` python lib and `pip`.
then just run the python project.
```sh
python3 demo_main.py
```
then open up your browser and see the website!!
>Note: The project automatically installs it's dependencies through `os.system` and `pip`

## Get the module
i made a module that fetches the data.
but i didn't publish it to pip yet.
so, you have to download it and import it locally.
download the `repluser.py` file and also download `jparser.py`.

## funcs
A simple example demoing all the functions.
```py
import repluser
user = repluser.ReplAPI(input(">>> ")); 
e = {'all_time': 'all time','': 'past week','past_year': 'past year','past_30_days': 'past 30 days'}
print(f"Their org is {user.getOrg()}") 
print(f"It is {user.getIsHacker()} that they are a hacker")
print(f"Their first name is {user.getFirstName()}") 
print(f"Their last name is {user.getLastName()}") 
print(f"their name is {user.getName()}") 
print(f"their repls are {user.getRepls()}") 
print(f"they have {user.getCycles()} cycles") 
print(f"their pfp can be found here: {user.getPfp()}")
print(f"their bio is: {user.getBio()}")
print(f"It is {user.isInLeaderboard()} that they are in the leaderboard.")
```
Oh and, to get the leaderboard, just type `repluser.getLeaderboard()`.

