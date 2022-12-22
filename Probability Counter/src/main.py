
class ProbabilityCounter():
    def __init__(self):
        self.allCards = "AKQJT98765432X"
        self.first = ""
        self.second = ""
        self.dash = 5
        self.usCards = {}
        self.oppsCards = {} #kartu musuh
        #end of init

    def getInput(self):
        while(True):
            counter = {}
            for letter in self.allCards:
                counter[letter] = 0
            isError = False
            print("Masukkan distribusi kartu")
            
            self.first = input("Pertama >> ")
            self.second= input("Kedua   >> ")

            self.first = self.first.upper()
            self.second = self.second.upper()

            for letter in self.first:
                if letter not in self.allCards:
                    isError = True
                    break
                if counter[letter] == 0 and letter != "X":
                    counter[letter] += 1
                else :
                    isError = True
                    break
                
            for letter in self.second:
                if letter not in self.allCards:
                    isError = True
                if counter[letter] == 0 and letter != "X":
                    counter[letter] += 1
                else :
                    isError = True
                    break
                if isError:
                    break
            
            if isError:
                print("kartu dengan format AKQJT98765432 atau x untuk kartu yang tidak diperhatikan")
            
            self.printDash(self.dash)

            break
    
    def printDash(self, n):
        for _ in range(n):
            print("-", end="")
        print("")
    
    def setCards(self):
        all = self.first + self.second
        x_count = all.count('X')
        newSet = True
        newStr = ""
        usStr = ""
        count_opps = 1
        count_us = 1
        for letter in self.allCards[0:-x_count-1]:
            if letter not in all and letter != 'X':
                newStr += letter
                newSet = False
                if usStr != "":
                    self.usCards[count_us] = usStr
                    usStr = ""
                    count_us += 1
            elif not newSet:
                self.oppsCards[count_opps] = newStr
                count_opps += 1
                newSet = True
                newStr = ""
                usStr = letter
            else:
                usStr += letter
        if not newSet:
            self.oppsCards[count_opps] = newStr
        if usStr != "":
            self.usCards[count_us] = usStr
        elif x_count > 0:
            self.usCards[count_us] = self.allCards[-x_count-1:-1]
        pass

    def generateDist(self):
        all = ""
        for sets in self.oppsCards:
            all += self.oppsCards[sets]
        countCards = len(all)
        self.allDist = []
        for i in range(0, countCards+1):
            self.generateOppsCard(all, countCards-i, i)
        for comb in self.allDist:
            print(comb)
    
    def generateOppsCard(self, card, l, r):
        if l == 0:
            self.allDist.append(["", card])
            return
        elif r == 0:
            self.allDist.append([card, ""])
            return
        left = ""
        right = ""
        self.combination("", card, l + r, l, 0)
        return self.allDist
    
    def combination(self, left, card, n, r, i):
        if r == 0:
            right = ""
            for letter in card:
                if letter not in left:
                    right += letter
            self.allDist.append([left, right])
            return None
        for index in range(i,n):
            left += card[index]
            self.combination(left, card, n, r-1, index+1)
            left = left[:-1]
    
    def getRankOpps(card):
        if card == "": return
        output = ""
        counter = [0 for _ in range(len(list(self.oppsCard)))]
        for letter in card :
            for sets in self.oppsCards:
                if letter in self.oppsCards[sets]:
                    output += sets
        

    def setRankCombination(self):
        self.RankCombination = []
        counter = 0
        for comb in self.combination:


    def startPlay(self):
        history = ""
        rankCard = list(self.usCards)
        first = list(self.first)
        second = list(self.second)
        print(rankCard)
        # counter = 0
        # for i in range(len(self.first)):
        #     if first[i] == 'X':
        #         first[i] = self.usCards[rankCard[-1]][counter]
        #         counter += 1
        # for i in range(len(self.second)):
        #     if second[i] == 'X':
        #         second[i] = self.usCards[rankCard[-1]][counter]
        #         counter += 1
        print(first)
        print(second)

        #example
        #1-2-3-4444
        #4444
        #first choice : 4*1 + 1*4 biar gak ribet
        #if playing highest/lowest card, there is no diff from where
        #if opps low, branch option
        #if opps high, set bigger card / lowest
        #if opps void known, always play finesse
        #defending, if not beneficial putting high, put lowest
    def play(self, played, )


def main():
    pc = ProbabilityCounter()
    pc.getInput()
    pc.setCards()
    pc.generateDist()
    pc.startPlay()
    
    #end of main

if __name__ == "__main__":
    main()
