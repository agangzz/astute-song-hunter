import tkSnack, Tkinter
import line,math

root = Tkinter.Tk()
tkSnack.initializeSnack(root)
Snd1 = tkSnack.Sound(load="songs/milana1.wav")
Snd2 = tkSnack.Sound(load="tunes/ghajini.wav")
b1 = line.normalize(Snd1.dBPowerSpectrum(fftlength=16384))
b2 = line.normalize(Snd2.dBPowerSpectrum(fftlength=16384))

if b1 > b2 :
  A = math.atan((b1-b2)/(1+b1*b2))
else:
  A = math.atan((b2-b1)/(1+b1*b2))
print "Angle between lines = ",A