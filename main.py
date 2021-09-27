# Tasks:
# 1.) Add header saying:
# "2021 F1 Drivers"
# "==============="
# 2.) Sort the list of drivers in alphabetical order by last name.
# 3.) sort the list of drivers in numerical order by driver's last name. 

# list of all the drivers, along with their information
driverInfo=["Max Verstappen 33 Red Bull","Lewis Hamilton 44 Mercedes YEET!","Valtteri Bottas 77 Mercedes",
           "Lando Norris 4 McLaren","Sergio Perez 11 Red Bull","Charles Leclerc 16 Ferrari",
           "Carlos Sainz 55 Ferrari","Daniel Ricciardo 3 McLaren","Pierre Gasly 10 AlphaTauri",
           "Fernando Alonso 14 Alpine","Esteban Ocon 31 Alpine","Esteban Ocon 31 Alpine",
           "Lance Stroll 18 Aston Martin","Yuki Sonoda 22 AlphaTauri","George Russell 63 Williams",
           "Nicholas Latifi 6 Williams","Kimi Raikkonen 7 Alfa Romeo","Antonio Giovinazzi 99 Alfa Romeo",
           "Mick Schumacher 47 Haas","Nikita Mazepin 9 Haas"]

# prints the header
print("\n2021 F1 Drivers \n===============\n")
# sorts in alphabetical order of last name
# words are seperated by white space, then the second word is sorted
driverInfo=sorted(driverInfo,key=lambda x: x.split(" ")[1])
# loop that will cycle through evey driver
for i in range(len(driverInfo)):
    print(driverInfo[i])

# prints the header
print("\n2021 F1 Drivers \n===============\n")

# sorting by numerical order, this looks at the third word to do this, and we add int to sort it numerically
driverInfo=sorted(driverInfo,key=lambda x: int(x.split(" ")[2]))
print()
# loop that will cycle through evey driver
for i in range(len(driverInfo)):
    print(driverInfo[i])