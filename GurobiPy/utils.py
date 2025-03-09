import matplotlib.pyplot as plt

def plot_schedule(machines, machine_loads):
    plt.bar(machines, machine_loads)
    plt.xlabel('Machine')
    plt.ylabel('Total processing time')
    plt.title('Machine loads')

    # set x-axis ticks to be the machine numbers
    plt.xticks(machines)

    plt.show()