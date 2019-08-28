import matplotlib.pyplot as plt

fig = plt.figure(figsize=(7,5))

seasons = ["S3", "S4","S5","S6","S7","S8"] #LCS/Pro seasons
x = [6.3, 8.6,8.4,8.7,8.9,9.6] #Bjergsen cs per min
y = [8.8,9.2,9.5,9.6] #Jensen cs per min


positions = [0, 1, 2, 3, 4, 5]
positions2 = [2.20,3.20,4.20,5.20]
positions3 = [0,1,2.05,3.05,4.05,5.05]


#adjusting bar widths on the graph

plt.bar(positions,x, width=0.30)
plt.bar(positions2,y, width=0.30)

#adding legend

bjerg_legend = 'Bjergsen','Jensen'



#adjusting positioning of X axis ticks
plt.xticks(positions3, seasons)

#setting the title of the bar graph
plt.title("Bjergsen & Jensen, Average CS/Min By Season")

#setting x and y "titles" or labels on the bar graph
plt.xlabel('Season')
plt.ylabel('CS/Min')

#setting custom legend so outsiders will know which bar correlates to which player
plt.legend(bjerg_legend)

#prints the graph to the screen
plt.show()
