# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 00:39:52 2022

@author: Charissa
"""

import tkinter as tk
import secrets

window = tk.Tk()


def scissorspaperstone():
    letsplay = tk.Label(text = "Let's play scissors, paper, stone!")
    letsplay.grid(row =0, column = 0)
    scissors = tk.Button(window, text = "✂️", command = playscissors)
    scissors.grid(row = 2, column = 1)
    paper = tk.Button(window, text = "📄", command = playpaper)
    paper.grid(row = 2, column = 2)
    stone = tk.Button(window,text = "🪨", command = playstone)
    stone.grid(row=2, column = 3)
    
def playscissors():
    opt = botoption()
    val = tk.Label(text = "Computer chose " + str(opt))
    val.grid(row = 3, column = 0)
    if opt == "✂️":
        result = tk.Label(text = "Tie!")
    if opt == "📄":
        result = tk.Label(text = "You win!")
    if opt =="🪨":
        result = tk.Label(text = "You lose!")
    result.grid(row = 4, column = 0)

def playpaper():
    opt = botoption()
    val = tk.Label(text = "Computer chose " + str(opt))
    val.grid(row = 3, column = 0)
    if opt == "✂️":
        result = tk.Label(text = "You lose!")
    if opt == "📄":
        result = tk.Label(text = "Tie!")
    if opt =="🪨":
        result = tk.Label(text ="You win!")
    result.grid(row = 4, column = 0)
    
def playstone():
    opt = botoption()
    val = tk.Label(text = "Computer chose " + str(opt))
    val.grid(row = 3, column = 0)
    if opt == "✂️":
        result = tk.Label(text = "You win!")
    if opt == "📄":
        result = tk.Label(text = "You lose!")
    if opt =="🪨":
        result = tk.Label(text = "Tie!")
    result.grid(row = 4, column = 0)
    
def botoption():
    lt = ["✂️", "📄","🪨"]
    option = secrets.randbelow(3)
    return lt[option]

scissorspaperstone()
window.mainloop()