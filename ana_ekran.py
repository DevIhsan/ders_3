import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage  # Resim eklemek için PhotoImage kullanılır
from PIL import Image, ImageTk
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from passlib.hash import sha256_crypt