import numpy as np
from match import match

class methods(object):
	
	def under_over(m):

		result = 0

		# - To-do: Round float values -- FIX
		
		l1 = (m.goals_table_a[1][0]/m.games_played_a[0] + m.goals_table_b[3][0]/m.games_played_b[0])/2
		l2 = (m.goals_table_b[1][0]/m.games_played_b[0] + m.goals_table_a[3][0]/m.games_played_a[0])/2

		m1 = (m.goals_table_a[1][1]/m.games_played_a[1] + m.goals_table_b[3][1]/m.games_played_b[1])/2
		m2 = (m.goals_table_b[1][1]/m.games_played_b[1] + m.goals_table_a[3][1]/m.games_played_a[1])/2

		n1 = l1*0.7 + m1*0.3
		n2 = l2*0.7 + m2*0.3

		o1 = round( (1 - m.goals_table_a[7][0])*m.games_played_a[0])/m.games_played_a[0] + round((1 - m.goals_table_b[7][0])*m.games_played_b[0])/m.games_played_b[0]
		o2 = round(m.goals_table_a[7][0]*m.games_played_a[0])/m.games_played_a[0] + round(m.goals_table_b[7][0]*m.games_played_b[0])/m.games_played_b[0]

		p1 = round((1 - m.goals_table_a[7][1])*m.games_played_a[1])/m.games_played_a[1] + round((1 - m.goals_table_b[7][1])*m.games_played_b[1])/m.games_played_b[1]
		p2 = round(m.goals_table_a[7][1]*m.games_played_a[1])/m.games_played_a[1] + round(m.goals_table_b[7][1]*m.games_played_b[1])/m.games_played_b[1]

		q1 = (o1*0.7 + p1*0.3)/2
		q2 = (o2*0.7 + p2*0.3)/2

		result = (n1+n2) * (1 - (q1 - q2))

		print(result)
		if(result < 2): print("Under")
		else:
			if(result>3):print("Over")
			else: print("no bet")
