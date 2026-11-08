import string
def main():
  password = input("Введите пароль: ")
  errors = []
  if len(password) != 8:
    errors.append("Длина пароля не равна 8")
  if password == password.lower() or not any(c.isupper() for c in password):
    errors.append("В пароле отсутствуют заглавные буквы")
  if password == password.upper() or not any(c.islower() for c in password):
    errors.append("В пароле отсутствуют строчные буквы")
  if not any(c.isdigit() for c in password):
    errors.append("В пароле отсутствуют цифры")
  special_chars = "*–#"
  if not any(c in special_chars for c in password):
    errors.append("В пароле отсутствуют специальные символы")
  allowed = (
      string.ascii_uppercase
      + string.ascii_lowercase
      + string.digits
      + "*–#"
  )
  if not all(c in allowed for c in password):
    errors.append("В пароле используются непредусмотренные символы")

  if not errors:
    print("Надежный пароль")
  else:
    for err in errors:
      print(err)
if __name__ == "__main__":
  main()