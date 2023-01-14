#length of latin alphabet
alphabetLength = 26
#range of UNICODE integer IDs for lowercase latin
rangeLowercase = range(97, 123)
#range of UNICODE integer IDs for uppercase latin
#rangeUppercase = range(65, 91)

#exception class for shiftNumber length exceeding int length
class LengthError (Exception):
    pass

#exception class for finishing main loop
class FinishException (Exception):
    pass

#encoding/decoding function
def encryption_and_decryption(shiftNumber, inputText):
    print("Output text: ", end="")
    #calculate shift number, 27 shift = 1 shift
    if shiftNumber > alphabetLength or shiftNumber < -alphabetLength:
        shiftNumber -= (shiftNumber//26)*26
    else:
        pass
    #for every letter in inputText convert to lowercase
    for originalLetter in inputText:
        if originalLetter.isupper() == True:
            loweredLetter = originalLetter.lower()
        else:
            loweredLetter = originalLetter
        #increment letter by shiftNumber
        decimalID = ord(loweredLetter)
        if decimalID in rangeLowercase:
            decimalID += shiftNumber
            while decimalID > 122:
                shiftRemainder = decimalID - 122
                decimalID = 96 + shiftRemainder
                if decimalID <= 122:
                    break
            while decimalID < 97:
                shiftRemainder = decimalID - 97
                decimalID = 123 + shiftRemainder
                if decimalID >= 97:
                    break
        elif decimalID not in rangeLowercase:
            pass
        #print original uppercase letters in uppercase
        if originalLetter.isupper() == True:
            print(chr(decimalID).upper(), end="")
        else:
            print(chr(decimalID), end="")
    print("\n")

#main program part, while True loops take input, arguments passed to encryption_and_decryption function
print("Welcome to the Caesar cipher encoder & decoder. Specify your parameters below.\nOnly latin lowercase & uppercase letters are encoded, special characters are ignored!\n")
#while True execute code in main loop
while True:
    #try executing main loop
    try:
        #try getting operartionType
        try:
            print("Choose operation type:\n1) Encryption \n2) Decryption")
            print("Operation: ", end="")
            operationType = int(input())
            if operationType == 1 or operationType == 2:
                pass
            else:
                raise ValueError
        #except operationType !=1 or !=2 print error and start again
        except ValueError:
            print("\nInvalid input! Choose correct operation type.\n")
            continue
        #if no error continue
        else:
            while True:
                #try getting shiftNumber
                try:
                    print("\nChoose letter shift (positive or negative int): ")
                    print("Letter shift: ", end="")
                    shiftNumber = int(input())
                    if shiftNumber > 2147483647 or shiftNumber < -2147483647:
                        raise LengthError
                    else:
                        pass
                #except shiftNumber longer than int print error and start again
                except LengthError:
                    print("\nLetter shift too long! Choose letter shift from -2147483647 to 2147483647.")
                    continue
                #except shiftNumber 
                except ValueError:
                    print("\nInvalid input! Choose correct letter shift.")
                #if no error continue
                else:
                    while True:
                        if operationType == 1:
                            pass
                        elif operationType == 2:
                            shiftNumber *= -1
                        #try to get inputText
                        try:
                            print("\nInput text: ", end="")
                            inputText = str(input())
                            if inputText == "":
                                raise ValueError
                            else:
                                pass
                        #except inputText is blank print error and start again
                        except ValueError:
                            print("\nInvalid input! Enter correct phrase.")
                            continue
                        #if no error continue
                        else:
                            encryption_and_decryption(shiftNumber, inputText)
                            while True:
                                try:
                                    print("More? (blank = yes), (y/n)")
                                    wantMore = str(input())
                                    if wantMore == "" or wantMore == "y":
                                        pass
                                    elif wantMore == "n":
                                        quit()
                                    else: 
                                        raise ValueError
                                except ValueError:
                                    continue
                                else:
                                    raise FinishException
    #except FinishException is raised finish main loop and start again
    except FinishException:
        continue

                  
                   
                           
                        
    