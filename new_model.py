#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 19:06:55 2018

@author: chloe
"""
import random
import operator
import matplotlib.pyplot
import agentframework
import csv
import matplotlib.animation

# Create new list for environment
environment = []
# Create new variable which defines the number of agents
num_of_agents = 10
# Create number of iterations
num_of_iterations = 100
# Create the neighbourhood for the agents to interact
neighbourhood = 20
# Create an empty list called agents
agents = []

a = agentframework.Agent(environment, agents)

# Open csv file
f = open('in.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:
    rowlist = []
    for value in row:				
        rowlist.append(value)
    environment.append(rowlist)
f.close()

# Create a for loop that appends a list with num_of_agents agent coordinates
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))
    
# Create the map figure
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

# Move the agents
def update(frame_number):
    global carry_on 
    
    fig.clear()   
    matplotlib.pyplot.imshow(environment) 
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
        
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y, color="black")
        
    matplotlib.pyplot.ylim(0, 100)
    matplotlib.pyplot.xlim(0, 100)

for x in range(num_of_agents):
    for z in range(x + 1,num_of_agents):
        distance = agents[x].distance_between(agents[z])

animation = matplotlib.animation.FuncAnimation(fig, update, repeat=False)
matplotlib.pyplot.show()
animation.save("leeds_final.gif", writer="imagemagick")
