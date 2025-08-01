echo "xX Device Fingerprint Report Xx"
echo "-----------------------------------"
echo "Hostname: $(hostname)"
echo "OS: $(uname -s) $(uname -r)"
echo "Architecture: $(uname -m)"
echo "Uptime: $(uptime | awk '{print $3,$4}' | sed 's/,//')"
echo "IP Address: $(ip a | grep inet | grep -v 127.0.0.1 | head -n1 | awk '{print $2}')"
echo "Disk Usage:"
df -h / | tail -n1
echo "Memory Used:"
free -m | awk 'NR==3{printf "%.2f%%\n", $3*100/$2 }'
