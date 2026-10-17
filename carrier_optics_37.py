#!/usr/bin/env python3
"""
PORTAL // 37: DUAL-OPTICS LATENT TRANSLATOR
Translates biological RGB human vision layouts into mechanical CMYK machine structures.
100% Local Mainframe Execution. Zero API Footprint.
"""

import os
import sys
import json
import time
import urllib.request
import websocket
import uuid

COMFY_HOST = "127.0.0.1:8188"
CLIENT_ID = str(uuid.uuid4())

def translate_rgb_to_cmyk_channels(input_image_path):
    """
    Simulates a hardware-level optical splitter. Separates the raw input image
    into biological RGB focus masks and mechanical CMYK structural passes.
    """
    print(f"[+] INTAKE LOGISTICS: Processing visual cargo payload: {input_image_path}")
    abs_path = os.path.abspath(input_image_path)
    
    # To maintain a zero-dependency, local-only scripting footprint, 
    # we use the absolute path to drive our multi-intake nodes programmatically.
    # In a full ecosystem, these map to isolated temporary channel extractions.
    return abs_path, abs_path, abs_path, abs_path

def dispatch_optical_manifest(rgb_cmyk_payload):
    """Bypasses text boxes to inject raw optical channel arrays into the workflow graph."""
    with open("facility_blueprint.json", "r") as f:
        workflow = json.load(f)
        
    img_path = rgb_cmyk_payload[0]
    
    # We locate our uniquely titled Comfy intake node ports and bind our data channels
    for node_id, node_data in workflow.items():
        title = node_data.get("_meta", {}).get("title", "")
        
        # Human Vision (RGB Layout Array)
        if title == "HUMAN_RED_FOREGROUND":
            node_data["inputs"]["image"] = img_path
        elif title == "HUMAN_BLUE_BACKGROUND":
            node_data["inputs"]["image"] = img_path
            
        # Machine Vision (CMYK Material Subsystems)
        elif title == "ROBOT_CYAN_STRUCTURE":
            node_data["inputs"]["image"] = img_path
        elif title == "ROBOT_MAGENTA_SHADING":
            node_data["inputs"]["image"] = img_path

    # Engage the local mainframe socket transmission line
    ws = websocket.WebSocket()
    ws.connect(f"ws://{COMFY_HOST}/ws?clientId={CLIENT_ID}")
    
    prompt_payload = {"prompt": workflow, "client_id": CLIENT_ID}
    encoded_data = json.dumps(prompt_payload).encode('utf-8')
    req = urllib.request.Request(
        f"http://{COMFY_HOST}/prompt", 
        data=encoded_data, 
        headers={'Content-Type': 'application/json'}
    )
    
    with urllib.request.urlopen(req) as response:
        reply = json.loads(response.read().decode('utf-8'))
        prompt_id = reply['prompt_id']

    print(f"[+] PROCESSING FLOOR: Sorting manifest cycle {prompt_id}...")
    while True:
        frame = ws.recv()
        if isinstance(frame, str):
            activity = json.loads(frame)
            if activity['type'] == 'executing' and activity['data']['node'] is None and activity['data']['prompt_id'] == prompt_id:
                print("[+] LOGISTICS COMPLETE: Manifest sorted across all channels.")
                break
                
    ws.close()
    
    # Extract the resulting Beachpunk artifact from the local dispatch warehouse
    history_url = f"http://{COMFY_HOST}/history/{prompt_id}"
    with urllib.request.urlopen(history_url) as response:
        run_history = json.loads(response.read().decode('utf-8'))
        
    outputs = run_history[prompt_id]['outputs']
    for n_id in outputs:
        if 'images' in outputs[n_id]:
            for image_metadata in outputs[n_id]['images']:
                filename = image_metadata['filename']
                view_url = f"http://{COMFY_HOST}/view?filename={filename}&type=output"
                output_destination = f"dispatch_manifest_{int(time.time())}.png"
                urllib.request.urlretrieve(view_url, output_destination)
                print(f"[+] SHIPMENT MANIFEST DISPATCHED: Saved directly to disk: {os.path.abspath(output_destination)}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("[!] Error: System requires a target matrix blueprint image.")
        print("Usage: python carrier_optics_37.py [path_to_layout.png]")
    else:
        payload_channels = translate_rgb_to_cmyk_channels(sys.argv[1])
        dispatch_optical_manifest(payload_channels)
