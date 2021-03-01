from LeagueStats import LeagueStats
from methods import methods
import numpy as np

leagues = ["brazil", "england", "italy", "germany", "portugal", "spain"]

controller = 1

while(controller != 0):
	print("Insira uma liga")
	league = input()

	if(league in leagues):
		stats = LeagueStats(league)
		for i in range(0, len(stats.match_list)):
			methods.under_over(stats.match_list[i])
