"""Read-only file-metadata audit; writes only its report JSON beside this script."""
import os, sys, json, time, stat, shutil, ctypes
from pathlib import Path
ROOT = Path(r'C:\Users\Owner')
OUT = Path(__file__).parent
start = time.time()
records, large_files, errors, skipped = [], [], [], []
file_count = 0
special = {'node_modules', '.venv', 'venv', '.next', '.nuxt', 'target', '__pycache__', 'dist', 'build', 'Cache', 'Code Cache', 'GPUCache', '_cacache', 'Cache_Data', 'wheels', 'http-v2', 'Temp', 'tmp', 'cache', 'caches', 'models', 'blobs', '.git', 'logs', 'CrashDumps', 'extensions', 'registry', 'toolchains'}
def walk(path, depth=0, in_dependency=False):
    global file_count
    total = count = 0
    try:
        with os.scandir(path) as entries:
            for e in entries:
                try:
                    s = e.stat(follow_symlinks=False)
                    if getattr(s, 'st_file_attributes', 0) & stat.FILE_ATTRIBUTE_REPARSE_POINT:
                        if len(skipped) < 500: skipped.append(e.path)
                        continue
                    if e.is_dir(follow_symlinks=False):
                        b, n = walk(e.path, depth + 1, in_dependency or os.path.basename(path) == 'node_modules')
                        total += b; count += n
                    elif e.is_file(follow_symlinks=False):
                        total += s.st_size; count += 1; file_count += 1
                        if s.st_size >= 250 * 1024**2:
                            large_files.append({'path':e.path,'bytes':s.st_size,'modified':s.st_mtime,'links':s.st_nlink})
                except OSError as ex:
                    if len(errors) < 500: errors.append({'path':e.path,'error':str(ex)})
    except OSError as ex:
        if len(errors) < 500: errors.append({'path':str(path),'error':str(ex)})
    name = os.path.basename(path)
    if depth <= 4 or (name in special and not in_dependency) or (total >= 500*1024**2 and not in_dependency):
        records.append({'path':str(path),'bytes':total,'files':count,'depth':depth,'dependency_nested':in_dependency})
    if depth == 1:
        print(f'{path}: {total/1024**3:.2f} GiB ({count:,} files), elapsed {time.time()-start:.0f}s', flush=True)
    return total, count

walk(str(ROOT))
for extra in [r'C:\$Recycle.Bin',r'C:\tmp',r'C:\Windows\Temp',r'C:\ProgramData\Docker',r'C:\ProgramData\DockerDesktop',r'C:\ProgramData\NVIDIA Corporation\Downloader']:
    if os.path.isdir(extra): walk(extra)
usage = shutil.disk_usage('C:\\')
result = {'scanned_at':time.strftime('%Y-%m-%d %H:%M:%S %z'),'elapsed_seconds':round(time.time()-start,1),'files':file_count,'disk':{'total':usage.total,'used':usage.used,'free':usage.free},'directories':sorted(records,key=lambda r:r['bytes'],reverse=True),'large_files':sorted(large_files,key=lambda r:r['bytes'],reverse=True),'errors':errors,'skipped_reparse_points':skipped}
(OUT/'storage-scan.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(f'DONE: {file_count:,} files in {time.time()-start:.0f}s. JSON: {OUT / "storage-scan.json"}',flush=True)
