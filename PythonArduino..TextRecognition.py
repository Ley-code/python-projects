import speech_recognition
import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

portslist = []

for port in ports:
    portslist.append(str(port))
    print(str(port))

val = input("Select port: COM")

for x in range(0,len(portslist)):
    if portslist[0].startswith("COM" + str(val)):
        portvar = "COM" + str(val)

serialInst.baudrate = 9600
serialInst.port = portvar
serialInst.open()

recongizer = speech_recognition.Recognizer()
while True:
    try:
        with speech_recognition.Microphone() as mic:
            recongizer.adjust_for_ambient_noise(mic,duration = 0.2)
            audio = recongizer.listen(mic)
            text = recongizer.recognize_google(audio)
            text = text.lower()
            print(f"Recognized:  {text}")
    except speech_recognition.UnknownValueError():
        recongizer = speech_recognition.Recognizer()
        continue
    serialInst.write(text.encode('utf-8'))
