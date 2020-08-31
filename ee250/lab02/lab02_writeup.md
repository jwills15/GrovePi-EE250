Joshua Williams
Lab 2
Repo: https://github.com/jwills15/GrovePi-EE250/tree/lab02
Video Demo: 
Reflection Questions:

1. Cloned a new respository, add a second file "my_second_file.py" and
push to Github:
    git clone git@github.com:my-name/my-imaginary-repo.git
    cd my-imaginary-repo
    touch my_second_file.py
    git add my_second_file.py
    git commit -m "Created my_second_file.py"
    git push origin master

2. Workflow for this lab and improvements:
    I developed on my VM with Visual Studio Code and then push/pulled to get
    my code on my RPi. To be more efficient in the next lab, I want to learn
    how to use Vim within Visual Studio Code. Vim makes navigating code quicker
    and can be installed directly as an extension in Visual Studio Code. I
    also use VS Code in my other CS courses, so learning to use Vim would be
    benifical for those classes as well.

3. What is the delay when only ultrasonicRead() is called? What communication
protocol does the RPi use to communicate with the Atmega328P on the GrovePi
when it tries to read the ultrasonic ranger output?
    The constant delay is 0.06 seconds. The function ultrasonicRead() sets a
    delay of 0.06 seconds because, as the comment in the function states, the
    firmware has a time of 50 milliseconds so the read of the data must wait
    longer than that.
    The RPi communicates with I2C protocol.