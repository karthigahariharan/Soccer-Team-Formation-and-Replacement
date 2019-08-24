import numpy as np
import csv
import json
from collections import OrderedDict
import pandas as pd

class TeamFormation:
    def __init__(self):
        self.players = {'139671': ['Marc Albrighton', 'm'], '23571': ['Wes Morgan', 'd'], '37770': ['Kasper Schmeichel', 'g'], '319300': ['N\'Golo Kante', 'm'], '278343': ['Riyad Mahrez', 'm'], '20694': ['Shinji Okazaki', 's'], '286119': ['Jamie Vardy', 's'], '173317': ['Danny Drinkwater', 'm'], '38899': ['Robert Huth', 'd'], '43061': ['Christian Fuchs', 'd'], '49571': ['Danny Simpson', 'd'], '26554': ['Jose Leonardo Ulloa', 's'], '103419': ['Andy King', 'm'], '214570': ['Jeffrey Schlupp', 'm'], '67850': ['Ritchie De Laet', 'd'], '23305': ['Nathan Dyer', 'm'], '492586': ['Demarai Gray', 'm'], '436036': ['Daniel Amartey', 'd'], '25818': ['Gokhan Inler', 'm'], '94326': ['Yohan Benalouane', 'd'], '173461': ['Andrej Kramaric', 's'], '45571': ['Ben Hamer', 'g'], '30633': ['Mark Schwarzer', 'g'], '1000': ['Ben Chilwell', 'd'], '1001': ['Matty James', 'm'], '494435': ['Tom Lawrence', 's'], '210804': ['Liam Moore', 'd']}
        self.players = OrderedDict(self.players)
        self.goal_keepers = {'37770': 'Kasper Schmeichel', '45571': 'Ben Hamer', '30633': 'Mark Schwarzer'}
        self.strikers = {'286119': 'Jamie Vardy', '494435': 'Tom Lawrence', '173461': 'Andrej Kramaric', '20694': 'Shinji Okazaki', '26554': 'Jose Leonardo Ulloa'}
        self.mid_fielders = {'173317': 'Danny Drinkwater', '1001': 'Matty James', '103419': 'Andy King', '139671': 'Marc Albrighton', '319300': 'N\'Golo Kante', '214570': 'Jeffrey Schlupp', '492586': 'Demarai Gray', '23305': 'Nathan Dyer', '278343': 'Riyad Mahrez', '25818': 'Gokhan Inler'}
        self.defenders = {'67850': 'Ritchie De Laet', '23571': 'Wes Morgan', '38899': 'Robert Huth', '436036': 'Daniel Amartey', '49571': 'Danny Simpson', '210804': 'Liam Moore', '43061': 'Christian Fuchs', '94326': 'Yohan Benalouane', '1000': 'Ben Chilwell'}

        self.skill_probability_matrix = self.getJSONData("skill_with_probability_svm.json")
        df = pd.DataFrame(self.skill_probability_matrix)
        df_t = df.transpose()
        df_t.to_csv("skill_matrix_replacement.csv",index=False)
        
        self.coordinationMatrix = self.getJSONData("coordination.json")
        df = pd.DataFrame(self.coordinationMatrix)
        df.to_csv("coordination_matrix_replacement.csv",index=False)
        self.scores = []

        self.team_formed = []
        self.rem_players = self.players.copy()
        self.num_players = {}
        self.home_matches = self.getJSONData("HomeMatches.json")
        self.away_matches = self.getJSONData("AwayMatches.json")

    def getJSONData(self, fileName):
        with open(fileName) as json_data:
            return json.load(json_data)

    def normalizeScoreMatrix(self):
        self.scores = self.coordinationMatrix[:]
        maxCordination = max(max(self.scores))
        self.scores = [[item / maxCordination for item in subl] for subl in self.scores]

    def calculateScoreMatrix(self, w1, w2):
        self.normalizeScoreMatrix()
        for i, (k1, v1) in enumerate(self.players.iteritems()):
            for j, (k2, v2) in enumerate(self.players.iteritems()):
                self.scores[i][j] = w2 * float(self.scores[i][j]) + w1 * float(self.skill_probability_matrix[k1]['prob_gnb']) #Change to prob_svm to run SVM and prob_gnb to run GNB

    def initTeamWith4TopPlayers(self):

        for i, (k1, v1) in enumerate(self.goal_keepers.iteritems()):
            self.goal_keepers[k1] = self.skill_probability_matrix[k1]['prob_gnb']
        goal_keepers_s = [(k, self.goal_keepers[k]) for k in sorted(self.goal_keepers, key=self.goal_keepers.get, reverse=True)]
        for i, (k1, v1) in enumerate(self.strikers.iteritems()):
            self.strikers[k1] = self.skill_probability_matrix[k1]['prob_gnb']
        strikers_s = [(k, self.strikers[k]) for k in sorted(self.strikers, key=self.strikers.get, reverse=True)]
        for i, (k1, v1) in enumerate(self.mid_fielders.iteritems()):
            self.mid_fielders[k1] = self.skill_probability_matrix[k1]['prob_gnb']
        mid_fielders_s = [(k, self.mid_fielders[k]) for k in sorted(self.mid_fielders, key=self.mid_fielders.get, reverse=True)]
        for i, (k1, v1) in enumerate(self.defenders.iteritems()):
            self.defenders[k1] = self.skill_probability_matrix[k1]['prob_gnb']
        defenders_s = [(k, self.defenders[k]) for k in sorted(self.defenders, key=self.defenders.get, reverse=True)]

        self.team_formed = []
        self.rem_players = self.players.copy()
        self.team_formed.append(strikers_s[0][0])
        del self.rem_players[strikers_s[0][0]]
        self.team_formed.append(mid_fielders_s[0][0])
        del self.rem_players[mid_fielders_s[0][0]]
        self.team_formed.append(defenders_s[0][0])
        del self.rem_players[defenders_s[0][0]]
        self.team_formed.append(goal_keepers_s[0][0])
        del self.rem_players[goal_keepers_s[0][0]]
        self.num_players = {'g': 0, 'd': 3, 'm': 3, 's': 1}

    def formTeam(self):
        self.initTeamWith4TopPlayers()

        while (len(self.team_formed) < 11):
            sum_scores = np.zeros(len(self.rem_players))
            for i, (k1, v1) in enumerate(self.rem_players.iteritems()):
                for j, n in enumerate(self.team_formed):
                    sum_scores[i] += self.scores[self.players.keys().index(k1)][self.players.keys().index(n)]
            player_index = np.argmax(sum_scores)
            key_chosen_p = self.rem_players.keys()[player_index]
            if self.num_players[self.rem_players[key_chosen_p][1]] > 0:
                self.num_players[self.rem_players[key_chosen_p][1]] -= 1
                self.team_formed.append(key_chosen_p)
            del self.rem_players[key_chosen_p]

