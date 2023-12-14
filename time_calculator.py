def add_time(start, duration, start_day):
  # Parsear la hora de inicio y la duración
  start_hour, start_minute, period = list(map(str.strip, start[:-6].split(":"))), int(start[-5:-3]), start[-3:]
  duration_hour, duration_minute = map(int, duration.split(":"))

  # Convertir la hora de inicio a minutos y sumar la duración
  total_minutes = int(start_hour[0]) * 60 + start_minute
  total_minutes += duration_hour * 60 + duration_minute

  # Calcular nuevas horas y minutos
  new_hour = (total_minutes // 60) % 12
  new_minute = total_minutes % 60

  # Calcular si es AM o PM
  new_period = "AM" if total_minutes // 60 < 12 else "PM"

  # Calcular el número de días después
  days_later = total_minutes // (12 * 60)

  # Construir el resultado
  new_time = f"{new_hour}:{str(new_minute).zfill(2)} {new_period}"

  if days_later == 1:
      new_time += " (next day)"
  elif days_later > 1:
      new_time += f" ({days_later} days later)"

  # Agregar el día de la semana si se proporciona
  if start_day:
      start_day = start_day.lower()
      days_of_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
      start_day_index = days_of_week.index(start_day)
      days_later += start_day_index

  return new_time


if __name__ == '__main__':
  print(add_time())