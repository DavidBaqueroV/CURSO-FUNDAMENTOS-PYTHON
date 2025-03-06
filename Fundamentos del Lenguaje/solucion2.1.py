motor = input("Pulse 1 para encender el motor")

if motor == "0":
    print("Motor apagado")
elif motor == "1":
    motor_temp = int(input("digite la temperatura del motor: "))
    print("Motor encendido")
    if motor_temp == 80:
        print("excede la temperatura\n" + "apagando el motor...")