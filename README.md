**Add path to file with logs in file "settings.json"  
example: "log1": "home\\user\\logs\\file_with_logs.txt"**  
  
# Example usage:  
```
import logany  
logany.save_log("log1", "Example log")
```
```
# File *file_with_logs.txt*:  
[2026-02-27 22:47:20] [id:8ju0zdvwdco54up]  Example log
              |                   |  
              |                   |  
              |                   |  
              ↓                   ↓  
           Time*     Random id (Doesn't repeat)
```
