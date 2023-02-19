# Verifica se o Python está instalado
if (Get-Command python -ErrorAction SilentlyContinue) {
    Write-Host "Python já está instalado na máquina."
} else {
    Write-Host "Python não está instalado na máquina. Iniciando o download e instalação..."
    
    # Define a versão do Python a ser instalada
    $pythonVersion = "3.11.2"

    # Define o nome do arquivo de instalação
    $installerFile = "python-$pythonVersion-amd64.exe"

    # Define a URL do instalador do Python
    $installerUrl = "https://www.python.org/ftp/python/$pythonVersion/$installerFile"

    # Define o caminho onde o instalador será baixado
    $installerPath = "C:\Temp\$installerFile"

    # Baixa o instalador do Python
    Invoke-WebRequest -Uri $installerUrl -OutFile $installerPath

    # Instala o Python
    Start-Process -FilePath $installerPath -ArgumentList "/quiet", "PrependPath=1" -Wait

    # Remove o arquivo de instalação
    Remove-Item $installerPath

}

python .\net_py_tools.py