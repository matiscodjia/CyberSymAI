#!/usr/bin/env fish

set pipe "signal.pipe"
set python_bin (which python3)
# Créer le pipe si nécessaire
if not test -p $pipe
    mkfifo $pipe
end

# Lancer extractor en arrière-plan
fish extractor.fish &
set extractor_pid $last_pid

# Lancer listener au premier plan
fish listener.fish

# Quand listener se termine, on arrête extractor
kill $extractor_pid

echo "✅ Pipeline terminée."