#        for player in self.team_formed:
#            print self.players.keys().index(player)
#            print self.players[player]

    def calculateAccuracy(self):
        print "All matches"
        allMatches = self.home_matches + self.away_matches

        overAllAccuracy = 0
        for match in allMatches:
            print "Actual team",match
            print "Predicted team", self.team_formed
            matchAccuracy = 0
            for player in self.team_formed:
                if int(player) in match:
                    
                    matchAccuracy += 1
            matchAccuracy = matchAccuracy / float(len(self.team_formed))
            print "matchAccuracy", matchAccuracy
            overAllAccuracy += matchAccuracy
        overAllAccuracy = overAllAccuracy / float(len(allMatches))
        print overAllAccuracy

        print "Home matches"
        allMatches = self.home_matches

        overAllAccuracy = 0
        for match in allMatches:
            matchAccuracy = 0
            for player in self.team_formed:
                if int(player) in match:
                    matchAccuracy += 1
            matchAccuracy = matchAccuracy / float(len(self.team_formed))
            # print "matchAccuracy", matchAccuracy
            overAllAccuracy += matchAccuracy
        overAllAccuracy = overAllAccuracy / float(len(allMatches))
        print overAllAccuracy

        print "Away matches"
        allMatches = self.away_matches

        overAllAccuracy = 0
        for match in allMatches:
            matchAccuracy = 0
            for player in self.team_formed:
                if int(player) in match:
                    matchAccuracy += 1
            matchAccuracy = matchAccuracy / float(len(self.team_formed))
            # print "matchAccuracy", matchAccuracy
            overAllAccuracy += matchAccuracy
        overAllAccuracy = overAllAccuracy / float(len(allMatches))
        print overAllAccuracy

    def runEverything(self, w1, w2):
        self.calculateScoreMatrix(w1, w2)
        self.formTeam()
        self.calculateAccuracy()


def runWithDifferentWeights():
    team = TeamFormation()
    for i in xrange(11):
        w2 = i * 0.1
        w1 = 1 - w2
        print "\n Weights", w1, w2
        team.runEverything(w1, w2)


if __name__ == '__main__':
    runWithDifferentWeights()
