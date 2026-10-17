#!/usr/bin/env python3
import time
import os
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

DROP_ZONE = "./unreal_drops"
LAST_RUN = 0

class LatentLogisticsHandler(FileSystemEventHandler):
    def on_modified(self, event):
        global LAST_RUN
        # Listen exclusively for our custom Unreal Engine layout export
        if not event.is_directory and event.src_path.endswith("engine_layout.png"):
            now = time.time()
            # Prevent double-trigger anomalies during engine file operations
            if now - LAST_RUN > 2:
                LAST_RUN = now
                print(f"\n[+] PORTAL INTERCEPT: Live blueprint update detected at {event.src_path}")
                print("[+] GIGADREAM ENGINE: Translating optical matrices...")
                
                # Fire the dual-optics carrier script via the system shell
                subprocess.run(["python3", "carrier_optics_37.py", event.src_path])

if __name__ == "__main__":
    if not os.path.exists(DROP_ZONE):
        os.makedirs(DROP_ZONE)
        
    print(f"--- GIGADREAM PORTAL // 37 ONLINE: Monitoring drop zone: {DROP_ZONE} ---")
    handler = LatentLogisticsHandler()
    monitor = Observer()
    monitor.schedule(handler, path=DROP_ZONE, recursive=False)
    monitor.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        monitor.stop()
    monitor.join()
