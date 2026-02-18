import time

def animate_text(label, base_text, duration=1000, dots_interval=500, end_text=None, dots=0, start_time=None):
    if start_time is None:
        start_time = int(time.time() * 1000)

    #Affichage du texte avec point
    label.config(text=base_text + "." * dots)

    elapsed = int(time.time() * 1000) - start_time
    if elapsed < duration:
        dots = (dots + 1) % 4
        label.after(dots_interval, lambda: animate_text(label, base_text, duration, dots_interval, end_text, dots, start_time))
    else:
        if end_text:
            label.config(text=end_text)