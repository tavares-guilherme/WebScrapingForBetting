import numpy as np
from match import match

class methods(object):
	
	def under_over(m):

		result = 0

		# - To-do: Round float values -- FIX
		
		a1 = (m.goals_table_a[1][0]/m.games_played_a[1] + m.goals_table_b[3][0/m.games_played_b[1]])/2
		b1 = (m.goals_table_b[1][0]/m.games_played_b[1] + m.goals_table_a[3][0/m.games_played_a[1]])/2

		a2 = (m.goals_table_a[1][1]/m.games_played_a[0] + m.goals_table_b[3][1]/m.games_played_b[0])/2
		b2 = (m.goals_table_b[1][1]/m.games_played_b[0] + m.goals_table_a[3][1]/m.games_played_a[0])/2

		n1 = (a1*0,7) + (a2*0,3)
		n2 = (b2*0,7) + (b2*0,3)

		o1 = ( ((1-m.goals_table_a[6][0]) * m.goals_table_a[1]) + (1-m.goals_table_b[6][0]) * m.goals_table_b[1])
		o2 = ( (m.goals_table_a[6][1] * m.goals_table_a[1]) + (m.goals_table_b[6][0] * m.goals_table_b[1]))

		p1 = ( ((1-m.goals_table_a[6][1]) * m.goals_table_a[0]) + (1-m.goals_table_b[6][1]) * m.goals_table_b[0])
		p2 = ( (m.goals_table_a[6][1] * m.goals_table_a[0]) + (m.goals_table_b[6][1] * m.goals_table_b[0])) 
		
		q1 = ((o1*0,7) + (p1*0,3))/2
		q2 = ((o2*0,7) + (p2*0,3))/2

		result = (n1+n2) * (1-q1-q2)

		print(result)
		if(result < 2): print("Under")
		else:
			if(result>3):print("Over")
			else: print("no bet")
