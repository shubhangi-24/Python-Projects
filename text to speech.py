from win32com.client import Dispatch

speaker=Dispatch("SAPI.SpVoice")

print("Enter the text\n")
s=input()
speaker.Speak(s)