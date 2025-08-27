{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  name = "python-dev-shell";
  
  buildInputs = with pkgs; [
    python3
    python3Packages.pip
    python3Packages.virtualenv
  ];
  
  shellHook = ''
    if [ ! -d ".venv" ]; then
      python -m venv .venv
    fi
    
    source .venv/bin/activate
    
    echo "Python development environment ready!"
    echo "Virtual environment: .venv/"
  '';
}
