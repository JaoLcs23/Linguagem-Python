import tkinter as tk
from tkinter import messagebox

hotel = {101: 1, 102: 1, 103: 0, 104: 1, 105: 0}
reservas = []

def quartosDisponiveis():
    disponiveis = [numero_quarto for numero_quarto, disponivel in hotel.items() if disponivel]
    if disponiveis:
        messagebox.showinfo("Quartos Disponíveis", f"Quartos disponíveis: {', '.join(map(str, disponiveis))}")
    else:
        messagebox.showinfo("Quartos Disponíveis", "Nenhum quarto disponível no momento.")

def fazerReserva():
    try:
        numero_quarto = int(entrada_quarto.get())
        nome_hospede = entrada_nome.get().strip()
        
        if not nome_hospede:
            messagebox.showwarning("Erro", "O nome do hóspede não pode estar vazio.")
            return
        
        if hotel.get(numero_quarto) == 1:
            hotel[numero_quarto] = 0
            reservas.append({"numero_quarto": numero_quarto, "nome_hospede": nome_hospede})
            messagebox.showinfo("Reserva", f"Reserva feita para o quarto {numero_quarto} para {nome_hospede}.")
        else:
            messagebox.showwarning("Erro", f"O quarto {numero_quarto} não está disponível ou não existe.")
        
        atualizarInterface()
    except ValueError:
        messagebox.showwarning("Erro", "Por favor, insira um número válido para o quarto.")

def cancelarReserva():
    try:
        numero_quarto = int(entrada_quarto.get())
        
        for reserva in reservas:
            if reserva["numero_quarto"] == numero_quarto:
                reservas.remove(reserva)
                hotel[numero_quarto] = 1
                messagebox.showinfo("Cancelamento", f"Reserva para o quarto {numero_quarto} foi cancelada.")
                atualizarInterface()
                return
        
        messagebox.showwarning("Erro", f"Reserva para o quarto {numero_quarto} não encontrada.")
    except ValueError:
        messagebox.showwarning("Erro", "Por favor, insira um número válido para o quarto.")

def atualizarInterface():
    lista_quartos.delete(0, tk.END)
    for numero_quarto, disponivel in hotel.items():
        status = "Disponível" if disponivel else "Reservado"
        lista_quartos.insert(tk.END, f"Quarto {numero_quarto}: {status}")

root = tk.Tk()
root.title("Sistema de Reservas de Hotel")

frame_info = tk.Frame(root)
frame_info.pack(pady=10)

tk.Label(frame_info, text="Número do Quarto:").grid(row=0, column=0, padx=5)
entrada_quarto = tk.Entry(frame_info)
entrada_quarto.grid(row=0, column=1, padx=5)

tk.Label(frame_info, text="Nome do Hóspede:").grid(row=1, column=0, padx=5)
entrada_nome = tk.Entry(frame_info)
entrada_nome.grid(row=1, column=1, padx=5)

frame_botoes = tk.Frame(root)
frame_botoes.pack(pady=10)

btn_disponiveis = tk.Button(frame_botoes, text="Quartos Disponíveis", command=quartosDisponiveis)
btn_disponiveis.grid(row=0, column=0, padx=5)

btn_reserva = tk.Button(frame_botoes, text="Fazer Reserva", command=fazerReserva)
btn_reserva.grid(row=0, column=1, padx=5)

btn_cancelar = tk.Button(frame_botoes, text="Cancelar Reserva", command=cancelarReserva)
btn_cancelar.grid(row=0, column=2, padx=5)

frame_quartos = tk.Frame(root)
frame_quartos.pack(pady=10)

tk.Label(frame_quartos, text="Status dos Quartos:").pack()

lista_quartos = tk.Listbox(frame_quartos, width=40, height=10)
lista_quartos.pack()

atualizarInterface()

root.mainloop()
