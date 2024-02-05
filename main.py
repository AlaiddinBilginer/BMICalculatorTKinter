import tkinter

window = tkinter.Tk()
window.minsize(width=300, height=300)
window.maxsize(width=300, height=300)
window.configure(bg="#68EEEA", pady=20, padx=20)
window.title("BMI Calculator")

img = tkinter.PhotoImage(file="bmi.png")
window.iconphoto(False, img)

#Title Label
titleLabel = tkinter.Label(text="BMI Calculator", font=("Verdena", 20, "normal"))
titleLabel.config(bg="#FFC300", pady=10)
titleLabel.pack()

#Weight Label
weightLabel = tkinter.Label(text="What is your weight?(kg)", font=("Verdena", 10, "bold"))
weightLabel.place(x=50, y=70)

#Weight Input
weightEntry = tkinter.Entry(width=20)
weightEntry.place(x=68, y=95)

#Height Label
heightLabel = tkinter.Label(text="What is your height?(cm)", font=("Verdena", 10, "bold"))
heightLabel.place(x=48, y=125)

#Height Input
heightEntry = tkinter.Entry(width=20)
heightEntry.place(x=68, y=150)

def calculateBMI(weight, height):
    return weight / float((height/100) ** 2)

#Calculate Button
resultLabel = tkinter.Label(text=" ")
def clickedButton():
    resultLabel.config(text="")
    try:
        bmi = calculateBMI(int(weightEntry.get()), int(heightEntry.get()))
        if bmi <= 18.4:
            state = "underweight"
        elif bmi > 18.4 and bmi <= 24.9:
            state = "normal"
        elif bmi > 24.9 and bmi <= 39.9:
            state = "overweight"
        else:
            state = "obese"

        resultLabel.config(text=f"Your BMI value is {bmi: .2f}, you are {state}.")
        resultLabel.pack(side="bottom")
        resultLabel.config(font=("Verdena", 8, "bold"))
    except ValueError:
        resultLabel.config(text="Please enter the correct values")


calculateButton = tkinter.Button(text="Calculate BMI", command=clickedButton)
calculateButton.config(bg="#30BB43", fg="white")
calculateButton.place(x=87, y=180)

#Result Label


window.mainloop()