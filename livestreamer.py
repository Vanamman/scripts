import subprocess


print ("Channel name means only the name of the channel. twitch.tv/ is not needed")
print ("\n")


stream = input("Enter a twitch channel name: ")
quality = input('Enter a quality level (Low, Medium, High, Source): ')

subprocess.call(["C:\Program Files (x86)\Livestreamer\livestreamer.exe", 'twitch.tv/' + stream, quality])
