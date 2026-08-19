# Portable Dependency Closures

These capsules make selected recursive verifiers independent of the historical
directory layout. Each manifest names exact SHA-256 blobs and excludes absolute
machine paths.

`q79_qg_terminal/` contains the complete reachable dependency graph of the
selected q79 quantum-gravity terminal packet: 77 unique files joined by 206
declared hash edges. Its status is `INTEGRITY_SUPPORT_ONLY`. Inclusion preserves
bytes and availability; it does not promote a theorem, resolve an open packet,
or replace any packet-level check.

Rebuild it from the pinned adjacent source workspace with:

```powershell
python tools/build_dependency_closure.py
```
