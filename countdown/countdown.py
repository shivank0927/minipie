import sys
import time
import sevseg 

secondsLeft = int(input("\n>>> "))

def hourCalculation(prompt: int):
    return str(prompt // 3600)

def minuteCalculation(prompt: int):
    return str((prompt % 3600) // 60)

def secondCalculation(prompt: int):
    return str(prompt % 60)

try:
    while True:  
        print('\n' * 60)

 
        hours = hourCalculation(secondsLeft)
        minutes = minuteCalculation(secondsLeft)
        seconds = secondCalculation(secondsLeft)


        hDigits = sevseg.getSevSegStr(hours, 2)
        hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()

        mDigits = sevseg.getSevSegStr(minutes, 2)
        mTopRow, mMiddleRow, mBottomRow = mDigits.splitlines()

        sDigits = sevseg.getSevSegStr(seconds, 2)
        sTopRow, sMiddleRow, sBottomRow = sDigits.splitlines()

        # display
        print(hTopRow + ' ' + mTopRow + ' ' + sTopRow)
        print(hMiddleRow + ' * ' + mMiddleRow + ' * ' + sMiddleRow)
        print(hBottomRow + ' * ' + mBottomRow + ' * ' + sBottomRow)

        if secondsLeft == 0:
            print()
            print('Times up!')
            break

        print()
        print('press Ctrl + C to quit.')

        time.sleep(1)  
        secondsLeft -= 1

except KeyboardInterrupt:
    print('\ncountdown interrupted.')
    sys.exit() 

