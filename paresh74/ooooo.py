def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.spVoice")
    speak.speak(str)
if __name__== "__main__":
    speak("mama kay asa ")
