"""Read-only Docker inspection. Never starts the daemon or removes anything."""
import subprocess, shutil, json
from pathlib import Path
out=Path(__file__).parent
checks=[]
def run(args,timeout=40):
    try:
        p=subprocess.run(args,capture_output=True,text=True,errors='replace',timeout=timeout)
        row={'command':args,'code':p.returncode,'stdout':p.stdout,'stderr':p.stderr}
    except (subprocess.TimeoutExpired,OSError) as e:
        row={'command':args,'error':str(e)}
    checks.append(row)
    print(json.dumps(row),flush=True)
    return row
if shutil.which('docker'):
    version=run(['docker','version','--format','{{json .Server}}'],25)
    if version.get('code') == 0:
        run(['docker','system','df','-v'],60)
        run(['docker','ps','-a','--size','--format','{{json .}}'],30)
        run(['docker','volume','ls','--format','{{json .}}'],30)
        run(['docker','image','ls','--format','{{json .}}'],30)
    else: print('Docker daemon unavailable; did not start Docker.',flush=True)
else: print('Docker executable unavailable.',flush=True)
(out/'docker-inspection.json').write_text(json.dumps(checks,indent=2),encoding='utf-8')
