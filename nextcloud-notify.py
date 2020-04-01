import subprocess

cmd0 = "rm -r 10Gym"
cmd1 = "wget https://cloud.ifb-engel.de/s/tFESY5zSy24b4cg/download -O 10G.zip"
cmd2 = "unzip 10G.zip"
cmd3 = "mv 10\ Gymnasium\ Aufgaben/ 10Gym"
cmd4 = "diff -qr 10Gym old"
cmd5 = "rm -r old"
cmd6 = "mv 10Gym old"
success = "kdeconnect-cli -d ################ --ping-msg 'notification_message'"

try:
    subprocess.check_output(cmd0, shell=True)
except subprocess.CalledProcessError:
    print("An Error occured while renaming the current directory")
try:
    subprocess.check_output(cmd1, shell=True)
except subprocess.CalledProcessError:
    print("An Error occured while downloading the file")
try:
    subprocess.check_output(cmd2, shell=True)
except subprocess.CalledProcessError:
    print("An Error occured while Unzipping the file")
try:
    subprocess.check_output(cmd3, shell=True)
except subprocess.CalledProcessError:
    print("An Error occured while renaming the folder")
try:
    subprocess.check_output(cmd4, shell=True)
except subprocess.CalledProcessError:
    try:
        subprocess.check_output(success, shell=True)
    except subprocess.CalledProcessError:
        print("Error sending Notification")

print("Preparing Environment for the next run...")

try:
    subprocess.check_output(cmd5, shell=True)
except subprocess.CalledProcessError:
    print("An Error occured while removing the old directory")
try:
    subprocess.check_output(cmd6, shell=True)
except subprocess.CalledProcessError:
    print("An Error occured while renaming the current directory")
