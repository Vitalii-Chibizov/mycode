import numpy as np
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt

def main():
    fibonacci_limit = 1000  # Set the limit for the Fibonacci sequence
    fibonacci_sequence = [0, 1]

    # Generate the Fibonacci sequence up to the specified limit
    while fibonacci_sequence[-1] + fibonacci_sequence[-2] <= fibonacci_limit:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    # Calculate coordinates for a Fibonacci spiral
    x = [0]
    y = [0]
    angle = 90  # Initial angle
    length = 1   # Initial length

    for number in fibonacci_sequence:
        angle_rad = np.radians(angle)
        x.append(x[-1] + length * np.cos(angle_rad))
        y.append(y[-1] + length * np.sin(angle_rad))
        angle += 90  # Rotate 90 degrees for each Fibonacci number
        length = number  # Set length based on the Fibonacci number

    # Plot the Fibonacci spiral
    plt.plot(x, y, marker='o', linestyle='-')
    plt.title("Fibonacci Spiral")
    plt.xlabel("X")
    plt.ylabel("Y")

    # Save the plot as a PDF
    plt.savefig("/home/student/mycode/graphing/fibonacci_spiral.pdf")

if __name__ == "__main__":
    main()

