import pyqrcode
import os
import sys
import tkinter as tk
from tkinter import filedialog

try:
    from rich.console import Console
except ImportError:
    print("Hata: 'rich' kütüphanesi eksik.")
    sys.exit()

console = Console()

def print_banner():
    # Blok Q Logosu
    ascii_q = r"""
  ██████╗  ██████╗       ██████╗ ███████╗███╗   ██╗
 ██╔═══██╗ ██╔══██╗     ██╔════╝ ██╔════╝████╗  ██║
 ██║   ██║ ██████╔╝     ██║  ███╗█████╗  ██╔██╗ ██║
 ██║▄▄ ██║ ██╔══██╗     ██║   ██║██╔══╝  ██║╚██╗██║
 ╚██████╔╝ ██║  ██║     ╚██████╔╝███████╗██║ ╚████║
  ╚══▀▀═╝  ╚═╝  ╚═╝      ╚═════╝ ╚══════╝╚═╝  ╚═══╝

    """
    lines = [line for line in ascii_q.splitlines() if line.strip()]
    total_lines = len(lines)
    for i, line in enumerate(lines):
        # Sarıdan yeşile geçiş (RGB hesaplama)
        r = int(255 * (1 - i / (total_lines - 1))) if total_lines > 1 else 255
        color_hex = f"rgb({r},255,0)"
        console.print(line, style=color_hex)
    console.print("    https://www.youtube.com/@S_P1RE",)
    console.print("    By sp1re", style="rgb(0,255,0) italic")
    print("    " + "-" * 45)

def dosya_yolu_sec():
    # Arka planda boş bir tkinter penceresi açılmasını engellemek için
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True) # Pencereyi en üste getir
    
    yol = filedialog.asksaveasfilename(
        title="QR Kodu Kaydedilecek Yeri Seçin",
        defaultextension=".svg",
        filetypes=[("SVG Dosyası", "*.svg"), ("Tüm Dosyalar", "*.*")]
    )
    root.destroy()
    return yol

def qr_olustur():
    os.system('cls' if os.name == 'nt' else 'clear')
    print_banner()
    
    url = input("\n[?] QR URL: ").strip()

    if url:
        # Kayıt yerini seçmek için pencereyi açıyoruz
        console.print("[yellow][*] Lütfen kayıt yerini seçin...[/yellow]")
        kayit_yolu = dosya_yolu_sec()

        if kayit_yolu:
            try:
                qr = pyqrcode.create(url)
                qr.svg(kayit_yolu, scale=8)
                
                console.print(f"\n[bold green][+] Başarılı![/bold green]")
                console.print(f"[bold cyan][ℹ] Kayıt Yeri:[/bold cyan] {kayit_yolu}")
            except Exception as e:
                console.print(f"\n[bold red][!] Hata oluştu:[/bold red] {e}")
        else:
            console.print("\n[bold yellow][!] İşlem iptal edildi (Yer seçilmedi).[/bold yellow]")
    else:
        console.print("\n[bold yellow][!] URL girmediniz!")

if __name__ == "__main__":
    qr_olustur()