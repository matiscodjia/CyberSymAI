#!/usr/bin/env fish

set pipe "signal.pipe"
set script_path "extract_features.py"
set python_bin (which python3)
echo "🔄 Extractor en attente de signaux..."
while true
    read signal < $pipe
    echo "📥 Signal reçu, lancement de l'extraction"
    python3 $script_path
end