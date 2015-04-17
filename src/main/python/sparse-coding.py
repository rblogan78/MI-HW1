import sys
from random import randint

def generate(sampleCount, lowerBound=0, upperBound=15):

    dataset = []
    emptyCodedVector = []
    for i in xrange(0, upperBound, 1):
        emptyCodedVector.append(0)

    for i in xrange(sampleCount):
        rand = randint(lowerBound, upperBound-1) # Inclusive
        sample = list(emptyCodedVector)
        sample[rand] = 1
        dataset.append(sample)
        print sample

if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        # Only the filename was input
        print "Error: At least one argument is required"
        print "Expected usage: 'sparse-coding.py sampleCount [lowerBound], [upperBound]'"
    elif len(sys.argv) == 2:
        # One argument - Samples to generate
        generate( int(sys.argv[1]) )
    elif len(sys.argv) == 4:
        # Too many arguments
        sampleCount = int(sys.argv[1])
        lowerBound  = int(sys.argv[2])
        upperBound  = int(sys.argv[3])
        generate(sampleCount, lowerBound, upperBound)
    else:
        # Invalid number of arguments
        print "Error: Unexpected number of arguments"
        print "Expected usage: 'sparse-coding.py sampleCount [lowerBound], [upperBound]'"