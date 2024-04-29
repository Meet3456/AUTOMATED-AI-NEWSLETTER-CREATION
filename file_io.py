from datetime import datetime


def save_output_as_markdwon(task_output):

  today_date = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

  filename = f"{today_date}.md"

  with open(filename,'w') as file:
    file.write(task_output.result)
  
  print(f"Newsletter saved as {filename}")