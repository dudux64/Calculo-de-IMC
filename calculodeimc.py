import dearpygui.dearpygui as dpg

dpg.create_context()
def calcular_imc():

    peso = dpg.get_value ("peso")
    altura = dpg.get_value ("altura")
    try:
        peso = float(peso)
        altura = float(altura)
        imc = peso / (altura ** 2)
    

        if imc < float(18.5):
            resultado_imc = "Você está na categoria MAGREZA"
        elif imc > float(18.5) and imc < float(24.9):
           resultado_imc = "Você está na categoria NORMAL"
        elif imc > float(24.9) and imc < float(29.9):
           resultado_imc = "Você está na categoria SOBREPESO"
        elif imc > float(29.9) and imc < float(39.9):
           resultado_imc = "Você está na categoria OBESIDADE"
        elif imc > float(39.9):
           resultado_imc = "Você está na categoria OBESIDADE GRAU 2 "
        else:
           resultado_imc = "Operação Incorreta!"
    
        if imc >0: 
            dpg.set_value("resultado", f"Seu IMC final é {imc:,.2f}")
        dpg.set_value("resultado2", resultado_imc)
    
    except ValueError:
        dpg.set_value("resultado","Por favor, insira valores numéricos válidos")


dpg.create_viewport(title='Calculadora de peso IMC', width=700, height=300)

with dpg.window(label="Calculadora IMC", width=700, height=300):
    dpg.add_input_text(label="Peso", tag="peso")
    dpg.add_input_text(label="Altura", tag="altura")
    dpg.add_button(label="Calcular IMC", callback=calcular_imc)
    dpg.add_text("", tag="resultado")
    dpg.add_text("", tag= "resultado2")


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()


