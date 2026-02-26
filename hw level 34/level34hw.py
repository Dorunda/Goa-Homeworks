#custom-ფუნქციები არის ჩვენს მიერ შექმნილი ფუნქცია რომელსაც ჩვენთვითონ ვქმნით კონკრეტული ამოცანის შესასრულებლად
#ვიყენებთ იმისთვის რომ ავიცილოთ კოდის განმეორება
#ასევე ვიყენებთ კოდი რომ განმარტივდეს და გაიწმინდოს
#მას დანაშნულება გააჩნია გამოთვლების შესრულებისთვის
#მონაცემების დამუშავებისთვის
#მნიშვნელობის დაბრუნებისთვის
#ის იქმნება def ატრიბუტით ვწერთ def-ს ვწერთ ფუნქციის სახელს და ვუწერთ ორ წერტილს 
#და ასევე ვუწერთ ფრჩხილებს და ვწერთ greet-ს რომელიც ბეჭდავს ტექსტს


def hello_python(num1, num2):
    return num1 + num2
result = hello_python(10, 15)
print(result)
    

def chech_even(number):
    if number % 2 == 0:
        print("რიცხვი არის ლუწი")
    else:
        print("რიცხვი არის კენტი")
chech_even(10)
chech_even(7)


def number_1(number):
    return number ** 3
result = number_1(7)
print(result)



def gamarjoba_saqartvelo(text):
    return text.upper()
result = gamarjoba_saqartvelo("GAMARJOBA SAQARTVELO")
print(result)


def name_surname(name, surname):
    return f"ჩემი სახელია {name} ჩემი გვარია {surname}"
print(name_surname("ილია", "გონგლაძე"))




