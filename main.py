import tkinter as tk
from tkinter import ttk
import chessboard_detection
import board_basics
from game_state_classes import Game_state
from tkinter.simpledialog import askstring
import ml_model
import chess
from PIL import ImageTk, Image
import cv2
import numpy as np
import time
import sys
import os
from game_state_classes import PositionChanged,NoValidPosition
import tensorflow as tf


function_parser = ""
sess = tf.InteractiveSession()



def clear_logs(logs_text):
    logs_text.delete('1.0', tk.END)
    #add_log("Logs have been cleared:")
