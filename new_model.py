#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 19:06:55 2018

@author: chloe
"""
# Import relevant packages
import matplotlib.pyplot
import agentframework
import csv
import matplotlib.animation

environment = [] # Empty list for environment
num_of_agents = 10 # Define the number of agents
num_of_iterations = 100 # Create number of iterations
neighbourhood = 20 # Create the neighbourhood for the agents to interact
agents = [] # Empty list of the Agents

# Open 'environment' csv file 
f = open('in.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
# Append 'environment' csv file to environment list as coordinates
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

# Apply the agents behaviours
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

# This can be used to calculate the distance between the agents
for x in range(num_of_agents):
    for z in range(x + 1,num_of_agents):
        distance = agents[x].distance_between(agents[z])

# Animate the model until the stopping condition has been met
animation = matplotlib.animation.FuncAnimation(fig, update, repeat=False)
matplotlib.pyplot.show()
#animation.save("leeds_final.gif", writer="imagemagick")
