import matplotlib.pyplot as plt

from random_walk import RandomWalk

# We can generate various patterns of walks as long as the program is active.
while True: 
    # Make a random walk. By inserting values inside the parenthesis we can control how many point we see. 
    rw = RandomWalk(50_000)
    rw.fill_walk()

    # Plot the points in the walk. 
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15,9))
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
        edgecolors= 'none', s=1)
    # When the size of the plots are 's=15', all the points cant fit and wont show on the graph.

    # Emphasisze the first and last points. To show where the walk started and ended.
    ax.scatter(0,0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    
    # Now lets removes the axises from the graph so that it's less distracting
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break

