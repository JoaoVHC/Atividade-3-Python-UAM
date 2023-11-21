# Link no Github: https://github.com/JoaoVHC/Atividade-3-Python-UAM

import json

with open('textodesafio.txt', 'r') as file:
    json_dict = json.load(file)
  
with open('jsonarquivado.txt', '+w') as file:
    json.dump(json_dict, file, indent=4)
  
print(json.dumps(json_dict, indent=4))

{
    "menu": {
        "header": "SVG Viewer",
        "items": [
            {
                "id": "Open"
            },
            {
                "id": "OpenNew",
                "label": "Open New"
            },
            null,
            {
                "id": "ZoomIn",
                "label": "Zoom In"
            },
            {
                "id": "ZoomOut",
                "label": "Zoom Out"
            },
            {
                "id": "OriginalView",
                "label": "Original View"
            },
            null,
            {
                "id": "Quality"
            },
            {
                "id": "Pause"
            },
            {
                "id": "Mute"
            },
            null,
            {
                "id": "Find",
                "label": "Find..."
            },
            {
                "id": "FindAgain",
                "label": "Find Again"
            },
            {
                "id": "Copy"
            },
            {
                "id": "CopyAgain",
                "label": "Copy Again"
            },
            {
                "id": "CopySVG",
                "label": "Copy SVG"
            },
            {
                "id": "ViewSVG",
                "label": "View SVG"
            },
            {
                "id": "ViewSource",
                "label": "View Source"
            },
            {
                "id": "SaveAs",
                "label": "Save As"
            },
            null,
            {
                "id": "Help"
            },
            {
                "id": "About",
                "label": "About Adobe CVG Viewer..."
            }
        ]
    }
}

for k1, v1 in json_dict.items():
    print(k1)
    for k2, v2 in v1.items():
        print('  ', k2)
        if type(v2) == str:
            print('    ', v2)
        elif type(v2) == list:
            for item in v2:
                if type(item) == dict:
                    try:
                        print('    ', item['label'])
                    except:
                        print('    ', item['id'])
                elif item == None:
                    print('     ---------')
menu
   header
     SVG Viewer
   items
     Open
     Open New
     ---------
     Zoom In
     Zoom Out
     Original View
     ---------
     Quality
     Pause
     Mute
     ---------
     Find...
     Find Again
     Copy
     Copy Again
     Copy SVG
     View SVG
     View Source
     Save As
     ---------
     Help
     About Adobe CVG Viewer...
