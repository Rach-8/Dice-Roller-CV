import os
from datetime import date


dice_type = "D6"
par_dir = "./Dataset/"
if os.path.isdir("Dataset"):
    print("Dataset directory exists")
    path = os.path.join(par_dir,dice_type)

    if os.path.isdir("Dataset/D6"):
        print(dice_type+"directory exists")
    else:
        path = os.path.join(par_dir,dice_type)
        os.makedirs(path,0o666)
        print(dice_type+" directory created")

cr_date = date.today()
dice_dir="./Dataset/"+dice_type
itr = 1
itr_cp = itr
file_nm = str(cr_date) +"_"+str(itr)
path1 = os.path.join(dice_dir,file_nm)

# Check if the dice_dir exists
if not os.path.isdir(dice_dir):
    os.makedirs(dice_dir)

# Initialize the counter
itr = 1

# Generate the file name
file_nm = str(cr_date) + "_" + str(itr)
path1 = os.path.join(dice_dir, file_nm)

# Check if the folder already exists
while os.path.isdir(path1):
    itr += 1
    file_nm = str(cr_date) + "_" + str(itr)
    path1 = os.path.join(dice_dir, file_nm)

# Create the new folder
print(file_nm + " does not exist, making directory")

os.makedirs(path1, 0o666)
os.makedirs(path1+"/Dice_Imgs", 0o666)
os.makedirs(path1+"/Dice_Num", 0o666)


# Print the generated folder path
print("Folder created:", path1)

























