#!/usr/bin/env python3
"""Build the deterministic DOI-preparation source and PDF payloads."""

from datetime import datetime, timezone
from hashlib import md5, sha256
from pathlib import Path
from shutil import copyfile
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


ROOT = Path(__file__).resolve().parents[1]
RELEASE = ROOT / "release"
SOURCE_EPOCH = 1788048000

PAYLOAD_PATTERNS = (
    ".gitignore",
    ".github/workflows/*.yml",
    ".zenodo.json",
    "AI_DISCLOSURE.md",
    "AUDIT_INDEX.md",
    "CITATION.cff",
    "LICENSE",
    "LICENSE-CODE",
    "LICENSE-MANUSCRIPT",
    "MANUSCRIPT_STATUS.md",
    "Makefile",
    "README.md",
    "RELEASE_MANIFEST.md",
    "RELEASE_NOTES.md",
    "VERSION",
    "ZENODO_CHECKLIST.md",
    "audits/*.md",
    "main.tex",
    "output/pdf/binary-3qi-cores-preprint.pdf",
    "references.bib",
    "requirements.txt",
    "supplementary/README.md",
    "supplementary/*.py",
)


def digest(path, algorithm):
    value = algorithm()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            value.update(chunk)
    return value.hexdigest()


def payload_files():
    files = set()
    for pattern in PAYLOAD_PATTERNS:
        files.update(path for path in ROOT.glob(pattern) if path.is_file())
    return sorted(files, key=lambda path: path.relative_to(ROOT).as_posix())


def write_source_manifest(files):
    lines = [
        "{}  ./{}".format(
            digest(path, sha256), path.relative_to(ROOT).as_posix()
        )
        for path in files
        if path.name != "SHA256SUMS"
    ]
    manifest = ROOT / "SHA256SUMS"
    manifest.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return sorted(files + [manifest], key=lambda path: path.relative_to(ROOT).as_posix())


def deterministic_zip(archive, prefix, files):
    timestamp = datetime.fromtimestamp(SOURCE_EPOCH, timezone.utc)
    date_time = (timestamp.year, timestamp.month, timestamp.day,
                 timestamp.hour, timestamp.minute, timestamp.second)
    with ZipFile(archive, "w", compression=ZIP_DEFLATED, compresslevel=9) as bundle:
        for path in files:
            relative = path.relative_to(ROOT).as_posix()
            info = ZipInfo("{}/{}".format(prefix, relative), date_time=date_time)
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            info.create_system = 3
            bundle.writestr(info, path.read_bytes(), compress_type=ZIP_DEFLATED,
                            compresslevel=9)


def main():
    version = (ROOT / "VERSION").read_text(encoding="utf-8").splitlines()[0]
    if not version.startswith("v"):
        raise RuntimeError("VERSION must begin with a v-prefixed version line")

    source_pdf = ROOT / "output/pdf/binary-3qi-cores-preprint.pdf"
    if not source_pdf.is_file() or source_pdf.stat().st_size == 0:
        raise RuntimeError("build the manuscript PDF before packaging")

    RELEASE.mkdir(exist_ok=True)
    release_pdf = RELEASE / "binary-3qi-cores-preprint-{}.pdf".format(version)
    archive = RELEASE / "binary-3qi-cores-{}.zip".format(version)
    copyfile(source_pdf, release_pdf)

    files = write_source_manifest(payload_files())
    deterministic_zip(archive, "binary-3qi-cores-{}".format(version), files)

    release_files = (archive, release_pdf)
    (RELEASE / "SHA256SUMS").write_text(
        "".join("{}  {}\n".format(digest(path, sha256), path.name)
                for path in release_files),
        encoding="utf-8",
    )
    (RELEASE / "MD5SUMS").write_text(
        "".join("{}  {}\n".format(digest(path, md5), path.name)
                for path in release_files),
        encoding="utf-8",
    )
    print("RELEASE_PDF={}".format(release_pdf.relative_to(ROOT)))
    print("RELEASE_ZIP={}".format(archive.relative_to(ROOT)))
    print("RELEASE_PACKAGE_OK")


if __name__ == "__main__":
    main()
