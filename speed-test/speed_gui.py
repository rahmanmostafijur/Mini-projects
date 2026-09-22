import tkinter as tk
import speedtest
import threading


def start_test():
    button.config(state="disabled")
    label.config(text="Testing... please wait")

    thread = threading.Thread(target=worker, daemon=True)
    thread.start()


def worker():
    try:
        st = speedtest.Speedtest()
        download = st.download() / 1_000_000
        upload = st.upload() / 1_000_000
        ping = st.results.ping
        result = (
            f"Download: {download:.2f} Mbps\n"
            f"Upload: {upload:.2f} Mbps\n"
            f"Ping: {ping:.0f} ms"
        )
    except Exception as error:
        result = f"Failed: {error}"

    root.after(0, show_result, result)


def show_result(text):
    label.config(text=text)
    button.config(state="normal")

root = tk.Tk()
root.title("Speed Test")
root.geometry("600x500")

label = tk.Label(root, text="Ready", font=("Helvetica", 16))
label.pack(pady=40)

button = tk.Button(root, text="Run Speed Test", command=start_test, font=("Times New Roman", 14))
button.pack()

root.mainloop()
