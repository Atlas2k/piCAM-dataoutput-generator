import sys
import binascii
import math


def main():
    # outputSimulationData(hexDumpImage(sys.argv[1]))

    outputSimulationData(hexDumpImage(sys.argv[0]))


def hexDumpImage(fileName):
    with open("test.jpeg", 'rb') as f:
        hexString = binascii.hexlify(f.read()).decode('ascii')
    return hexString


def outputSimulationData(hexString):
    constructedString = "@%04x" % (0)
    totalSentences = math.ceil(len(hexString) / 56 + 1)
    constructedString += "%04x" % (totalSentences)
    charCount = 0
    lineCount = 0
    output = open("output.txt", "w")
    for char in hexString:
        if charCount < 56:
            constructedString += char
            charCount += 1
        else:
            constructedString += "\r\n"
            # Write to file
            output.write(constructedString)
            charCount = 0
            lineCount += 1
            constructedString = "@%04x" % (lineCount)
            constructedString += "%04x" % (totalSentences)
    # Add last sentence and close
    output.write(constructedString + ("0" * (56 - charCount)) + "\r\n")
    output.close()


main()
