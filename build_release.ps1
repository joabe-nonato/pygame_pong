$ErrorActionPreference = "Stop"

Write-Host "Gerando executavel com PyInstaller..."

python -m PyInstaller --noconfirm --clean --onefile --windowed --name pygame_pong --distpath release --workpath build --specpath build main.py

Write-Host "Build concluido. Confira a pasta 'release'."
