class SetTrippin(object):

    def setCreator(self, preSet):
        """
            Args:  preSet: String
            Return: postSet: Set of processed 'preSet' string
        """
        preSet = self.removeDelimiters(preSet)
        postSet = set(preSet.split(" "))
        return postSet

    def setIntersection(self, set1, set2):
        """
           Args:  set1: String
                  set2: String
           Return: None, prints the intersections or notifies user that there is a lack of intersections.
        """
        set3 = set1.intersection(set2)
        if not set3 or '' in set3:
            print("There are no points of intersection.\n")
        else:
            print("\nThe common words in this set include:")
            print("{}\n".format(set3))

    def setDifferences(self, set1, set2):
        """
            Args:   set1: String
                    set2: String
            Return: None, prints the differences or notifies user that there is a lack of differences.
        """
        set3 = set1.difference(set2), set2.difference(set1)
        if not set3 or '' in set3:
            print("There are no points of difference in your sets")
        else:
            print("The unique words in either set include:")
            print("Set #1 Unique Words : {}".format(set3[0]))
            print("Set #2 Unique Words : {}".format(set3[1]))

    def removeDelimiters(self, inputString):
        """
            Args:   inputString: String
            Return: outputString: processed string with all delimiters removed
        """
        delimiters = [",", ".", "!", "?", "/", "&", "-", ":", ";", "@", "'", "..."]
        outputString = []
        garbage = []
        for each in inputString:
            if each not in delimiters:
               outputString.append(each)
            else:
                garbage.append(each)
        print("Delimiters Removed from this set:")
        print("{}".format(garbage))

        outputString = "".join(outputString)
        return outputString

if __name__ == '__main__':
    run = SetTrippin()
    practiceSet1 = "Hell@o m,y n,ame is F,,red"
    practiceSet2 = "Pleasu@re to meet you@@, my name! is Gre.g"
    result1 = run.setCreator(practiceSet1)
    result2 = run.setCreator(practiceSet2)
    run.setIntersection(result1, result2)
    run.setDifferences(result1, result2)
