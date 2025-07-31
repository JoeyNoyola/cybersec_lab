echo "Starting backup..."
tar -czf ~/backups/$(date +%Y-%m-%d).tar.gz /home/user/Documents/
echo "Backup complete!"
