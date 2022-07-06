from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tensorflow import saved_model, strings, constant
app = FastAPI()


app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_methods=["GET"],
  allow_headers=["*"]
)

twilight_model = saved_model.load("./twilightify")
philip_model = saved_model.load("./Philipify")

@app.get("/")
def get_twilight(q:str = "What manner of sorcery is this?",chars:int=1000):
  states = None
  next_char = constant([q])
  result = [next_char]

  for n in range(chars):
    next_char, states = twilight_model.generate_one_step(next_char, states=states)
    result.append(next_char)
  result = strings.join(result)
  return {"result": result[0].numpy().decode('utf-8')}

@app.get("/philip")
def get_philip(q:str = "Twilight:",chars:int=1000):
  states = None
  next_char = constant([q])
  result = [next_char]

  for n in range(chars):
    next_char, states = philip_model.generate_one_step(next_char, states=states)
    result.append(next_char)
  result = strings.join(result)
  return {"result": result[0].numpy().decode('utf-8')}