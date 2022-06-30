from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import tensorflow as tf
import numpy as np
app = FastAPI()


app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_methods=["GET"],
  allow_headers=["*"]
)

model = tf.saved_model.load("./twilightify")

@app.get("/")
def get_twilight(q:str = "Twilight:",chars=""):
  next_char = tf.constant([q])
  result = [next_char]

  for n in range(1000):
    next_char, states = model.generate_one_step(next_char, states=states)
    result.append(next_char)
  result = tf.strings.join(result)
  return {"result": result[0].numpy().decode('utf-8')}