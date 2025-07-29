import os
import json
from typing import Dict, Any

def generate_challenge_with_ai(difficulty: str) -> Dict[str, Any]:
  if difficulty == "easy":
    title = "Basic Python List Operation"
    options = ["my_list.append(5)", "my_list.add(5)", "my_list.push(5)", "my_list.insert(5)"]
    correct_answer_id = 0
    explanation = "In python, append() is the correct method to add an alement to the end of a list"
  
  elif difficulty == "medium":
    title = "Medium"
    options = ["temp", "temp", "temp", "temp"]
    correct_answer_id = 0
    explanation = "Temp"
  
  elif difficulty == "hard":
    title = "Hard"
    options = ["temp", "temp", "temp", "temp"]
    correct_answer_id = 0
    explanation = "Temp"
  
  return {
    "title": title,
    "options": options,
    "correct_answer_id": correct_answer_id,
    "explanation": explanation
  }