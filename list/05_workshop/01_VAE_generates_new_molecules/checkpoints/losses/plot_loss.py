import pandas as pd
import matplotlib.pyplot as plt

def plot_and_save(df, model):
    fig = plt.figure(figsize = (7, 4))
    if model == 'vae':
        c = 'blue'
    else:
        c = 'orange'
    plt.plot(df['loss'], color=c, marker='o', linewidth=1, markersize=3)
    plt.ylabel("Loss")
    plt.xlabel("Epoch")
    plt.title(f'Model training: {model}')
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.savefig(f'img/{model}_loss.png')

df_vae = pd.read_csv('vae_epoch100.csv')
df_cvae = pd.read_csv('cvae_epoch100.csv')

plot_and_save(df_vae, 'vae')
plot_and_save(df_cvae, 'cvae')