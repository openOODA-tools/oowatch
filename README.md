# oowatch

> **Continuous command scheduler and delta watcher with ANSI diff highlighting for the openOODA era.**  
> *A drop-in `watch` alternative written in pure openOODA, featuring capability-bounded process execution (`ProcessCap`, `TimeCap`), dynamic delta diff highlighting via `oote` themes, iteration bounds, and a first-class Model Context Protocol (MCP) surface.*

Part of [openOODA-tools](https://github.com/openOODA-tools).

---

## 1. Installation

`oowatch` has zero runtime dependencies. It compiles to a standalone native binary linked directly with libc.

### Universal Web Installer
Installs the standalone native binary to `/usr/local/bin` (or `~/.local/bin`):

```bash
curl -fsSL https://openooda-tools.github.io/oowatch/install.sh | bash
```

### Debian / Ubuntu (APT)
```bash
# Automated via installer
curl -fsSL https://openooda-tools.github.io/oowatch/install.sh | bash -s -- --apt

# Or manual package install
sudo dpkg -i oowatch_0.1.0-1_amd64.deb
```

### Fedora / RHEL / CentOS (DNF)
```bash
# Automated via installer
curl -fsSL https://openooda-tools.github.io/oowatch/install.sh | bash -s -- --dnf

# Or manual RPM install
sudo dnf install ./oowatch-0.1.0-1.fc44.x86_64.rpm
```

### Arch Linux (PKGBUILD)
```bash
# Automated via installer
curl -fsSL https://openooda-tools.github.io/oowatch/install.sh | bash -s -- --arch

# Or manual build via packaging/PKGBUILD
cd packaging && makepkg -si
```

### Clean Uninstaller
To cleanly remove `oowatch` and any installed package manager entries:

```bash
# Automated via standalone uninstaller
curl -fsSL https://openooda-tools.github.io/oowatch/uninstall.sh | bash

# Or via installer flag
curl -fsSL https://openooda-tools.github.io/oowatch/install.sh | bash -s -- --uninstall

# Or preview removal without making changes (dry-run)
curl -fsSL https://openooda-tools.github.io/oowatch/uninstall.sh | bash -s -- --dry-run
```

---

## 2. Usage & Features

### Continuous Monitoring & Delta Highlighting
Periodically execute commands and view outputs in real time:

```bash
# Run command every 2 seconds (default)
oowatch uptime

# Custom refresh interval of 1 second with delta highlighting
oowatch -n 1 -d free -m

# Suppress status header bar
oowatch -t date

# Run 5 iterations and exit
oowatch -c 5 -n 1 ps aux

# Single-shot execution snapshot
oowatch -1 df -h
```

### Model Context Protocol (MCP) Server
`oowatch` features a native Model Context Protocol (MCP) stdio server allowing AI pair programmers and LLM coding assistants to execute scheduled observations and detect system deltas:

```bash
oowatch --mcp
```

#### Exposed MCP Tools:
- `watch_poll`: Executes a target host command once under `ProcessCap` and returns standard output with line counts.
- `watch_diff`: Executes a command twice separated by an interval and returns structured outputs with delta change flags.
- `watch_status`: Inspects active `oowatch` runtime engine capabilities and metadata.

---

## 3. License

Apache License 2.0. See [LICENSE](LICENSE) for details.