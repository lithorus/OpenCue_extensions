
import hou
import soho

print("OpenCue_Render_soho.py")

def render():
    soho.init()
    frame = soho.getDefault('now', 1.0)
    print(f"[export_scene] Exporting full scene at frame {frame}")
    # 6. Finalize the SOHO process cleanly
    soho.finalize()
