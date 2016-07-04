import subprocess


print ("Channel name means only the name of the channel. twitch.tv/ is not needed")
print ("This script will open the stream in source.")
print ("\n")


stream = input("Enter a twitch channel name ")

subprocess.call(["C:\Program Files (x86)\Livestreamer\livestreamer.exe", 'twitch.tv/' + stream, "source"])
